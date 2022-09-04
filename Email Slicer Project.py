# Email Slicer Project

# Ask for user Email
email = input ("Please enter your email address!: ").strip()
# Slice out username
user = email[:email.index('@')]
domain = email[email.index('@')+ 1:]
# Format message
output = "Your username is {} and your domain name is {}".format(user,domain)
# Display Output
print(output)