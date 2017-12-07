def print_directory_contents(sPath):
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
    for sChild in os.listdir(sPath):
        child_path = os.path.join(sPath, sChild)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


print_directory_contents("..")


