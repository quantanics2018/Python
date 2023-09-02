import ssl
import smtplib
from email.message import EmailMessage

# Your email sender details
email_sender = "rajeshadhiban2005@gmail.com"
email_password = "zswwbvqdccmewtrz"  # This is an example password, use your actual password
email_receiver = "dianoman12@gmail.com"
subject = "Testing from Adhiban"
body = """
This is my Python program for Sending email checking
"""

# Create an EmailMessage instance
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Create an SSL context for secure connection
context = ssl.create_default_context()

# Connect to the Gmail SMTP server using SSL
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Log in to the sender's email account
    smtp.login(email_sender, email_password)
    
    # Send the email
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# Print a success message
print("Mail sent successfully")
