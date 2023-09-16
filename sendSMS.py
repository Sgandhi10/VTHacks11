import smtplib

def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    import smtplib
    """this is some test documentation in the function"""
    message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()

if __name__ == "__main__":
    sendMail("sohamgandhi@live.com", "sohamgandhi@live.com", "Test", "Test", "localhost")
