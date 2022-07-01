
import os
import shutil
import pathlib

FROM_PATH = ".\\"
TO_PATH = ".\\results"
WHITELIST = {"png", "jpg"}

def setup():
	if not os.path.isdir(TO_PATH):
		os.mkdir(TO_PATH)

def gather_files(path) -> list:
	gathered_files = []
	for path, d_names, f_names in os.walk(path):
		for f in f_names:
			gathered_files.append(os.path.join(path, f))
			print(f)
	return gathered_files

def get_extension(file) -> str:
	return pathlib.Path(file).suffix[1:]

def create_file_extension_folders():
	for file_extension in WHITELIST:
		try:
			os.mkdir(f"{TO_PATH}\\{file_extension}")
		except FileExistsError:
			print(f"{file_extension} folder already generated.")

def copy_files_to_extension_folder(file, ext):
	shutil.copy(file, f"{TO_PATH}\\{ext}")

def main():
	create_file_extension_folders()
	for file in gather_files(FROM_PATH):
		ext = get_extension(file)
		if ext not in WHITELIST:
			break
		copy_files_to_extension_folder(file, ext)

if __name__ == "__main__":
	setup()
	main()
