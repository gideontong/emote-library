from emotify.convert import convert_to_all_formats
from os import listdir
from os.path import isdir


def auto_convert_everything(import_folder: str):
    if isdir(import_folder):
        pass
    else:
        # TODO: Do something if the parameter is bad
        pass
