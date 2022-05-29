
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
        }

        return arg.translate(str.maketrans(dictionary))

    def ReplaceBadGrammarEnglish(arg):

        """
            Replaceing bad english grammar

        """
        dictionary = {
                        'Whats':'What',
                        'Req':'requirement',
                        'Ive':'i have',
                        'Cant': 'Can not',
                        'dont':'Do not',
        }
        return arg.translate(str.maketrans(dictionary))