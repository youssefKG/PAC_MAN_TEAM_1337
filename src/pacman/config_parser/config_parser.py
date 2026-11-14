import os

class ConfigParserError(Exception):
    pass

class ConfigParser:
    def __init__(self, file_path: str) -> None:
        self.__file_path: str = file_path
        self.__width: int | None =  None
        self.__height: int | None = None

    def parse(self) -> None:
        if not os.access(self.__file_path, os.F_OK):
            raise ConfigParserError("Config file error: file path {self.__file_path} not found")
        elif not os.access(self.__file_path, os.R_OK):
            raise ConfigParserError("Config file error: Config file is not found {self.__file_path}")
        with open(self.__file_path, "r") as config_file:
            pass
