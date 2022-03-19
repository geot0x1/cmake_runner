import yaml
import sys
import os

class Variant:
	def __init__(self, data, varname) -> None:
		self.raw_dict = data
		self.variantName = varname
		self.shortName = "Untitled"
		self.longName = "Untitled"
		self.description = "No description given"
		self.settings = None
		self.__parse_dict()

	def __parse_dict(self):
		data = self.raw_dict
		try:
			self.shortName = data['shortName']
			self.longName = data['longName']
			self.buildType = data['buildType']
			self.description = data['description']
			self.settings = data['settings']
		except KeyError:
			pass


def read_project_variants(workspace):
	file = os.path.join(workspace, "project-variants.yaml")
	f = open(file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	variants = list()
	for i in yamlfile:
		v = Variant(yamlfile[i], i)
		variants.append(v)
	return variants

def current_project_variant(workspace):
	file = os.path.join(workspace, ".cur_proj_variant.yaml")
	f = open(file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	return yamlfile

def save_current_variant(variant, workspace):
	file = os.path.join(workspace, ".cur_proj_variant.yaml")
	f = open(file, "w")
	yaml.dump(variant, f)
	f.close()


if __name__ == '__main__':
	x = read_project_variants()
	print(x)
