from datetime import datetime

now = datetime.now()
birth_str = input("When where you born? Please enter date and time (format DD-MM-YYYY HH:MM:SS): \n-")
birth_validation = False

while birth_validation == False:
    birth_validation = True
    try:
        birth_datetime = datetime.strptime(birth_str, '%d-%m-%Y %H:%M:%S')
    except:
        print("Ups... Looks like you entered incorrect data. Please try again.")
        birth_str = input("When where you born? Please enter date and time (format DD-MM-YYYY HH:MM:SS): \n-")
        birth_validation = False

time_between = int((now-birth_datetime).total_seconds())
print(f"You live for {time_between} seconds or \n{int(time_between/60)} minutes \n{int(time_between/60/60)} hours \n{int(time_between/60/60/24)} days")



