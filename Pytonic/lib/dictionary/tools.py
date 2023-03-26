
import requests as req
from os import getenv

class APITools():

    #   API-Ninja

    def NinjaRandomWord(self):

        '''
            API by API-Ninja
            API to choose a randomly generated word
        '''

        parse = 'https://api.api-ninjas.com/v1/randomword'
        response = req.get(parse, headers={'X-Api-Key': getenv("DictionaryToken")})
        string = ""

        try:

            if response.status_code != req.codes.ok: raise Exception("Something went wrong with the connection to Ninja API")
        except Exception as e : return e
        else:

            for i in response.text:
                if i.isalpha(): string += i

        del parse, response#   Clear some space

        return string

    def NinjaDefinition(self, word):

        """
            #   API by API-Ninja
            # Using an api to check wether the word exist or not.
        """

        parse = f'https://api.api-ninjas.com/v1/dictionary?word={word}'
        response = req.get(parse, headers={'X-Api-Key': getenv("DictionaryToken")})
        json = dict(response.json())

        try:
            if response.status_code != req.codes.ok: raise Exception(response.status_code)

        except Exception as e: return e

        for i, j in json.items():

            if "valid" in i : 
                del word, parse, response, json#   Clear some memory
                
                return j
