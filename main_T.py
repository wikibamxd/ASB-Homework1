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
#Parsing function
def XMLParse(esearch):
	"""
	Should get the XML output from the search function and return the query key and webenv
	It is not working currently because the query_key and WebEnv are not being recognized for some reason
	"""
	tree = ET.fromstring(esearch)	
	query_key = tree.find("QueryKey").text
	WebEnv = tree.find("WebEnv").text
	return(query_key, WebEnv)

def efetch(db, query_key, WebEnv):
	"""
	SHould get the query key and webenv from the parsing fucntion and return the fasta result from the efetch
	"""
	payload2 = {"db" : db, "term": query_key, "term" : WebEnv, "usehistory" : "y", "rettype" : "fasta"}
	efetch = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=payload2)

	return(efetch.text)

print(efetch)

