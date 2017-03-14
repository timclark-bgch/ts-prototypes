import os
import shutil
import sys


def package(files, requirements, build_directory):
	__check_files(files)
	__create_destination(build_directory)
	__pip_install(requirements, build_directory)
	__copy_files(files, build_directory)
	__make_zip_file('package', build_directory)


def __check_files(files):
	for f in files:
		if not os.path.exists(f):
			print "The file {} doesn't exist".format(f)
			sys.exit(1)


def __create_destination(destination):
	if os.path.exists(destination):
		shutil.rmtree(destination)
	os.mkdir(destination)


def __pip_install(requirements, destination):
	os.system('pip install -t {} -r {}'.format(destination, requirements))


def __copy_files(files, destination):
	for f in files:
		dest_path = '{}/{}'.format(destination, f)
		if os.path.exists(dest_path):
			print('{} clashes with a file or directory in the build directory.')
			sys.exit(1)

		print 'Copying: {} -> {}'.format(f, dest_path)
		if os.path.isdir(f):
			shutil.copytree(f, dest_path)
		else:
			shutil.copy2(f, dest_path)


def __make_zip_file(file_name, source):
	shutil.make_archive(file_name, 'zip', source)
