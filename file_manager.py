import os


class FileManager:
    @staticmethod
    def _normalize_file_name(file_name):
        file_name = file_name.strip()
        if len(file_name) >= 2 and file_name[0] == file_name[-1] and file_name[0] in ("\"", "'"):
            return file_name[1:-1]
        return file_name

    def create_file(self, file_name, content):
        file_name = self._normalize_file_name(file_name)
        with open(file_name, "w") as file:
            file.write(content)

    def read_file(self, file_name):
        file_name = self._normalize_file_name(file_name)
        if not os.path.exists(file_name):
            return None

        with open(file_name, "r") as file:
            return file.read()

    def delete_file(self, file_name):
        file_name = self._normalize_file_name(file_name)
        if not os.path.exists(file_name):
            return False

        os.remove(file_name)
        return True