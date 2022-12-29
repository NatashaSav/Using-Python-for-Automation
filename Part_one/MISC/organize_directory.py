import os
from pathlib import Path


class DirectoriesConstants:
    SUBDIRECTORIES: dict = {
        "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
        "AUDIO": ['.m4a', '.m4b', '.mp3'],
        "VIDEOS": ['.mov', '.avi', '.mp4'],
        "IMAGES": ['.jpg', '.jpeg', '.png']
    }

    MISC_DIRECTORY: str = 'MISC'


class OperationsWithDirectory:

    @staticmethod
    def pick_directory(value: str) -> str:
        for category, suffixes in DirectoriesConstants.SUBDIRECTORIES.items():
            for suffix in suffixes:
                if suffix == value:
                    return category
        return DirectoriesConstants.MISC_DIRECTORY

    def organize_directory(self):
        for item in os.scandir():
            if item.is_dir():
                continue
            file_path = Path(item)
            file_type = file_path.suffix.lower()
            directory = self.pick_directory(file_type)
            directory_path = Path(directory)
            if not (directory_path.name in os.getcwd()):
                directory_path.mkdir()
                file_path.rename(directory_path.joinpath(file_path))
            else:
                print("directory {0} is already created".format(directory))


if __name__ == "__main__":
    new_directory = OperationsWithDirectory()
    new_directory.pick_directory(DirectoriesConstants.MISC_DIRECTORY)
    new_directory.organize_directory()
