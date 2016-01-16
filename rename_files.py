import os

def rename_files():
    file_list = os.listdir("/Users/dennyvuong/Desktop/python_foundations/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/dennyvuong/Desktop/python_foundations/prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1234567890"))
    os.chdir(saved_path)
    print(file_list)

rename_files()
