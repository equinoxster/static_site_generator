import os
import shutil
from textnode import *

src_dir = "static"
dest_dir = "public"
def main():
    copy_content()

def copy_content():
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    current_dir = src_dir
    copy_files_and_folder(current_dir)
    


def copy_files_and_folder(current_dir):
    if os.path.isdir(current_dir):
        print(os.listdir(current_dir))
        for file in os.listdir(current_dir):
            file_handle = current_dir + "/" + file
            if os.path.isdir(file_handle):
                os.mkdir(file_handle.replace(src_dir, dest_dir))
                copy_files_and_folder(file_handle)
            else:
                shutil.copy(file_handle, file_handle.replace(src_dir, dest_dir))

main()
