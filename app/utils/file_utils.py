import csv
from pathlib import Path
from typing import Callable

import logging


def file_exists(file_path: str) -> None:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"{file_path} not exist")


def read_binary(
    file_path: str,
) -> bytes:
    file_exists(file_path)

    with open(file_path, "rb") as f:
        data = f.read()
    return data


def read_csv(file_path: str) -> list[dict]:
    file_exists(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        data = [
            {key: value for key, value in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)
        ]
    return data


def write_csv(data: list[dict], file_path: str) -> None:
    file_exists(file_path)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            fields = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
    except csv.Error as exception:
        logging.error("file_path: %s, exception: %s", file_path, exception)


def validated_file_list(
    root_file_path: str,
    file_format_validation: Callable[[str], bool] | None = None,
) -> list[str]:
    if file_format_validation is None:
        return [
            str(path)
            for path in Path(root_file_path).glob("**/*")
            if path.is_file()
        ]
    else:
        return [
            str(path)
            for path in Path(root_file_path).glob("**/*")
            if path.is_file() and file_format_validation(str(path))
        ]
