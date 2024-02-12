def main():
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    month , date , year = month_value(month_list)
    print(f"{year}-{month:02}-{date:02}")




def month_value(months):
    while True:
        user_input = input("Date : ")
        try:
            month , day , year = user_input.split("/")
            if 1 <= int(month) <= 12 and 1<= int(day) <= 31 :
                return int(month), int(day) , int(year)
            else:
                pass


        except:
            try:
                date_data = user_input.split()
                if "," in date_data[1]:
                    day = date_data[1].split(",")
                else:
                    pass
                if date_data[0] in months and 1 <= int(day[0]) <= 31:

                    return int(months.index(date_data[0])+1) , int(day[0]) , int(date_data[-1])
                else:
                    pass
            except:
                pass

main()
