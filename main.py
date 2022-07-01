
import os
import shutil
import pathlib

FROM_PATH = ".\\"
TO_PATH = ".\\results"
WHITELIST = {"png", "jpg"}

def setup(result_path) -> None:
	''' sets up the result folder if not existent '''
	if not os.path.isdir(result_path):
		os.mkdir(result_path)


def gather_all_files(path: str) -> list:
	''' returns a list of all nested files in path '''
	files = []
	for path, d_names, f_names in os.walk(path):
		for f in f_names:
			files.append(os.path.join(path, f))
	return files


def get_extension(file: str) -> str:
	''' string formatting to get the extension type as str '''
	return pathlib.Path(file).suffix[1:]

def create_file_extension_folders() -> None:
	''' creates a folder for each extension in the whitelist '''
	for ext in WHITELIST:
		try:
			os.mkdir(f"{TO_PATH}\\{ext}")
		except FileExistsError:
			print(f"{ext} folder already generated.")


def copy_file_to_ext_folder(file: str, ext: str) -> None:
	''' copies file to extension specific folder '''
	shutil.copy(file, f"{TO_PATH}\\{ext}")

def main(root) -> None:
	create_file_extension_folders()
	for file in gather_all_files(root):
		ext = get_extension(file)
		if ext not in WHITELIST:
			break
		copy_file_to_ext_folder(file, ext)

if __name__ == "__main__":
	setup(TO_PATH)
	main(FROM_PATH)
