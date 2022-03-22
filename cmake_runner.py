import os
import sys
import project_variants
import argparse
import platform
import yaml


def get_cmake_runner_settings():
	CURRENT_SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
	settings_file = os.path.join(CURRENT_SCRIPT_DIR, "cmake_runner_settings.yaml")
	f = open(settings_file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	return yamlfile

def create_build_dir(build_dir):
	if os.path.exists(build_dir):
		return
	if platform.system() == "Windows":
		cmd = "mkdir " + build_dir
		print("Running command: " + cmd)
		os.system(cmd)

def delete_build_dir(build_dir):
	if platform.system() == "Windows":
		cmd = "rd /s /q " + build_dir
		print("Running command: " + cmd)
		os.system(cmd)

def get_cmake_definitions(variant):
	cmake_runner_settings = get_cmake_runner_settings()
	definitions = ""
	if cmake_runner_settings['cmake-generator'] == 'Ninja':
		definitions = " -G\"Ninja\" -DCMAKE_GENERATOR=Ninja "
	elif cmake_runner_settings['cmake-generator'] == 'MinGW Makefiles':
		definitions = " -G\"MinGW Makefiles\" "
	else:
		print("-- Error Cmake Generator not specified")
		sys.exit(0)
	definitions += "-DCMAKE_BUILD_TYPE=" + variant.buildType + " "
	for i in variant.settings:
		d = "-D" + i + "=" + variant.settings[i] + " "
		definitions += d
	return definitions

def build_file_exists(build_dir):
	build_file = ""
	cmake_runner_settings = get_cmake_runner_settings()
	if cmake_runner_settings['cmake-generator'] == 'Ninja':
		build_file = os.path.isfile(os.path.join(build_dir, "build.ninja"))
	elif cmake_runner_settings['cmake-generator'] == 'MinGW Makefiles':
		build_file = os.path.isfile(os.path.join(build_dir, "Makefile"))
	else:
		print("-- Error Cmake Generator not specified")
		sys.exit(0)
	if os.path.isfile(build_file):
		return True
	return False

def execute_configure_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	create_build_dir(build_dir)
	definitions = get_cmake_definitions(variant)
	cmd = "cmake -S \"" + workspace + "\" -B \"" + build_dir + "\" " + definitions
	print("Running command: " + cmd)
	os.system(cmd)

def execute_build_command(workspace, variant):
	cmake_runner_settings = get_cmake_runner_settings()
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	if build_file_exists(build_dir):
		execute_configure_command(workspace, variant)
	cmd = "cmake --build " + build_dir
	print("Running command: " + cmd)
	os.system(cmd)

def execute_flash_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	cmd = "cmake --build " + build_dir + " --target flash_mcu"
	print("Running command: " + cmd)
	os.system(cmd)

def execute_rebuild_command(workspace, variant):
	os.chdir(workspace)
	build_dir = "build-" + variant.variantName
	delete_build_dir(build_dir)
	execute_configure_command(workspace, variant)
	execute_build_command(workspace, variant)


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