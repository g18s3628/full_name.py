#Request user for their full name 
full_name = input("Please input your full name:")

#If the length of characters is zero then print an error message 
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
#If the length of characters is less than 4 then print an error message 
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you hav entered your name and surname.")
#If the length of characters is more than 25 then print an error message 
elif len(full_name) > 25: 
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
#Else print thank you for entering your name
else: 
    print("Thank you for entering your name.")
