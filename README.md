# Homework 1
A repository for the first Homework of "Análise e Sequencias Biologicas"

---
## Program usage
```
python main.py -db «database» -q «query» -o «output»
```
### OR
```
python main.py --database «database» --query «query» --output «output»
```
## Program Description 
A non-interactive Python script to retrive sequences that takes user input database and search query. It uses the history EntrezAPI's feature and the output is in FASTA format and written to STDOUT.

## Program Objectives
Facilitate the process of NCBI's api handling

## Requirements
Python Standard Libraries

## Structure:
	1. Input Argument Parsing
	2. Esearch (NCBI database search)
	3. Esearch output Parsing (XML file)
	4. Efetch (Gets the corresponding sequences)
	5. Main function (Coordenates everything)

