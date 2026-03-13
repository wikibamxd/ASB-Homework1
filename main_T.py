import argparse
import requests
import xml.etree.ElementTree as ET

#command line arguments
parser = argparse.ArgumentParser(description="im not sure yet")
parser.add_argument("-db", required=True, type=str, help="Database to use", dest="db")
parser.add_argument("-query", required=True, type=str, help="Search query", dest="query")
args = parser.parse_args()



##SEARCH FUNCTION
def search(db, query):
	payload = {"db": db, "term": query, "usehistory": "y"}
	esearch = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=payload) #calls the entrez API and prints the result

	return(esearch.text)

def XMLParse(esearch):
	tree = ET.fromstring(esearch)	
	query_key = tree.find("QueryKey").text
	WebEnv = tree.find("WebEnv").text
	return(query_key, WebEnv)

print(query_key)
print(WebEnv)




	#efetch = requests.get("url pending")

	##section to parse results to get the sequences





#def write():
	##heavily pending
	#darrrgggggggg (heartbroken emoji x3)	
search_result = search(args.db, args.query)
print(search_result)