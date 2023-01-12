import pandas
import smtplib
import datetime as dt


def send_telegram(email, message):
    email_sender = "stingzld.test.email@gmail.com"
    password = "aaeddmspdtbyixxw"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email_sender, password=password)
        connection.sendmail(from_addr=email_sender,
                            to_addrs=email,
                            msg="Subject:Happy Birthday!\n\n"
                                f"{message}")


def create_letter(name):
    with open("letter.txt") as file:
        contents = file.read()
    return contents.replace("[NAME]", name)


today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():
    birthday = (row.month, row.day)
    if birthday == today:
        letter = create_letter(row["name"])
        send_telegram(row.email, letter)
