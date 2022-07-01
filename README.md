# file_by_extension_mover
Moves all files below the script's current path and sort them by extension in folders (uses os.walk to go through all nested folders)

Just drop it in a folder and run the script.

There's a WHITELIST set within the script containing the extensions the program will create folders for.
FROM_PATH is by default the current script's folder
TO_PATH is by default a result folder (generated during setup if non-existent).


Some todo:
1) Don't get all the file extensions, instead implement a sorting/binary search to reduce function call
2) Add a way to use shutil.move instead of copy for those who like to live dangerously

DISCLAIMER : 
It is not recommended to add "py" to the WHITELIST when running the script with its default FROM_PATH.
This is a very crude tool, so use at your own risk.
