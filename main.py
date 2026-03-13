import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

#command line arguments
def args_parse():
    """
    Argument Parsing Function

    Transforms user inputs into usable variables in the code
    Takes 'database', 'query' and 'output' inputs from the user
    Outputs the inputs for the code to utilize
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
    parameters = urllib.parse.urlencode({
        "db": db,
        "term": query,
        "usehistory": "y",
        "retmode": "xml"
    })

    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{parameters}"
    with urllib.request.urlopen(url) as url1:
        return url1.read()



def esearchParse(esearch):
    """
    Parsing Function

    Parses the XML file from the eSearch function
    Receives the XML file as input
    Outputs the information needed to get the FASTA files
    """
    root = ET.fromstring(esearch)
    query_Key = root.find("QueryKey").text
    WebEnv = root.find("WebEnv").text
    return WebEnv, query_Key
    

def efetch(db, query_key, WebEnv):
    """
    Fetch sequences in FASTA format from NCBI using the Entrez API

    Args:
        db        : NCBI database name.
        web_env   : webEnv string from esearch.
        query_key : querykey string from esearch.

    Returns:
        str: FASTA-formatted sequences as a string.
    """
    parameters = urllib.parse.urlencode({
        "db" : db,
        "query_key" : query_key,
        "WebEnv" : WebEnv,
        "rettype" : "fasta",
        "retmode" : "text",
        })
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{parameters}"
    with urllib.request.urlopen(url) as url2:
        return url2.read().decode("utf-8")
        
def main():
    """
    Main function: orchestrates argument parsing, esearch, parsing, efetch, and output.
    """
    args = args_parse()

    xml = esearch(args.database, args.query)
    webenv, query_key = esearchParse(xml)
    fasta = efetch(args.database, query_key, webenv)
    
    #Creates the FASTA file
    with open(f"{args.output}.fasta", "w") as f:
        f.write(fasta)

    print(fasta)
    

if __name__ == "__main__":
    main()