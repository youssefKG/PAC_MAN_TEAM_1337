import json
from typing import Any
from FSMParser import FSMJson

class JSONParser:

    def __init__(self) -> None:
        self.previous_state: FSMJson = FSMJson.IN_START
        self.current_state: FSMJson = FSMJson.IN_START
        self.escape: bool = False
        self.cleaned_json: str = ''
        self.stack_brackets: list[str] = []

    def brackets_to_stack(self, character: str) -> None:
        if character in "{[":
            self.stack_brackets.append(character)
        elif character in "}]":
            if not len(self.stack_brackets):
                raise json.JSONDecodeError(msg=f"Unexpected closing bracket '{character}'", doc="darwin", pos=1)
            else:
                self.stack_brackets.pop()
        else:
            raise json.JSONDecodeError(msg="Darwin Error should pass to brackets_to_stack() only valid brackets", doc="darwin", pos=1)

    def parse_in_start(self, character: str) -> None:
        if character == '#':
            self.previous_state = FSMJson.IN_JSON
            self.current_state = FSMJson.IN_COMMENT
        elif character in '[{}]':
            self.cleaned_json += character
            self.previous_state = FSMJson.IN_JSON
            self.current_state = FSMJson.IN_JSON
            self.brackets_to_stack(character)
        elif character.isspace():
            pass
        else:
            raise json.JSONDecodeError(msg=f"Error: Unexpected character \'{character}\', json start with open brace", doc="darwin", pos=1)

    def parse_in_comment(self, character: str) -> None:
        if character == '\n':
            self.current_state = self.previous_state

    def parse_in_json(self, character: str) -> None: # " } # whitespace
        if character.isspace():
            pass
        elif character in '[{}]':
            self.cleaned_json += character
            self.brackets_to_stack(character)
        elif character == '#':
            self.previous_state = self.current_state
            self.current_state = FSMJson.IN_COMMENT
        elif character == '"':
            self.cleaned_json += character
            self.previous_state = self.current_state
            self.current_state = FSMJson.IN_STRING
        else:
            self.cleaned_json += character

    def parse_in_string(self, character: str) -> None:
        if character == '"' and self.escape == True:
            self.cleaned_json += character
            self.escape = False
        elif character == '"' and self.escape == False:
            self.cleaned_json += character
            self.current_state = FSMJson.IN_JSON
            self.escape = False
        elif character == '\\':
            self.cleaned_json += character
            self.escape = True
        else:
            self.cleaned_json += character
            self.escape = False

    def parse_in_end(self, character: str) -> None:
        if character.isspace():
            pass
        elif character == "#":
            self.previous_state = self.current_state
            self.current_state = FSMJson.IN_COMMENT
        else:
            raise json.JSONDecodeError(msg="Error: Invalid Json, found normal character after closing json", doc="darwin", pos=1)

    def load_config(self, cleaned_json: str) -> dict[str, Any]:
        return json.loads(cleaned_json)

    def parse(self, content: str) -> None:
        for character in content:
            if self.current_state == FSMJson.IN_START:
                self.parse_in_start(character)

            elif self.current_state == FSMJson.IN_JSON:
                self.parse_in_json(character)

            elif self.current_state == FSMJson.IN_STRING:
                self.parse_in_string(character)

            elif self.current_state == FSMJson.IN_COMMENT:
                self.parse_in_comment(character)

            elif self.current_state == FSMJson.IN_END:
                self.parse_in_end(character)

        if self.current_state != FSMJson.IN_END and self.stack_brackets:
            raise json.JSONDecodeError(pos=1, msg=f"json not completed!", doc="darwin")

        return self.cleaned_json
