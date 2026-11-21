import sys
import os
import json


class Parser:

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

    def __remove_coments(self, content: str) -> None:
        lines_content = self.__json_parser.parse(content)


    def split_json_structure(self, content: str) -> None:

        
    def parse(self) -> None:
        self.__remove_comments(self.__read_config_file)

         

        



 

 



if __name__ == '__main__':

    parser = Parser()
