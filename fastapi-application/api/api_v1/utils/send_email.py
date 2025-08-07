from email.message import EmailMessage

import aiosmtplib


async def send_email():
    message = EmailMessage()
    message["From"] = "root@localhost"
    message["To"] = "somebody@example.com"
    message["Subject"] = "Hello World!"
    message.set_content("Sent via aiosmtplib")

    recipient = ""
    await aiosmtplib.send(  # move config
        message,
        sender="email_sender@pet_care.com",
        recipients=[recipient],
        hostname="localhost",
        port=1025,
    )
