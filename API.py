from colors import *


print('''
%s1%s %sCensys API key%s
%s2%s %sCensys Secret API key%s
%s3%s %sAlienvault API key%s
%s4%s %sVirustotal API key%s
%s5%s %sWhatCMS API key%s''' % (
    red, end, yellow, end, red, end, yellow, end, red, end, yellow, end, red, end, yellow, end, red, end, yellow, end,))

value = input('''%sEnter Value : %s''' % (green, end))


def switcher_demo(value):
    switcher = {
        1: censys(),
        2: censyss(),
        3: alienvault(),
        4: virustotal(),
        5: whatcms()
    }
    print(switcher.get(value, "Invalid Input"))


# Taking input

def censys():
    while True:
        censysapi = input('''%sEnter censys API key : %s''' % (green, end))
        if not censysapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[140] = f"apikey ={censysapi}\n"
            break


def censyss():
    while True:
        censyssapi = input('''%sEnter censys secret API key : %s''' % (green, end))
        if not censyssapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[141] = f"secret ={censyssapi}\n"
            break


def alienvault():
    while True:
        alienvaultapi = input('''%sEnter alienvault API key : %s''' % (green, end))
        if not alienvaultapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[120] = f"apikey ={alienvaultapi}\n"
            break


def virustotal():
    while True:
        virustotalapi = input('''%sEnter virustotal API key : %s''' % (green, end))
        if not virustotalapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            a_file = open("config.ini", "r")
            list_of_lines = a_file.readlines()
            list_of_lines[262] = f"apikey ={virustotalapi}\n"
            break


def whatcms():
    while True:
        whatcmsapi = input('''%sEnter whatcms API key : %s''' % (green, end))
        if not whatcmsapi:
            print('''%sCan not be empty API%s''' % (bad, end))
        else:
            break
