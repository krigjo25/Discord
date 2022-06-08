

class StringManagement():

    def ReplaceCharacters(arg):

        """
            Replaces Symbols in the string
            
        """
        dictionary = {
                        '?':'',
                        ',':'',
                        '.':'',
                        ':':'',
                        '-':'',
                        '\'':'',
                        '\"':'',
                        '\\':'',
        }

        return arg.translate(str.maketrans(dictionary))