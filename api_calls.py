"""
USAGE:   

python3 api_calls.py --query queryString --sleep n --output output_file_name

                    or 

python3 api_calls.py --file query_list.txt --sleep n --output output_file_name


Description:

This script takes in either a single query string or a plain text file containing a lists of query strings(each separated by "\n") and then makes api calls to Crossref API. It retrieves the DOIs for the queried items. With the optional argument "--output", it retrieves and saves the metadata in "bibtex" files.

Either the argument "--query" or "--file" is required. The argument "--output" is optional and --sleep is optional.

If only one query string is provided(Argument: --query), the output file name will be the output file name supplied by the user followed by "_0.bibtex". 
If a query_list(txt file) is provided, the output files will be named "[user_provided_final_name]_0.bibtex", "[user_provided_final_name].bibtex", etc.

The interval between api calls is set to 2 seconds by default. You can put a number after the "--sleep" argument. The unit is second.

Specific and accurate query strings are essentail to ensure correct DOI retrieval. This program is ideal for migrating exiting bibliographies in text format into a digital manager like Zotero or Endnote. It is also ideal for quickly generating the reference metadata for one or two items.


"""

from crossref_api_functions import api_call_doi, api_call_bibtex, write_bibtex
import time
import argparse

parser = argparse.ArgumentParser(description="api calls to Crossref API")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("--query", 
                   metavar= "query_string", 
                   type=str, 
                   help="query list")

group.add_argument("--file", 
                   metavar= "query_txt_file", 
                   type=str, 
                   help="query list file")

parser.add_argument("--sleep", type=int, 
                    default=2, 
                    help="sleep time between api calls")

parser.add_argument("-o", "--output", 
                    type=str, 
                    help="output file name")

args = parser.parse_args()


SLEEP_TIME = args.sleep

if __name__ == "__main__":

    start_time = time.time()

    if args.query is not None:
        query_s_list = [args.query]
    
    if args.file is not None:
        with open(args.file, "r") as fh:
            query_s_list = fh.readlines()

    print("-----------------program starts-----------------")
    print("query list examples:", query_s_list[:3])

    doi_list=[]
    for item in query_s_list:
        doi_list.append(api_call_doi(item))
        time.sleep(SLEEP_TIME)

    print("doi list")
    for i in doi_list:
        print(i[1])

    if args.output is not None:
        n = 0
        for doi_item in doi_list:
            write_bibtex(api_call_bibtex(doi_item[1]), f"{args.output}_{n}.bibtex")
            time.sleep(SLEEP_TIME)
            n += 1


    end_time = time.time()
    print(f"---program ends--it takes{end_time - start_time}seconds---")