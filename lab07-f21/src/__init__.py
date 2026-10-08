from difflib import SequenceMatcher
import os
class encoder_decoder:

    def __init__(self, key):
        self.key = key

## encode has to equal false
    def encode(self, input_file_name, input_directory, output_file, output_directory):
        file_path = os.path.join(input_directory, input_file_name)
        outText = []
        with open(file_path, encoding = "utf-8") as file:
            file = file.readlines()
            for thing in file:
                thing = thing.strip()
                cryptText = []
                step = self.key
                symbols = [":",' ',"<",",",">",".","^",";","!","?","@","[","#","]","$","!","%","-","&","'","*",'"',"{",
                               "(","}",")","/","ú","ó","+","í","=","é","_","á","~","#"]
                number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                uppercase=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                lowercase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                for newletter in thing:
                    if newletter in uppercase:
                        index = uppercase.index(newletter)
                        crypting = (index + step) % 26
                        cryptText.append(crypting)
                        newLetter = uppercase[crypting]
                        outText.append(newLetter)
                    elif newletter in lowercase:
                        index = lowercase.index(newletter)
                        crypting = (index + step) % 26
                        cryptText.append(crypting)
                        newLetter = lowercase[crypting]
                        outText.append(newLetter)
                    elif newletter in number:
                        index = number.index(newletter)
                        crypting = (index + step) % 9
                        cryptText.append(crypting)
                        newLetter = number[crypting]
                        outText.append(newLetter)
                    elif newletter in symbols:
                        index = symbols.index(newletter)
                        crypting = (index + step) % 37
                        cryptText.append(crypting)
                        newLetter = symbols[crypting]
                        outText.append(newLetter)
                outText.append("`")

        string = ''
        for letter in outText:
           string += letter
        file_exit = os.path.join(output_directory, output_file+".enc")
        with open(file_exit, "wt", encoding = "utf-8") as file2:
            file2.write(string)

        pass


    def decode(self,input_file_name, input_directory, output_file, output_directory):
        file_path = os.path.join(input_directory, input_file_name)
        outText = []
        with open(file_path, encoding = "utf-8") as file:
            file = file.readlines()
            for thing1 in file:
                thing1 = thing1.strip()
                for thing in thing1:
                    step = self.key
                    cryptText = []
                    symbols = [":",' ',"<",",",">",".","^",";","!","?","@","[","#","]","$","!","%","-","&","'","*",'"',"{",
                               "(","}",")","/","ú","ó","+","í","=","é","_","á","~","#"]
                    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                 'U', 'V', 'W', 'X', 'Y', 'Z']
                    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                                 'u', 'v', 'w', 'x', 'y', 'z']
                    for newletter in thing:
                        if newletter in uppercase:
                            index = uppercase.index(newletter)
                            crypting = (index - step) % 26
                            cryptText.append(crypting)
                            newLetter = uppercase[crypting]
                            outText.append(newLetter)
                        elif newletter in lowercase:
                            index = lowercase.index(newletter)
                            crypting = (index - step) % 26
                            cryptText.append(crypting)
                            newLetter = lowercase[crypting]
                            outText.append(newLetter)
                        elif newletter in number:
                            index = number.index(newletter)
                            crypting = (index - step) % 9
                            cryptText.append(crypting)
                            newLetter = number[crypting]
                            outText.append(newLetter)
                        elif newletter in symbols:
                            index = symbols.index(newletter)
                            crypting = (index - step) % 37
                            cryptText.append(crypting)
                            newLetter = symbols[crypting]
                            outText.append(newLetter)
                        elif newletter == "`":
                            outText.append("\n")


        string = ''
        for letter in outText:
            string += letter
        file_exit = os.path.join(output_directory, output_file +".dec")
        with open(file_exit, "wt", encoding = "utf-8") as file2:
            file2.write(string)
        pass

    def validate(self, source_file_name, source_directory, output_file, output_directory):
        file_path_origin = os.path.join(source_directory, source_file_name)
        file_path_output = os.path.join(output_directory, output_file)
        distance = 0
        list_file = []
        list_file2 = []
        with open(file_path_origin, encoding= 'utf-8') as file:
            list_file.append(file.readlines())
        with open(file_path_output, encoding= "utf-8") as file2:
            list_file2.append(file2.readlines())
        string1 = ""
        string2 = ""
        dict1 = {}
        dict2 = {}
        for list in list_file:
            list1 = list
            for i in list1:
                string1 += i
        for list in list_file2:
            list1 = list
            for i in list1:
                string2 += i
        for i in range(len(string1)) and range(len(string2)):
            if string1[i] != string2[i]:
                distance += 1
            dict1[i] = string1[i]
            dict2[i] = string2[i]
        seq = SequenceMatcher(None, string1, string2).ratio()
        with open(file_path_origin, encoding = "utf-8") as file:
            file = file.readlines()
            for thing1 in file:
                thing1 = thing1.strip()
            with open(file_path_output, encoding = "utf-8") as file2:
                file2 = file2.readlines()
                for thing2 in file2:
                    thing2 = thing2.strip()

                if thing1 == thing2:
                    return "True", distance, seq, #dict1, dict2
                else:
                    return "False", distance, seq, #dict1, dict2

    def compare(self, source_file_name, source_directory, output_file, output_directory):
        file_path_origin = os.path.join(source_directory, source_file_name)
        file_path_output = os.path.join(output_directory, output_file)
        distance = 0
        list_file = []
        list_file2 = []
        with open(file_path_origin, encoding = "utf-8") as file:
            list_file.append(file.readlines())
        with open(file_path_output, encoding = "utf-8") as file2:
            list_file2.append(file2.readlines())
        string1 = ""
        string2 = ""
        dict1 = {}
        dict2 = {}
        for list in list_file:
            list1 = list
            for i in list1:
                string1 += i
        for list in list_file2:
            list1 = list
            for i in list1:
                string2 += i
        for i in range(len(string1)) and range(len(string2)):
            if string1[i] != string2[i]:
                distance += 1
            dict1[i] = string1[i]
            dict2[i] = string2[i]
        seq = SequenceMatcher(None, string1, string2).ratio()
        #seq = SequenceMatcher(None, string1, string2).get_matching_blocks()
        return distance, seq, #dict1, dict2



