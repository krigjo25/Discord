import datetime

#   Discord responsory
import discord as d
from discord.utils import get
from discord.ui import InputText, Modal, select


class Member(Modal):


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.embed = d.Embed()
        self.kwargs = [kwargs]

        for i in self.kwargs:

            match i['title']:
                case "Member Report": self.report()
                case "Member Support": self.support()

        return

    def report(self):

        self.add_item(InputText(label = "Member", placeholder= "Member Name"))
        self.add_item(InputText(label = "Uniform Resource Locator", style=d.InputTextStyle.long, required= True, placeholder= "(link)"))
        self.add_item(InputText(label = "Reason", style=d.InputTextStyle.long, required= False, placeholder= ""))
        self.embed.colour = d.Colour.dark_red()

        return

    def support(self):

        self.add_item(InputText(label = "Image", placeholder= "Member", style=d.InputTextStyle.short))
        self.add_item(InputText(label = "Challange", placeholder= "Member", style=d.InputTextStyle.long))
        self.embed.colour = d.Colour.dark_red()
        return

    async def callback(self, interaction:d.Interaction):

        for i in self.kwargs:

            match i['title']:
                case "Member Report": ch = get(interaction.guild.text_channels, name = "report")
                case "Member Support":ch = get(interaction.guild.text_channels, name = "support")


        try:

            if not ch: raise Exception(f"{ch} does not exists")

        except Exception as e:
     
            ch = get(interaction.guild.channels, name = "auditlog")

             #   Prepare the embed message
            self.embed.description = f" {e}"
            self.embed.title = "An Exception Occured"
            self.embed.timestamp = datetime.datetime.now() 

            await ch.send(embed= self.embed)    #   Send the modal response

        else:

            #   Prepare the embed message
            self.embed.title = self.title
            self.embed.timestamp = datetime.datetime.now() 
            self.embed.set_author(name = f"Author: {interaction.user.name}")


            #   Prepare the user mode
            for i in range(len(self.children)): self.embed.add_field(name = self.children[i].label, value = self.children[i].value, inline= False)

            await interaction.response.defer()  #   Save the modal response
            await ch.send(embed= self.embed)    #   Send the modal response

        del ch, interaction
        return

class Channel(Modal):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.embed = d.Embed()
        self.channel()

        return

    def channel(self):

        self.add_item(InputText(label = "What do you want to create", placeholder= "eg. Forum / Text / Voice Channel", required= True))
        self.add_item(InputText(label = "Channel Name", placeholder= "eg. general-talk", required= True))
        self.add_item(InputText(label = "Age restriction", placeholder= "eg. Yes / No", required= True, default = "No"))
        self.add_item(InputText(label = "Description of the channel", placeholder= "eg. General member conversations" ,style=d.InputTextStyle.long, required = False, default = None))
        self.add_item(InputText(label = "Category (default None)", placeholder= "eg. SERVER SUPPORT"),style=d.InputTextStyle.long, required= False)
#        self.add_item(InputText(label = "Permissions (default hidden)", style=d.InputTextStyle.long, required= False, placeholder= "eg. Members / Moderator"))


        self.embed.colour = d.Colour.dark_red()

        return

    async def callback(self, interaction:d.Interaction):

        modal = [{
                    "ChannelType":self.children[0].value.lower(),
                    "ChannelName":self.children[1].value.lower(),
                    "Description":self.children[2].value.lower(),
                    "Category":self.children[3].value.upper(),
#                    "Permission":self.children[4].value.lower()
                }]

        print(modal)
        
        for i in modal:

            match i["ChannelType"]:
                case "forum":
                    ch = get(interaction.guild.forum_channels, name = f"{i['ChannelName']}")

                    try:
                        if ch: raise Exception(f"Forum Channel {ch} already exists")


                        else: 
                            #   Age restricted 
                            #   Category
                            #   Permisions

                            await interaction.guild.create_forum_channel(name= f"{i['ChannelName']}", category= i["Category"])

                    except (d.Forbidden, d.InvalidArgument, d.HTTPException, Exception) as e:
                        self.embed.title = self.title
                        self.embed.timestamp = datetime.datetime.now() 
                        self.embed.description = f"{e}"
                        await interaction.response.send_message(embed=self.embed, delete_after= 100.0)

        await interaction.response.send_message("Channel Created", delete_after=0.1)

        del interaction     #   Clearing some memory
        return
