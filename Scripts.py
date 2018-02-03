"""
This function takes the name of a directory
and prints out the paths files within that
directory as well as any files contained in
contained directories.

This function is similar to os.walk. Please don't
use os.walk in your answer. We are interested in your
ability to work with nested structures.
"""
import os


def print_directory_contents(path):
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


print_directory_contents("..")


