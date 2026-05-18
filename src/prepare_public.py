import os
import shutil


def prepare_public():
    if os.path.exists("./public/"):
        shutil.rmtree("public")
        print("Removed public")

    os.mkdir("public")
    print("Created public")
    copy_static_to_public()
    return


def copy_static_to_public(current_path: str = ""):
    source_dir = os.path.join("static", current_path)
    target_dir = os.path.join("public", current_path)
    files = os.listdir(source_dir)
    for file in files:
        file_path = os.path.join(source_dir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_dir)
            print(f"Copied file {file_path} to {target_dir}")
        else:
            os.mkdir(os.path.join(target_dir, file))
            print(f"Created folder {os.path.join(target_dir, file)}")
            copy_static_to_public(os.path.join(current_path, file))

    return
