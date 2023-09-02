import imaplib
import email

user = "rajeshadhiban2005@gmail.com"
password = "zswwbvqdccmewtrz" #App password
imap_url = 'imap.gmail.com'
# Function to get email content part i.e its body part
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
# Function to search for a key value pair
def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data
# this is done to make SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
# calling function to check for email under this label
con.select('Inbox')
# Search for the most recent email from the sender
sender_email = "dianoman12@gmail.com"
messages = search('FROM', sender_email, con)[0].split()
if messages:
    latest_message = messages[-1]  # Get the ID of the latest email
    # Fetch the latest email
    typ, msg_data = con.fetch(latest_message, '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    # Extracting required information
    sender = msg["From"]
    recipient = msg["To"]
    date = msg["Date"]
    subject = msg["Subject"]
    print("Sender:", sender)
    print("Recipient:", recipient)
    print("Date:", date)
    print("Subject:", subject)
    body = get_body(msg)
    print("Body:", body)
else:
    print("No recent email found from the sender.")
