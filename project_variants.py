import yaml
import sys
import os

class Variant:
	def __init__(self, name, data) -> None:
		self.variantName = ""
		self.shortName = ""
		self.longName = ""
		self.buildType = "Debug"
		self.description = ""
		self.settings = None
		self.set_name(name)
		self.load(data)

	def load(self, data):
		try:
			self.shortName = data['shortName']
			self.longName = data['longName']
			self.description = data['description']
			self.settings = data['settings']
			self.buildType = data['buildType']
		except KeyError:
			pass
	
	def set_name(self, name):
		self.variantName = name
	
	def to_dictionary(self):
		data = dict()
		data['shortName'] = self.shortName
		data['longName'] = self.longName
		data['buildType'] = self.buildType
		data['description'] = self.description
		if self.settings:
			data['settings'] = self.settings
		return {self.variantName: data}



def __read_project_yaml_file(workspace):
	file = os.path.join(workspace, "project-variants.yaml")
	f = open(file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	return yamlfile

def get_project_variants(workspace):
	yamlfile = __read_project_yaml_file(workspace)
	variants = list()
	for i in yamlfile:
		v = Variant(i, yamlfile[i])
		variants.append(v)
	return variants

def get_selected_project_variant(workspace):
	file = os.path.join(workspace, "selected_variant.yaml")
	f = open(file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	variantName = list(yamlfile.keys())[0]
	v = Variant(variantName, yamlfile[variantName])
	return v

def save_current_variant(variant, workspace):
	file = os.path.join(workspace, "selected_variant.yaml")
	f = open(file, "w")
	yaml.dump(variant.to_dictionary(), f)
	f.close()


if __name__ == '__main__':
	x = get_selected_project_variant(".")
	print(x)