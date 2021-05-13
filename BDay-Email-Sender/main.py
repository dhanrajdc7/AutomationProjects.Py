import smtplib
import datetime as dt
import pandas

MY_MAIL = "abc@gmail.com"
MY_PASS = "Abc@3"

# Check Today = BDay
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read Bday Data
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    bday_person = birthdays_dict[today_tuple]
    with open("quotes.txt") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASS)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=bday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n {contents}")
