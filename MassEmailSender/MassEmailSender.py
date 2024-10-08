import click
import smtplib
from email.message import EmailMessage
import re
import time

@click.command()
@click.argument('send_from')
@click.argument('to_txt')
@click.argument('subject')
@click.argument('email_txt')
def send(send_from, to_txt, subject, email_txt):
    sendInternal(send_from, to_txt, subject, email_txt)
    
def sendInternal(sendFrom, toTxt, subject, emailTxt):
    print("Starting...")
    # TODO check if it's HTML or not
    with open(emailTxt) as file:
        msg = EmailMessage()
        msg.set_content(file.read())
    
    with open(sendFrom) as file:
        i = 0
        email = ""
        pwd = ""
        server = "smtp.gmail.com"
        for line in file:
            if line.strip() == "":
                continue
            if i == 0:
                email = line.strip()
            elif i == 1:
                pwd = line.strip()
            elif i == 2:
                server = line.strip()
            else:
                break
            i += 1

    msg['From'] = email
    with open(subject) as file:
        subj = file.read()
    msg['Subject'] = subj
    print("Subject: "+subj)
    s = smtplib.SMTP_SSL(server)
    s.login(email, pwd)
    s.connect
    with open(toTxt) as file:
        for line in file:
            address = line.strip()
            if line == "":
                continue
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', address):
                if 'To' in msg:
                    msg.replace_header('To', address)
                else:
                    msg['To'] = address
                s.send_message(msg)
                print("Sent to "+address)
    s.quit()

print("Hello world")
if __name__ == '__main__':
    try:
        sendInternal("SendFrom.txt", "SendTo.txt", "SubjectText.txt", "EmailText.txt")
    except:
        print("Something went wrong...")
    print("Sent!")