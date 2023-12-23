## I Introduction
This python script `api_calls.py` takes in either a single query string or a plain text file containing a list of query strings(each separated by "\n") and then makes api calls to Crossref API. It retrieves the DOIs for the queried items. With the optional argument "--output", it retrieves and saves the items' metadata in "bibtex" files.

The argument `--query` (corresponds to a query string) or `--file` (a plain txt file) is required. The arguments `--output`(output file base name, i.e. without the extension "bibtex") and `--sleep`(time intervals between api calls) are optional.

If only one query string is provided(with the argument `--query`) and the output file base name is given(with the `--output` argument), the output file name will be "[user_provided_file_base_name]_0.bibtex".   

If a query_list(with the argument `--file`) is provided and the output file base name is given(with the `--output` argument), the output files will be named "[user_provided_file_base_name]_0.bibtex", "[user_provided_file_base_name]_1.bibtex", etc.

The interval between api calls is set to 2 seconds by default. It can changed it with the argument `--sleep`. The unit is second.

Specific and accurate query strings are essentail to ensure correct DOI retrieval(and correct meta data retrievals as well). This program is ideal for migrating exiting bibliographies in text format into a digital manager like Zotero or Endnote. It is also ideal for quickly generating the reference metadata for one or two items.


## II USAGE:   

`python api_calls.py --query queryString --sleep n --output output_file_base_name`  

OR  

`python api_calls.py --file query_list.txt --sleep n --output output_file__base_name`  

