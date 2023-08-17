# -*- coding: utf-8 -*-
"""
Code to steer ARGUS

Created on Mon Jun  8 16:41:04 2020

@author: JDO
"""

# Modules
import os
import sys
import time

# get path to directory
script_dir = os.path.dirname(__file__)


class argus_settings:   
	os.chdir(script_dir)	# change working directory to project folder
	filepath = sys.argv[1] 	# file path for list containing URLs
		
	# settings for ARGUS spider
	delimiter = ";"    
	encoding = "utf-8"
	index_col = "ID"		# column with IDs
	url_col = "URL"		# column with URLs
	lang = "None"		# language
	n_cores = 8		# number of cores
	limit = 10		# scraping limit
	log_level = "WARNING"
	prefer_short_urls = "off"
	pdfscrape = "off"

# Execute scraping
if __name__ == "__main__":
	os.startfile(script_dir + r"\bin\start_server.bat")		# start scrapyd server
	time.sleep(2)
	# Start crawling
	from bin import start_crawl_steering
	start_crawl_steering.start_crawl()