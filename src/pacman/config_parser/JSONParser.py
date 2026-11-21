from . import FSMJson



class JSONParser:

    def __init__(self) -> None:
        self.previous_state; FSMJson = FSMJson.IN_START
        self.current_state: FSMJson = FSMJson.IN_START
        self.is_escape: bool = False
        self.cleaned_json: str = ''

    def parse_in_start(self, character: str) -> None:
        if character == '#':
            self.current_state = FSMJson.IN_COMMENT:
        elif character == '{':
            self.cleaned_json += character
            self.current_state = FSMJson.IN_JSON:
        elif character.isspace():
            pass
        else:
            raise JSONDecodeError("Error: Invalid json, json must start with {")

    def parse_in_comment(self, character: str) -> None:
        if character == '\n':
            self.current_state = FSMJson.IN_JSON

    def parse_in_json(self, character: str) -> None:
        if character.isspace():
            pass
        elif character == '}':
            self.cleaned_json += character
            self.current_state = FSMJson.IN_END
        elif character == '#':
            self.current_state = FSMJson.IN_COMMENT
        elif character == '"':
            self.clean_json += character
            self.current_state = FSMJson.IN_STRING

    def parse_in_string(self, character: str) -> None:
        if character == '"' and self.escape:
            self.cleaned_json += character
            self.escape = False
        elif character == '"' and not self.escape:
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
        elif character == "#":
            self.current_state = FSMJson.IN_COMMENT
        elif character.isspace():
            pass
        else:
            raise JSONDecodeError("Error: Invalid Json, found normal character after closing json")

    def parse(self, content_file: str) -> None:
        for character in content:
            if self.current_state == fSMJson.IN_START:
                self.parse_in_start(character)
            elif self.current_state == FSMJson.IN_JSON:
                self.parse_in_json(character)
            elif self.current_state == FSMJson.IN_STRING:
                self.parse_in_string(character)
            elif self.current_state == FSMJson.IN_COMMENT:
                self.parse_in_comment(character)
            elif self.current_state == FSMJson.IN_END:
                self.parse_in_end(character)

        if self.current_state != FSMJson.IN_END:
            raise JSONDecodeError(f"json not completed !")

