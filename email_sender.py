import yagmail
import datetime
import os
from datetime import date

def send_email():
    # Defining the filename based on the date
    #date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    #filename = f"~/TodoByEmail/todos/tasks_{date_str}.txt"
    
    date_str = os.path.join(os.path.expanduser("~"),"TodoByEmail","todos")
    filename = os.path.join(date_str, f"tasks_{date.today()}.txt")

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"No notes for {date_str}. Exiting...")
        return

    # Setup the email client
    yag = yagmail.SMTP("brennsmailbox@gmail.com")  # Assumes you've stored the credentials for this email in keyring

    # Send the email
    with open(filename, 'r') as f:
        contents = f.read()
        yag.send(
            to="nievab@wwu.edu",
            subject=f"{date.today()} Notes",
            contents=contents,
            attachments=filename
        )
    
    print(f"Sent notes for {date_str} via email!")

if __name__ == "__main__":
    send_email()

