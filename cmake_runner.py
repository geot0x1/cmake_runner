import os
import sys
import project_variants
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

def get_cmake_definitions(variant):
	definitions = "-DCMAKE_MAKE_PROGRAM=Ninja.exe "
	for i in variant.settings:
		d = "-D" + i + "=" + variant.settings[i] + " "
		definitions += d
	return definitions

def execute_configure_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	create_build_dir(build_dir)
	definitions = get_cmake_definitions(variant)
	cmd = "cmake -GNinja -S\"" + workspace + "\" -B\"" + build_dir + "\" " + definitions
	os.system(cmd)

def execute_build_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	cmd = "cmake --build " + build_dir
	os.system(cmd)

def execute_flash_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	cmd = "cmake --build " + build_dir + " --target flash"
	os.system(cmd)

def execute_rebuild_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	delete_build_dir(build_dir)
	execute_configure_command(workspace, build_dir)
	execute_build_command(workspace, build_dir)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Cmake runner application')
	parser.add_argument('action', type=str, choices={'build', 'rebuild', 'flash', 'run', 'configure'}, help='Command to run')
	parser.add_argument('workspace', type=str, help='Workspace of the project to build')
	args = parser.parse_args()
	

	variant = project_variants.get_selected_project_variant(args.workspace)
	
	if args.action == 'configure':
		execute_configure_command(args.workspace, variant)
	elif args.action == 'build':
		execute_build_command(args.workspace, variant)
	elif args.action == 'rebuild':
		execute_rebuild_command(args.workspace, variant)
	elif args.action == 'run':
		execute_flash_command(args.workspace, variant)