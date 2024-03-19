def process_email_ids(emails):
    usernames = []
    domains = []
    for email in emails:
        username, domain = email.split('@')
        usernames.append(username)
        domains.append(domain)
    return tuple(emails), tuple(usernames), tuple(domains)

n = int(input("Enter the number of students: "))
emails = []
for i in range(n):
    email = input(f"Enter email ID of student {i+1}: ")
    emails.append(email)

all_emails, usernames, domains = process_email_ids(emails)
print("All email IDs:", all_emails)
print("Usernames:", usernames)
print("Domains:", domains)
