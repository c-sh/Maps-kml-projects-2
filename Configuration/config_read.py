# Purpose of this file
# 1. Create a Dictionary with all configs
# 2. API to query the config from a module

import os
import csv

class _def_config:
	def __init__(self, config_csv = "./config.csv"):
		#dictionary of all configurations
		self.__top_level_config = {}
		self.__top_level_config = self.__read_from_config_file( config_csv )
		print self.__top_level_config
		
		#school config
		
		#real estate filter

	def __read_from_config_file(self, in_csv):
		with open(in_csv, "rb") as cfg_file:
			rd_file = csv.DictReader(cfg_file)
			classifications_dict = {}

			for loop_dict in rd_file:
				#python built in function 'any' - check if all values are 0, and discard those dictionaries (they are empty rows in CSV
				if any(loop_dict.values()):
					temp_dict = {loop_dict["Configuration"]: loop_dict["Value"]}
					if loop_dict["Classification"] in classifications_dict.keys():
						classifications_dict[loop_dict["Classification"]].update(temp_dict)
					else:
						classifications_dict[loop_dict["Classification"]] = temp_dict
		
		return classifications_dict

	def getClassificationList(self):
		return self.__top_level_config.keys()

	def getConfigList(self, classification):
		return self.__top_level_config[classification].keys()

O_def_config = _def_config()
# print O_def_config.getClassificationList()

# for key in O_def_config.getClassificationList():
	# print O_def_config.getConfigList(key)