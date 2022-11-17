# importing module
import requests
import sys
import os
from pathlib import Path

# function for scanning subdomains


def domain_scanner(domain_name, sub_domnames):
    print('----URL after scanning subdomains---- by :- Niraj adhikari' '\n')

    # loop for getting URL's
    for subdomain in sub_domnames:

        # making url by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"

        # using try catch block to avoid crash of the
        # program
        try:
            # sending get request to the url
            requests.get(url)

            # if after putting subdomain one by one url
            # is valid then printing the url
            print(f'[+] {url}')

            # if url is invalid then pass it
        except requests.ConnectionError:
            pass


# main function
if __name__ == '__main__':

    # inputting the domain name
    dom_name = input("Enter the Domain Name:  ")

    # opening the subdomain text file
    with open('sub.txt', 'r') as file:

        # reading the file
        name = file.read()

        # using spilitlines() function storing the list
        # of splitted strings
        sub_dom = name.splitlines()

    # calling the function for scanning the subdomains
    # and getting the url
 # * create a file and check the file is exit or not

if not os.path.exists('enu_domain_list.txt'):
    with open("enu_domain_list.txt", 'x')as sys.stdout:
        print(domain_scanner(dom_name, sub_dom))
# * if exits doesn't create another file append on it (append = write the text on the file with another line )
else:
    with open("enu_domain_list.txt", 'a') as sys.stdout:
        print(domain_scanner(dom_name, sub_dom))
