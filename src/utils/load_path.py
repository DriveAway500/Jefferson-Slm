from pathlib import Path

class LoadPath():

    @staticmethod
    def loadby_extension_path(extension):

        base_path = Path(__file__).resolve().parent
        data_path = base_path.parent / "data/raw/"

        extension=list(extension.split(", "))

        files=[]

        for ext in extension:
                files_path= list(data_path.rglob(ext))
                files.extend(files_path)

        return files

    @staticmethod
    def loadby_txt_file_path():

        # only for .txt
        base_path = Path(__file__).resolve().parent

        data_path = base_path.parent / "data/raw/"

        files= list(data_path.rglob("*.txt"))

        return files