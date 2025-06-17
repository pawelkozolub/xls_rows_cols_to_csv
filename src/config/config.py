import tomllib
import os.path

class Config():
    def __init__(self):
        cfg = self.read_config("config.toml")
        dir = cfg["data_dir"]
        file = cfg["input_file"]
        output = cfg["output_file"]
        data = cfg["config_data"]
        self.input_file = self.get_abs_path(dir, file)
        self.output_file = self.get_abs_path(dir, output)
        
        cfg = self.read_config(data)
        self.column_data = cfg["column_data"]
        self.row_data = cfg["row_data"]

    @staticmethod
    def read_config(filename: str) -> dict:
        with open(filename, "rb") as f:
            config = tomllib.load(f)
        return config
    
    @staticmethod
    def get_abs_path(directory: str, file: str) -> str:
        dir: list[str] = directory.split("/")
        path = ""
        for d in dir:
            path = os.path.join(path, d)
        rel_path = os.path.join(path, file)
        abs_path = os.path.realpath(rel_path)
        return abs_path