
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
	if(re.fullmatch(regex, email)):
		print("Valid Email")
	else:
		print("Invalid Email")


email = "xyz@gmail.com"
check(email)


