import sys

salutation = "Human"

if len(sys.argv)>1 and sys.argv[1]:
    salutation = sys.argv[1]

print("Hello, %s!" % salutation)