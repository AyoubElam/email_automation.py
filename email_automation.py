import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body):
    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body of the email to the MIME message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
        server.starttls()  # Use TLS

        # Log in to your email account
        server.login(sender_email, 'YOUR_PASSWORD')  # Replace with your email password

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    sender = "your_email@gmail.com"  # Replace with your email
    receiver = "recipient_email@gmail.com"  # Replace with recipient's email
    subject = "Test Email"
    body = "This is a test email sent from my Python script!"

    send_email(sender, receiver, subject, body)

