#!/usr/bin/python

import io
import sys



def main():
    
    reduce_domains('sorted_domains.txt')



def reduce_domains(file_name):
    
    with io.open(file_name, 'r', encoding='utf8') as file:
    
        count = 0
        
        previous_domain=''
        
        for domain in file:
            
            if (domain == previous_domain):
                count += 1
            else:
                # print the count and domain, remove trailing \n
                
                print('{0}\t{1}'.format(count, previous_domain[:-1]))
                
                previous_domain = domain
                count = 1



if __name__ == '__main__':

    main()