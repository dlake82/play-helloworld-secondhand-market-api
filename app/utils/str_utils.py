def get_splited_file_path(file_path: str) -> list[str]:
    splited_file_path = file_path.split("/")
    if splited_file_path[0] == "":
        return splited_file_path[1:]
    return splited_file_path
