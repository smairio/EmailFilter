import sys


def main():
	emails=open(sys.argv[1]).read().splitlines()
	for email in emails:
		append(email)



def split(email):
	domain= email.split("@")[1].split('.')[0]
	return domain

def append(email):
	domain=split(email)
	if domain in ['gmail','yahoo','mail','orange','aol']:
		with open(domain+'.txt',"a") as f:
			f.write("%s\n" % email)
	elif domain in ['hotmail','live','outlook'] :
		with open('outlook.txt',"a") as f:
			f.write("%s\n" % email)
	else:
		with open('others.txt',"a") as f:
			f.write("%s\n" % email)
main()

