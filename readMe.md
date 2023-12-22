
## I Introduction
This script takes in either a single query string or a plain text file containing a lists of query strings(each separated by "\n") and then makes api calls to Crossref API. It retrieves the DOIs for the queried items. With the optional argument "--output", it retrieves and saves the metadata in "bibtex" files.

Either the argument "--query" or "--file" is required. The argument "--output" is optional and --sleep is optional.

If only one query string is provided(Argument: --query), the output file name will be the output file name supplied by the user followed by "_0.bibtex".   
If a query_list(txt file) is provided, the output files will be named "[user_provided_final_name]_0.bibtex", "[user_provided_final_name].bibtex", etc.

The interval between api calls is set to 2 seconds by default. You can put a number after the "--sleep" argument. The unit is second.

Specific and accurate query strings are essentail to ensure correct DOI retrieval. This program is ideal for migrating exiting bibliographies in text format into a digital manager like Zotero or Endnote. It is also ideal for quickly generating the reference metadata for one or two items.


## II USAGE:   

`python3 api_calls.py --query queryString --sleep n --output output_file_name`  

OR  

`python3 api_calls.py --file query_list.txt --sleep n --output output_file_name`  

