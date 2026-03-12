import argparse
import requests

#command line arguments
parser = argparse.ArgumentParser(description="im not sure yet")
parser.add_argument("-db", required=True, type=str, help="Database to use")
parser.add_argument("-query", required=True, type=str, help="Search query")
args = parser.parse_args()

##SEARCH FUNCTION
def search(db, query, ):
	esearch = requests.get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\?db\="{db}"\&term\="{query}"\&usehistory\=y") #placeholder cuz im not sure it works
	print(response.text)
	##section to parse the resulting xml to extract the query key and webenv when i figure it out

	#efetch = requests.get("url pending")

	##section to parse results to get the sequences

	return()

#def write():
	##heavily pending
	#darrrgggggggg (heartbroken emoji x3)	