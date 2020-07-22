import argparse
import codecs
import os
from datetime import datetime, timedelta

def get_keywords (name_file):
	list_keywords = []
	with codecs.open (name_file, encoding='utf-8') as infile:
		for line in infile:
			list_keywords.append(line.strip())
	if len(list_keywords) == 0:
		print ('Error in keywords file.')
		exit()
	return (list_keywords)

def convert_date (date_str):
	try:
		date_obj = datetime.strptime(date_str, '%Y-%m-%d')
		return (date_obj.date())
	except:
		print ('Date is not well formated.')
		exit()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Twitter Crawler')
	parser.add_argument('--keywords', metavar='path', required=True, help='File with keywords')
	parser.add_argument('--language', metavar='path', required=True, default='pt', help='Language')
	parser.add_argument('--begin', metavar='path', required=True, help='Begin Date')
	parser.add_argument('--end', metavar='path', required=True, help='End Date')
	args = parser.parse_args()

	file_keywords = args.keywords
	keywords_set = get_keywords (file_keywords)

	language = args.language

	begin_date = args.begin
	begin_date_obj = convert_date(begin_date)

	end_date = args.end
	end_date_obj = convert_date(end_date)
	
	delta = end_date_obj - begin_date_obj

	for key in keywords_set:
		for d in range(delta.days + 1):
			day = begin_date_obj + timedelta(days=d)
			nextday = day + timedelta(1)
			comand = "twitterscraper \"" + key + "\" --lang " + language + " -ed " + str(nextday) + " -bd " + str(day) + " --output=" + key + "-" + str(day) + ".json"
			print (comand)
			os.system(comand)
