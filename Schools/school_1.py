# Purpose of this file
# 1. Create a Dictionary with all attributes of schools
# 2. Create an object for KML with school details

import os
import csv

from Configuration.config_read import _def_config as config

O_def_config = config()
print O_def_config.getClassificationList()

for key in O_def_config.getClassificationList():
	print key, "\t@@\t", O_def_config.getConfigList(key)
	print key, "\t>>\t", O_def_config.getConfigDict(key)

print O_def_config.getConfig('property type (apt/house)')