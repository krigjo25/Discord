
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
        arg = str(arg)
        
        badGrammar = ['Whats',]

        if arg in badGrammar:
            print('arg test', arg)
            dictionary = {
                        'Whats':'What',
                        'Req':'requirement',
                        'Ive':'i have',
                        'Cant':'Can not',
                        'dont':'Do not',
            }
            print (arg, badGrammar)
            dictionary = dictionary[badGrammar]
            arg.replace(badGrammar, dictionary)
            print(arg)
            return arg