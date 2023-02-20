import datetime

#   Discord responsory
import discord as d
from discord.utils import get
from discord.ui import InputText, Modal


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

class Role(Modal):
    '''
    #   1   Set a player's role
        sec = 60.0
        
        self.embed.title = f'Set the permissions for {role} '
        self.embed.description = 'Would you like to set the role\'s permissions?\n'
        await ctx.send(embed=self.embed)

        rolePerm = await self.bot.wait_for('message', timeout=sec)
        rolePerm = str(rolePerm.content).lower()

        self.embed.title = f' {role}\'s permissions'
        self.embed.description = 'Please type in one of the following selections '
        self.embed.add_field(name = 'Administrator', value = 'Basic user Role ')
        self.embed.add_field(name = 'Moderator', value = ' Moderator Role')
        self.embed.add_field(name = 'Member', value = ' Administrator role')
    
        await ctx.send(embed=self.embed)
        self.embed.clear_fields()

        role = await self.bot.wait_for('message', timeout=sec)
        role = str(voice.content).lower().replace(" ", "")

        match role:
            case "administrator":
                """
                    administrator = admin,
                    ban_members = bm,
                    mention_everyone = me,
                    kick_members    = km
                    manage_channels = mc,
                    manage_emojis = me,
                    manage_guild 
                    manage_messages
                    manage_nicknames
                    manage_permissions
                    manage_roles
                    manage_webhooks
                    change_nickname
                    create_instant_invite
                    move_members
                    mute_members
                    deafen_members = dm
                    priority_speaker
                    view_audit_log = val,
                    view_guild_insights = vgi,
                    manage_permissions = mp
                """

                #   Administrator Permissions
                self.embed.add_field(name='Administrator permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                ar = await self.bot.wait_for('message', timeout=sec)
                ar = ar.content

                if ar == True:

                    perm = Permissions(administrator = ar)

                    return perm
        
                #   Ban Members Permissions
                self.embed.add_field(name='Ban Members permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                bm = await self.bot.wait_for('message', timeout=sec)
                bm = str(bm.content)

                #   Manage Channels Permissions
                self.embed.add_field(name='Manage Channels permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mc = await self.bot.wait_for('message', timeout=sec)
                mc = str(mc.content)

                #   Manage Emoji Permissions
                self.embed.add_field(name='Manage Emoji permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                me = await self.bot.wait_for('message', timeout=sec)
                me = str(me.content)

                #   Manage Channels Permissions
                self.embed.add_field(name='Manage Guild permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mg = await self.bot.wait_for('message', timeout=sec)
                mg = str(mg.content)

                #   Manage Channels Permissions
                self.embed.add_field(name='Manage Message permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mm = await self.bot.wait_for('message', timeout=sec)
                mm = str(mm.content)

                #   Manage Nickname Permissions
                self.embed.add_field(name='Manage Nickname permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mn = await self.bot.wait_for('message', timeout=sec)
                mn = str(mn.content)

                #   Manage Roles Permissions
                self.embed.add_field(name='Manage Roles permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mr = await self.bot.wait_for('message', timeout=sec)
                mr = str(mr.content)

                #   Manage Webhooks Permissions
                self.embed.add_field(name='Manage Webhooks permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                mw = await self.bot.wait_for('message', timeout=sec)
                mw = str(mw.content)

                #   Change Nickname Permissions
                self.embed.add_field(name='Change NickName permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()
                    
                cn = await self.bot.wait_for('message', timeout=sec)
                cn = str(cn.content)

                #   Create Instant Invite Permissions
                self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                cii = await self.bot.wait_for('message', timeout=sec)
                cii = str(cii.content)

                #   Move member Permissions
                self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                move = await self.bot.wait_for('message', timeout=sec)
                move = str(move.content)

                #   Mute Members Permissions
                self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                mute = await self.bot.wait_for('message', timeout=sec)
                mute = str(mute.content)

                #   Deafen members Permissions
                self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                dm = await self.bot.wait_for('message', timeout=sec)
                dm = str(dm.content)

                #   Priority Speaker Permissions
                self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                ps = await self.bot.wait_for('message', timeout=sec)
                ps = str(ps.content)

                #   View Audit log Permissions
                self.embed.add_field(name='View Audit log Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                val = await self.bot.wait_for('message', timeout=sec)
                val = str(val.content)

                #   View guild insights Permissions
                self.embed.add_field(name='View guild insights Permissions', values='True or False')
                await ctx.send(embed=self.embed)
                self.embed.clear_fields()

                vgi = await self.bot.wait_for('message', timeout=sec)
                vgi = str(vgi.content)

            perm = Permissions(ban_members=bm, manage_channels = mc, manage_emojis = me, manage_guild = mg, manage_messages = mm,  manage_nicknames = mn, manage_roles = mr, manage_webhooks = mw, change_nickname = cn, create_instant_invite = cii, move_members = move, mute_members = mute, deafen_members = dm, priority_speaker = ps, view_audit_log = val, view_guild_insights = vgi)

        elif role == 'moderator':

            """

                manage_channels, manage_emojis, manage_guild, 
                manage_messages, manage_nicknames, manage_permissions, 
                manage_roles, manage_webhooks, change_nickname, 
                create_instant_invite, move_members, mute_members, 
                deafen_members, priority_speaker, view_audit_log, 
                view_guild_insights,

            """

            #   Kick Members Permissions
            self.embed.add_field(name='Kick Members permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            km = await self.bot.wait_for('message', timeout=sec)
            km = str(rmh.content)

            #   Manage Channels Permissions
            self.embed.add_field(name='Manage Channels permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mc = await self.bot.wait_for('message', timeout=sec)
            mc = str(mc.content)

            #   Manage Emoji Permissions
            self.embed.add_field(name='Manage Emoji permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            me = await self.bot.wait_for('message', timeout=sec)
            me = str(me.content)

            #   Manage Guild Permissions
            self.embed.add_field(name='Manage Guild permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mg = await self.bot.wait_for('message', timeout=sec)
            mg = str(mg.content)

            #   Manage Message Permissions
            self.embed.add_field(name='Manage Message permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mm = await self.bot.wait_for('message', timeout=sec)
            mm = str(mm.content)

            #   Manage Nickname Permissions
            self.embed.add_field(name='Manage Nickname permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mn = await self.bot.wait_for('message', timeout=sec)
            mn = str(mn.content)

            #   Manage Roles Permissions
            self.embed.add_field(name='Manage Roles permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mr = await self.bot.wait_for('message', timeout=sec)
            mr = str(mr.content)

            #   Manage Webhooks Permissions
            self.embed.add_field(name='Manage Webhooks permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            mw = await self.bot.wait_for('message', timeout=sec)
            mw = str(mw.content)

            #   Change Nickname Permissions
            self.embed.add_field(name='Change NickName permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            cn = await self.bot.wait_for('message', timeout=sec)
            cn = str(cn.content)

            #   Create Instant Invite Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            cii = await self.bot.wait_for('message', timeout=sec)
            cii = str(cii.content)

            #   Move member Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            move = await self.bot.wait_for('message', timeout=sec)
            move = str(move.content)

            #   Mute Members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            mute = await self.bot.wait_for('message', timeout=sec)
            mute = str(mute.content)

            #   Deafen members Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            dm = await self.bot.wait_for('message', timeout=sec)
            dm = str(dm.content)

            #   Priority Speaker Permissions
            self.embed.add_field(name='Create Instant Invite Permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            ps = await self.bot.wait_for('message', timeout=sec)
            ps = str(ps.content)

            perm = Permissions( kick_members=km, manage_channels = mc, manage_emojis = me, manage_guild = mg, manage_messages = mm, manage_nicknames = mn, manage_roles = mr,manage_webhooks = mw, change_nickname = cn, create_instant_invite = cii, move_members = move, mute_members = mute, deafen_members = dm, priority_speaker = ps )

        elif role == 'member':

            """ 
                #   Voice channels
                speak, request_to_speak, connect, stream

                #   Text Channels
                send_messages,
                read_message_history / view_channels, send_tts_messages,

                #   Misc
                add_reactions, attach_files,  embed_links, external_emojis, 
                use_slash_commands, use_voice_activation, value

            """

            #   Voice permissions
            self.embed.description = f'You selected {role} permissions'
            self.embed.add_field(name='Connect and speak in voice chat', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()

            conn = await self.bot.wait_for('message', timeout=sec)
            conn = str(conn.content)

            if conn == True:

                voice = True


            self.embed.add_field(name='Send Stream in voice channel', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            media= await self.bot.wait_for('message', timeout=sec)
            media= str(media.content)

            #   Send Messages permissions
            self.embed.add_field(name='Send Messages permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            msg = await self.bot.wait_for('message', timeout=sec)
            msg = str(msg.content)

            self.embed.add_field(name='Read entire history permissions', values='True or False')
            await ctx.send(embed=self.embed)
            self.embed.clear_fields()
                
            rmh = await self.bot.wait_for('message', timeout=sec)
            rmh = str(rmh.content)

            perm = Permissions(
                                speak = voice,
                                stream = media,
                                connect = conn,
                                send_messages=msg,
                                read_message_history=rmh,)

        else:

            perm = ''
            self.embed.title = f'Procsess canceled'

            await ctx.send(embed=self.embed)

        return perm
    '''
