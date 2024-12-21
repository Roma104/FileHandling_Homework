import emails

# Read the raw email content from email.txt
file_name = 'email.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        email_content = file.read()
        
        # Extract details using functions from emails.py
        sender = emails.email_sender(email_content)
        recipient = emails.email_recipient(email_content)
        subject = emails.email_subject(email_content)
        body = emails.email_body(email_content)
        
        # Print the extracted information
        print("Sender:", sender)
        print("Recipient:", recipient)
        print("Subject:", subject)
        print("Body:", body)
        
except FileNotFoundError:
    print(f"Error: The file {file_name} does not exist.")
