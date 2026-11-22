import sys
import os
import json
from typing import Any
from JSONParser import JSONParser
from enum import Enum, auto

class ConfigKeys(Enum):
    highscore_filename = auto()
    levels = auto()
    width = auto()
    height = auto()
    pacgum = auto()
    points_per_pacgum = auto()
    points_per_super_pacgum = auto()
    points_per_ghost = auto()
    seed = auto()
    level_max_time = auto()


class ConfigParser:

    def __init__(self, json_parser: JSONParser) -> None:

        self.__display_usage()
        self.__is_json(sys.argv[1])
        self.__is_exists(sys.argv[1])
        self.__can_access(sys.argv[1])
        self.__config_file: str = sys.argv[1]
        self.__json_parser = json_parser
        
    def __display_usage(self) -> None:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 pac-man.py config.json")

    def __is_json(self, config_file: str) -> None:
        if not config_file.endswith(".json"):
            raise TypeError('Error: {config_file} must ends with .json suffix!')

    def __is_exists(self, config_file: str) -> None:
       if not os.path.exists(config_file):
            raise FileNotFoundError(f"Error: {config_file} not exists!")

    def __can_access(self, config_file: str) -> None:
       if not os.access(config_file, os.R_OK):
            raise PermissionError(f"Error: {config_file} Permission denied!")

    def __read_config_file(self) -> str:
         with open(self.__config_file, "r", encoding='utf-8') as file:
            return file.read()

    def parse(self) -> None:
        content = self.__read_config_file()
        cleaned_json = self.__json_parser.parse(content)
        config = self.__json_parser.load_config(cleaned_json)
        print("member names: ", ConfigKeys._member_names_)

        for key_config, value_config in config.items():
            if key_config in ConfigKeys._member_names_:
                # continue here should pass configbuilder for building config and set defaults values
                pass
        
# try:
config_parser = ConfigParser(JSONParser())
print("check argument well!.")
print("*****" * 7)
print(config_parser.parse())

# except Exception as e:
#     print(e)

