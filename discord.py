import pyqrcode
import png
from discord_webhook import DiscordWebhook, DiscordEmbed

#proxies if you want to use it : list here https://free-proxy-list.net/
proxies = {
  'https': 'https://45.76.164.105:3128',
  'http': 'http://194.32.78.237:80',
}

#Webhooks part.
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/ - Enter the hook here')

#ask for link.
urlq = input("Enter the link you want to make QR as. ")
nam1 = input("Enter file name. ")
size = input("Enter file size. ")

big_code = pyqrcode.create(urlq)
big_code.png('QR.png', scale=6)
big_code.show()


#Image Upload to server.
with open("QR.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='QR.jpg')

embed = DiscordEmbed(title=nam1, description=size, color=242424)


# add embed object to webhook
webhook.add_embed(embed)
webhook.set_proxies(proxies)
webhook.execute()
