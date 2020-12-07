import pandas as pd
from matches_2020 import matches

df = pd.read_csv("sign_ups_2020.csv")

for key in matches.keys():
    print("Key", key)
    first_name_key = key.split(' ')[0]
    name = matches[key]['send_to']
    print(name, "\n")
    row = df[df['Name'] == name].iloc[0]
    if isinstance(row['Address2'], str):
        address_line_1 = row['Address1'] + ' ' + str(row['Address2'])
    else:
        address_line_1 = row['Address1']
    address_line_2 = row['City'] + ', ' + row['State'] + ' ' + row['Zip']
    message = row['Body']

    with open(f'emails/{key}.txt', 'w+') as email:
        email.write(f"Dear {first_name_key},\n")
        email.write("\n")
        email.write("Thanks for signing up for our Third Annual Christmas Eve Book Exchange! This email will give you all of the details you need to gift someone a delightful book of your choosing and for their reading.\n")
        email.write("\n")
        email.write("Some notes up top:\n")
        email.write("1. Please make sure the book will arrive before Christmas Eve! We want everyone to be able to read their book on Christmas Eve and it would be a real shame to be cozying up by a fire with no reading material. Which brings me to number 2!\n")
        email.write("2. Please make sure to send a book! If you realize you can’t, please let us know and we will make sure that your assigned someone receives a book.\n")
        email.write("3. Ways to send your book:\n")
        email.write("\t- Buy your book from a local book store you want to support! Employees at the bookstore can even help you pick out a book; their knowledge tends to be encyclopedic. Go to a post office and ship your chosen book to your assigned someone’s address.\n")
        email.write("\t- Send a book from your very own shelves. Some of the most delightful prose is handwritten in the margins of a preowned book.\n")
        email.write("\t- Buy your book on https://bookshop.org/ or from a bookstore online and have it delivered to your assigned someone’s address directly.\n")
        email.write("\n")
        email.write("Here is the information for your assigned someone:\n")
        email.write(f"Name: {name}\n")
        email.write("Address:\n")
        email.write(address_line_1 + "\n")
        email.write(address_line_2 + "\n")

        if not isinstance(message, str):
            email.write("Message: *This person left no message. Let the universe guide you.*\n")
        else:
            email.write(f"Message: {message}\n")
        email.write("\n")
        email.write("This is so fun! Let us know if you have any questions.\n")
        email.write("\n")
        email.write("--\n")
        email.write("Best,\n")
        email.write("Haylee\n")
        email.write("Public Press")