import yagmail
import datetime
import os

def send_email():
    # Defining the filename based on the date
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"/home/bniev/scripts/todos/tasks_{date_str}.txt"
    
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
            subject=f"{date_str} Notes",
            contents=contents,
            attachments=filename
        )
    
    print(f"Sent notes for {date_str} via email!")

if __name__ == "__main__":
    send_email()

