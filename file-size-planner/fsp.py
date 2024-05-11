def save_string(string: str, file_name: str, size: int) -> None:

    with open(file_name, "w") as file:
        current_size = 0
        while current_size < size * 1024:
            file.write(string)
            current_size += len(string.encode("utf-8"))


if __name__ == "__main__":

    string_to_save = "1889,44.388221,11.586389,79.8, 00:35:08,13.66,101006.92,80.81,13.35,73.34,2.0,2.0,2.0\n"
    file_size = 10
    save_string(string_to_save, "test.txt", file_size)

    print(f"File saved")
