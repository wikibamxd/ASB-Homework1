"""
Execução:
python3 my_script.py «arg1» «arg2»
Estrutura:
    1. Obter History.xml
    2. Parse no History.xml (WebEnv,Key)
    3. Obter file de sequencias
    4. Output (FASTA e STDOUT)
"""
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import sys

#command line arguments
def args():
    """
    """
    parser = argparse.ArgumentParser(description="Process files")
    parser.add_argument("-db", "--database", required=True, help="Database to use")
    parser.add_argument("-q", "--query", required=True, help="Search query")
    parser.add_argument("-o", "--output", required=True, help="Output directory")
    return parser.parse_args()



def esearch(db, query):
    """
    eSearch Function
    
    Searches the Database for the Query that it gets as an input
    Receives the Database and Query that the user wants to utilize
    Outputs the Result of the Search
    """
    parameters = {"db": db, 
                  "term": query, 
                  "usehistory": "y"}
    esearch = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", parameters) #calls the entrez API
    print(esearch.text) #prints out the result of the esearch
    return esearch.text



def esearchParse(esearch):
    """
    Parsing Function

    Parses the XML file from the eSearch function
    Receives the XML file as input
    Outputs the information needed to get the FASTA files
    """
    root = ET.fromstring("WebEnv")
    query
tree = ET.parse('country_data.xml')
root = tree.getroot()

def efetch(db, query_key, WebEnv):
    """
    """
    parameters = urllib.parse.urlencode({
        "db" : db,
        "query_key" : query_key,
        "WebEnv" : WebEnv,
        ""
        })
