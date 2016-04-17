import os


def rename_files():
    files_path = os.listdir("/home/vagrant/intro-programming"
                            "/Python/Functions/Secret-message/prank")
    for file_name in files_path:
        os.rename(file_name, file_name.translate(None, "0123456789"))

print os.getcwd()
rename_files()

