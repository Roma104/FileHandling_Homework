import re

# Function to fetch the sender email address
def email_sender(email_content):
    match = re.search(r"From:.*<([^>]+)>", email_content)
    if match:
        return match.group(1)
    return None

# Function to fetch the recipient email address
def email_recipient(email_content):
    match = re.search(r"To:.*<([^>]+)>", email_content)
    if match:
        return match.group(1)
    return None

# Function to fetch the subject of the email
def email_subject(email_content):
    match = re.search(r"Subject: (.*)", email_content)
    if match:
        return match.group(1)
    return None

# Function to fetch the body of the email
def email_body(email_content):
    match = re.search(r"Content-Type:.*text/plain; charset=.*\n\n(.*)", email_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None