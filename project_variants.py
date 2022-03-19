import yaml
import sys
import os

class ProjectVariant:
	def __init__(self, data) -> None:
		self.raw_dict = data
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


def read_project_variants():
	CURRENT_SCRIPT_DIR = (os.path.dirname(os.path.abspath(__file__)))
	file = os.path.join(CURRENT_SCRIPT_DIR, "project-variants.yaml")
	f = open(file, "r")
	yamlfile = yaml.load(f, Loader=yaml.FullLoader)
	f.close()
	variants = list()
	for i in yamlfile:
		v = ProjectVariant(yamlfile[i])
		variants.append(v)
	return variants


if __name__ == '__main__':
	x = read_project_variants()
	print(x)
