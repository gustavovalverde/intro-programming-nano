import os


def rename_files():
    files_path = os.listdir("C:\Users\GustavoA\intro-programming-nano"
                            "\Python\Functions\Secret-message\prank")
    saved_path = os.getcwd()
    os.chdir("C:\Users\GustavoA\intro-programming-nano\Python\Functions"
             "\Secret-message\prank")
    for file_name in files_path:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
