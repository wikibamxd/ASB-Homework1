"""
Execução:
python3 my_script.py «arg1» «arg2»
Estrutura:
    1. Obter History.xml
    2. Parse no History.xml (WebEnv)
    3. Obter file de sequencias
    4. Output (FASTA e STDOUT)
"""
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

#command line arguments
#args.db
parser = argparse.ArgumentParser(description="Process files")
parser.add_argument("-db", "--database", required=True, help="Database to use")
parser.add_argument("-q", "--query", required=True, help="Search query")
parser.add_argument("-o", "--output", required=True, help="Output directory")
args = parser.parse_args()

def esearch(db, query):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\?db={argparse.db}\&term={argparse.query}&usehistory=y"
    with urllib.request.urlopen(url) as response:
      data = response.read()
    return data

def esearchParse(esearch):
    root = ET.fromstring("WebEnv")
    query
tree = ET.parse('country_data.xml')
root = tree.getroot()