"""
Execução:
python3 my_script.py «arg1» «arg2»
Estrutura:


Output (FASTA e STDOUT)
"""
import argparse

#command line arguments
parser = argparse.ArgumentParser(description="im not sure yet")
parser.add_argument("-db", required=True, help="Database to use")
parser.add_argument("-query", required=True, help="Search query")
parser.add_argument("-out1", required=True, help="Output directory")
args = parser.parse_args()