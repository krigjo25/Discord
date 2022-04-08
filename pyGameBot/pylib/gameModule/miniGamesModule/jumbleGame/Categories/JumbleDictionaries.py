

class JumbleCategory():

    def __init__(self) -> None:
        pass

    def Titles():
        category = [
                    ['randomJumbles', 'selecting a random jumble category\n'],
                    ['waltDisney', '- Classics,\n- Heros,\n- Princesses,\n - Villians\n'],
                    ['Animal kingdom', '- flyingCreatures \n- Cats\n'],
                    ]
        return category

    def SubTitle(sub):

        sub = str(sub)
        sub.lower()

        if sub == 'waltdisney':
            category = [
                            f'{sub}', '- Characters\n- Classics,\n- Roles']
        if sub == 'animalkingdom':

            category = [
                        f'{sub}', '- flyingCreatures \n- Cats,\n- Dogs']

        return category