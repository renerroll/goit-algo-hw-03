from pathlib import Path
import shutil
import argparse
import os


def copy_files(source, destination):
    if not destination.exists():
        print("Створена тека призначення в поточній теки")
        destination.mkdir()

    for current_path in source.iterdir():
        if current_path.is_dir():
            copy_files(current_path, destination)
        else:
            has_access = check_access(current_path)
            is_new_folder_path = create_folder_by_extension(current_path, destination)
            if has_access and is_new_folder_path:
                copy_path = check_duplicates(current_path, is_new_folder_path)

                shutil.copy(current_path, copy_path)


def create_folder_by_extension(file_path, destination_folder):
    file_extension = file_path.suffix.lower()

    if file_extension:
        folder_path = destination_folder.joinpath(file_extension[1:])

        if not folder_path.exists():
            folder_path.mkdir()

        return folder_path

    return None


def check_access(file_path):
    try:
        # Перевірка доступу на читання / запис / виконання поточного файлу
        os.access(file_path, os.R_OK | os.W_OK | os.X_OK)
        return True

    except Exception as e:
        print(f"Немає прав доступу: {e}")
        return False


def check_duplicates(file_path, destination_folder):
    file_name = file_path.stem
    file_extension = file_path.suffix

    copy_path = destination_folder / f"{file_name}{file_extension}"

    index = 1
    while copy_path.exists():
        unique_name = f"{file_name}_copy_{index}"
        copy_path = destination_folder / f"{unique_name}{file_extension}"
        index += 1

    return copy_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Копіювання файлів")

    parser.add_argument(
        "--source",
        default=Path.cwd(),
        type=Path,
        help="Шлях до директорії джерела",
        required=False,
    )
    parser.add_argument(
        "--destination",
        default=Path("./dist"),
        type=Path,
        help="Шлях до директорії призначення",
        required=False,
    )

    args = parser.parse_args()

    copy_files(args.source, args.destination)
    print("Завдання виконано")
