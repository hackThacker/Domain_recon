# importing module
import requests
import sys
import os

start = time.time()
# function for scanning subdomains
def domain_scanner(domain_name, sub_domnames):
    print('\n''URL after scanning subdomains- by :-Niraj adhikari' '\n','Domain Name :', dom_name,'\n''\n''Subdomain')

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

     # inputting the files number
print("1 == sub.txt\n2 == subdomain.txt")
choice = input(" Enter the number :  ")
if choice == "1":
    with open('sub.txt', 'r') as sys.stdout:
        # * create a file and check the file is exit or not
        if not os.path.exists('enurmationdomainlist.txt'):
            with open("enurmationdomainlist.txt", 'x')as sys.stdout:
                print(print(domain_scanner(dom_name, sub_dom)))
        elif os.path.exists('enurmationdomainlist.txt'):
            with open("enurmationdomainlist.txt", 'a') as sys.stdout:
                print(domain_scanner(dom_name, sub_dom))
                '\n'
elif choice == '2':
    with open('subdomain.txt', 'r') as sys.stdout:
        # * create a file and check the file is exit or not
        if not os.path.exists('enurmationdomainlist.txt'):
            with open("enurmationdomainlist.txt", 'x')as sys.stdout:
                print(domain_scanner(dom_name, sub_dom))
        elif os.path.exists('enurmationdomainlist.txt'):
            with open("enurmationdomainlist.txt", 'a') as sys.stdout:
                print(domain_scanner(dom_name, sub_dom))
                '\n'
# * if exits doesn't create another file append on it (append = write the text on the file with another line )
else:
    print("""
    [1] small list  208 bytes  Less Time
    [2] large.txt   3.14 MB    More Time
    [@] Please chose 1 and 2 only Thank you ..<
                """)
