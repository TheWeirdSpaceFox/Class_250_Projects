"""
HW 4 - Do this individually

@author Amanda Sanders
@version 9/2/21
"""


def split_emails(list_of_emails):
    """
    This function should take in a list of email addresses and split them by the "@" symbol and return a new list of usernames

    :param list_of_emails: a list of email addresses formatted like first.last.YY@domain.edu
    :return: usernames: List of usernames formatted like first.last.YY
    """
    i = 0
    list = []
    while i <= len(list_of_emails)-1:
        email = list_of_emails[i]
        user_split = email.split('@')
        user = user_split[0]
        cnu = user_split[1]
        list.append(user)
        i += 1

    return list



def create_email_headers(usernames):
    """
    This function should take in a list of usernames in the first.last.YY format and return a list of email greetings.
    In order to properly create an email greeting you will need to split the username into the first and last name components.
    Note: You should capitalize the first letter in each name!
    The format for the greeting should be "Dear Firstname Lastname," (Don't forget the comma!)

    :param usernames: usernames: a list of usernames formatted like first.last.YY
    :return: email_headers: a list of email headers formatted like "Dear Christopher Newport,"
    """
    i = 0
    list = []
    while i <= len(usernames)-1:
        split_user = usernames[i].split('.')
        first = split_user[0]
        first = first.capitalize()
        last = split_user[1]
        last = last.capitalize()
        greeting = 'Dear {} {},'.format(first, last)
        list.append(greeting)
        i += 1

    return list


def create_email_addresses(names):
    """
    This function will take in a list of names and will return email addresses with first.last.19@cnu.edu formatting.
    Note: Make sure to use the .lower() function to change the first and last names to all lower case!

    :param names: a list of names where the first and last name are space separated like example: "Bilbo Baggins"
    :return: email_addresses: a list of properly formatted email addresses first.last.19@cnu.edu
    """
    i = 0
    list = []
    while i <= len(names)-1:
        split = names[i].split()
        first = split[0]
        first = first.lower()
        last = split[1]
        last = last.lower()

        email = "{}.{}.19@cnu.edu".format(first, last)
        list.append(email)
        i += 1
    return list


if __name__ == "__main__":

    # Constant uses UPPER_CASE style
    NAMES = ["Anna Welch", "Victor Miller", "Isaac Paige", "Carl Wilkins", "Elizabeth Randall", "Karen Pullman",
                       "Sebastian Paterson", "Ava Powell", "Keith Fisher", "Nicholas Lawrence"]
    print(create_email_headers(split_emails(create_email_addresses(NAMES))))
    ADDRESSES = create_email_addresses(NAMES) # this is constant so UPPER_CASE style
    for address in ADDRESSES:
        print(address[-8:])
