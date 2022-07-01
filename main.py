
import os
import shutil
import pathlib
import timeit

FROM_PATH = ".\\"
TO_PATH = ".\\results"
WHITELIST = {"png", "jpg"}

def make_end_result_directory(path) -> None:
	''' sets up the result folder if not existent '''
	if not os.path.isdir(path):
		os.mkdir(path)

def gather_all_files_generator(path: str) -> str:
	for path, d_names, f_names in os.walk(path):
		if TO_PATH not in path:
			for f in f_names:
				yield os.path.join(path, f)


def get_extension(file: str) -> str:
	''' string formatting to get the extension type as str '''
	return pathlib.Path(file).suffix[1:]

def create_file_extension_folders() -> None:
	''' creates a folder for each extension in the whitelist '''
	for ext in WHITELIST:
		try:
			os.mkdir(f"{TO_PATH}\\{ext}")
		except FileExistsError:
			print(f"Warning : folder {ext} exists already.")


def copy_file_to_ext_folder(file: str, ext: str) -> None:
	''' copies file to extension specific folder '''
	try:
		shutil.copy(file, f"{TO_PATH}\\{ext}")
	except shutil.SameFileError:
		print(f"File {file} exists already.") # was causing an error previously because TO_PATH was being walked while files were copied over...


def main(root) -> None:
	create_file_extension_folders()
	for file in gather_all_files_generator(root):
		file_extension = get_extension(file)
		if file_extension in WHITELIST:
			copy_file_to_ext_folder(file, file_extension)


if __name__ == "__main__":
	make_end_result_directory(TO_PATH)
	main(FROM_PATH)
