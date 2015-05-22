#!/bin/bash


# extract the domains from the added references

python3 get_domains.py > domains.txt
echo "Extracted domains from the references dataset"


# sort the domains by name

sort -o sorted_domains.txt domains.txt
echo "Sorted domains"


# collapse and count individual domains

python3 reduce_domains.py > domain_list.txt
echo "Reduced and counted individual domains"


# sort the list by decreasing number of occurrences of domains

sort -n -r -o sorted_domain_list.txt domain_list.txt
echo "Sorted domains by number of occurrences"
