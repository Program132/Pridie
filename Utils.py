import os


def is_valid_file_path(file_path):
    return os.path.exists(file_path)
