from GayuMusic.core.bot import Alone
from GayuMusic.core.dir import dirr
from GayuMusic.core.git import git
from GayuMusic.core.userbot import Userbot
from GayuMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Alone()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
