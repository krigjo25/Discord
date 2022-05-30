

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
        badGrammar = ['Whats', 'Req', 'Ive', 'Cant', 'dont']
        
        dictionary = {
                        'Whats':'What',
                        'Req':'Requirements',
                        'Ive':'i have',
                        'Cant':'can not',
                        'dont':'do not',
        }
        #   Replace badGrammar with good grammar.
        
        str(arg).replace('Whats', 'What')
        print('function test',arg)
        return arg