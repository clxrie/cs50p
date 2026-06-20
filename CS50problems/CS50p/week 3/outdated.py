months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    date = input("Date: ")

    try:
        if "/" in date:
            month, day, year = date.split("/")
            if int(month) < 1 or int(month) >12:
                raise ValueError
            if int(day) < 1 or int(day) > 31:
                raise ValueError
            print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
            break
            
        
        else:
            parts = date.split(" ")
            month_name = parts[0]
            if not parts[1].endswith(","):
                raise ValueError
            day = parts[1].strip(",")
            year = parts[2]

            if month_name not in months:
                raise ValueError
            month = months.index(month_name) + 1

            if int(day) < 1 or int(day) > 31:
                raise ValueError
            print(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
            break
    
    except ValueError:
        pass
 