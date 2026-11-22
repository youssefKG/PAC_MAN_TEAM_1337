import sys
import os
import json
from typing import Any
from JSONParser import JSONParser
from ConfigModel import Config


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
        config = Config.model_validate_json(cleaned_json)
        return config

if __name__ == '__main__':
    config_parser = ConfigParser(JSONParser())
    print("check argument well!.")
    print("*****" * 7)
    config = config_parser.parse()
    print("highscore_filename:", config.highscore_filename)
    print("levels:", config.levels)
    print("width:", config.width)
    print("height:", config.height)
    print("pacgum:", config.pacgum)
    print("points_per_pacgum:", config.pacgum)
    print("points_per_super_pacgum:", config.points_per_super_pacgum)
    print("seed:", config.seed)
    print("level_max_time:", config.seed)




