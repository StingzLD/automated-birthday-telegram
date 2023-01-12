import smtplib

EMAIL_SENDER = "stingzld.test.email@gmail.com"
EMAIL_RECIPIENT = "stingzld.other.test.email@gmail.com"
PASSWORD = "aaeddmspdtbyixxw"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL_SENDER, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL_SENDER,
                        to_addrs=EMAIL_RECIPIENT,
                        msg="Subject:Hello World!\n\n"
                            "This is the body of the email!")
