#!/usr/bin/python

import io
import csv
import sys
import re



def main():
    for domain in get_domains_from_refs():
        print(domain)



def get_domains_from_refs():
    
    REGEX = re.compile(r'(?:https?:\/\/)([^(?:\/|<|\]|,| |\||\})]+)')
    
    for ref in read_refs_from_tsv('../../refsdomains/mwrefs-enwiki-20150515.tsv'):
        
        match = re.search(REGEX, ref)
        
        if match:
            yield match.group(0)


       
def read_refs_from_tsv(tsv_file_name):
    
    with io.open(tsv_file_name, 'r', encoding='utf8') as tsv_file:
    
        for line in tsv_file:
            
            try:
                #a, b, c, d, e, refs, g = line.strip().split("\t")
                a, b, c, refs = line.strip().split("\t")
            
                refs.replace("\\t", "\t").replace("\\n", "\n")

                yield refs
            
            except ValueError:
                print(line)



if __name__ == '__main__':

    main()