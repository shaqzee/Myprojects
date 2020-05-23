import time

def get_userId():
	Email = input('Enter Email address: ')
	Email_Id = Email.split('@')
	user_Id = Email_Id[0]
	print(f"Your Email ID is {user_Id}")
	time.sleep(7)
get_userId()
