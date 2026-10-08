import os


def convert_data(sample_user_input):
    """
    Given a list of simulated user input that are supposed to be numbers return a list of integers.
    If the value is unable to be convert it to an integer do not add it to the list of integers.

        Note: You should be catching exceptions here! Do not try to check the type!

    :param sample_user_input: A list
    :return: a list of integers
    """
    list = []
    x = 0
    for i in sample_user_input:
        try:
            i = int(i)
            list.append(i)
        except Exception:
            x += 1
            #list.append("{} is wrong".format(i))
    return list


def safe_open_text(file_path):
    """
    Given a filepath return an opened file handle in write text mode or raise a FileExistsError exception if the file exists!

    Note: Use the os module to check to see if the file exists!

    :param file_path:
    :return: file
    """
    if os.path.exists(file_path):
        raise FileExistsError("File already exists!!!")
    else:
        return open(file_path, "wt")


def read_in_people(file_path):
    """
    Using the Person, CNUPerson and Student classes in the given folder,
    we will be opening a csv text file and creating instances based upon the input data.
    We must be prepared to handle exceptions that may arise when working with these classes.

    :param file_path
    :return: a list of instances of Person, CNUPerson, and Student
    """
    from given.person import Person
    people = []
    x = 0
    with open(file_path) as file:
        for line in file:
            words = line.strip().split(",")
            if len(words) == 2:
                people.append(Person(words[0], words[1]))
            elif words[0] is not str:
                words0 = str(words[0])
                people.append(Person(words0, words[1]))
            elif words[0] == "" or words[0] == " ":
                x += 1
                #words0 = "Need first name"
                #people.append(Person(words0, words[1]))
            elif words[0] is int or words[0] is float:
                x += 1
                #words0 = "Cant be number"
                #people.append(Person(words0, words[1]))
    return people

if __name__ == '__main__':
    sample_data = [1, 5, 7, "9", "eleven"]
    expected = [1, 5, 7, 9]
    actual = convert_data(sample_data)
    print("Expected:", expected)
    print("Actual:", actual)

    try:
        file = safe_open_text(os.path.join("data","safe_open_test_file.txt"))
        file.close()    # Remember, always close the file!
    except FileExistsError as e:
        print(e)
    except Exception:
        print("Something went wrong, you raised the wrong exception?")

    people = read_in_people(os.path.join("data","people.txt"))
    for person in people:
        print(person)

    people = read_in_people(os.path.join("data","survey_data.txt"))
    for person in people:
        print(person)