import argparse
import requests

#command line arguments
parser = argparse.ArgumentParser(description="im not sure yet")
parser.add_argument("-db", required=True, type=str, help="Database to use", dest="db")
parser.add_argument("-query", required=True, type=str, help="Search query", dest="query")
args = parser.parse_args()

##SEARCH FUNCTION
def search(db, query):
	payload = {"db": db, "term": query, "usehistory": "y"}
	esearch = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=payload) #calls the entrez API
	print(esearch.text) #prints out the result of the esearch

	##section to parse the resulting xml to extract the query key and webenv when i figure it out

	#efetch = requests.get("url pending")

	##section to parse results to get the sequences

	return(esearch.text)

#def write():
	##heavily pending
	#darrrgggggggg (heartbroken emoji x3)	
search_result = search(args.db, args.query)
print(search_result)