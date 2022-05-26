
class StringManagement():

    def ReplaceCharacters(arg):

        """
            Replaces given characters in the string
            
        """
        dictionary = {
                        '?':'',
                        ',':'',
                        '.':'',
                        ':':'',
                        '-':'',
                        '\'':'',
                        '\"':'',
        }

        return arg.translate(str.maketrans(dictionary))
