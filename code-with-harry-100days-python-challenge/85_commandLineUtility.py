import argparse
parser = argparse.ArgumentParser()

#add command line arguements
parser.add_argument("arg1", help="Description of arguement 1")
parser.add_argument("arg2", help="Description of arguement 2")

#parse the arguements
args = parser.parse_args()

#use the arguements to your code
print(args.arg1)
print(args.arg2)