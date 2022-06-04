
#   Python Responsories+
from pylib.list.ecrpglist import GeneralFAQ, CommunityFAQ, GameFAQ

class ECRPGFAQ():

    def __init__(self):
        pass

    def Introduction(question):

         #   Initializing lists

        faq = FrequentlyAskedQuestions()
        ecrpg =   [
                    GeneralFAQ(),
                    CommunityFAQ(),
                    GameFAQ()
        ]

        if question in faq:

            res = ''
            faq = CommonSAMPIssues()

            for i in faq:
                res += f"**Frequently Asked Questions**\n:arrow_right:{i}\n"

            return question, res

        elif question in ecrpg:

            response = {

                        #   General 

                        #   Community

                        #   GameFAQ

                        }    

            response = response[question]

            return question, response

        return