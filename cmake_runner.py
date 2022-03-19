import os
import sys
from project_settings import Variant
import project_settings
import argparse
import platform



def create_build_dir(build_dir):
	if os.path.exists(build_dir):
		return
	if platform.system() == "Windows":
		cmd = "mkdir " + build_dir
		os.system(cmd)

def delete_build_dir(build_dir):
	if platform.system() == "Windows":
		cmd = "rd /s /q " + build_dir
		os.system(cmd)

def get_selected_variant():
	variant = project_settings.read_project_variants()[0]
	return variant

def execute_configure_command(workspace, build_dir):
	os.chdir(workspace)
	create_build_dir(build_dir)
	cmd = "cmake -GNinja -S\"" + workspace + "\" -B\"" + build_dir + "\""
	os.system(cmd)

def execute_build_command(workspace, build_dir):
	os.chdir(workspace)
	cmd = "cmake --build " + build_dir
	os.system(cmd)

def execute_flash_command(workspace, build_dir):
	os.chdir(workspace)
	cmd = "cmake --build " + build_dir + " --target flash"
	os.system(cmd)

def execute_rebuild_command(workspace, build_dir):
	os.chdir(workspace)
	delete_build_dir(build_dir)
	execute_configure_command(workspace, build_dir)
	execute_build_command(workspace, build_dir)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Cmake runner application')
	parser.add_argument('action', type=str, choices={'build', 'rebuild', 'flash', 'run', 'configure'}, help='Command to run')
	parser.add_argument('workspace', type=str, help='Workspace of the project to build')
	args = parser.parse_args()

	variant = get_selected_variant()
	build_dir = "build-" + variant.variantName
	
	if args.action == 'configure':
		execute_configure_command(args.workspace, build_dir)
	elif args.action == 'build':
		execute_build_command(args.workspace, build_dir)
	elif args.action == 'rebuild':
		execute_rebuild_command(args.workspace, build_dir)
	elif args.action == 'run':
		execute_flash_command(args.workspace, build_dir)