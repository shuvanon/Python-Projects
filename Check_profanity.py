import urllib
def read_text():
    text = open("E:\Python Projects\short projects\Test.txt")
    contents_of_file = text.read()
    #print (contents_of_file)
    text.close()
    check_profanity (contents_of_file)

def check_profanity (text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
