"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {689061386}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "2677896"))
API_HASH = getenv("API_HASH", "7f37813fa807d4df7ccd358218a25d51")
BOT_TOKEN = getenv("BOT_TOKEN", "5027615920:AAHb9zt9a_zYZn64MGxJkkd6nThxjYcVdGA")
SESSION_STRING = getenv("SESSION_STRING", "BQDArq2nS3bfQeEUepVD-rxj7qLpOKwkTC-rgnyW2BIWoiKtgYsfImHeSanPV4t1tcL73qYTAXewnb8mlrxvwJBzzrZHbgem_lICial4kIC1j__BrQPtCPSVn8mUDtubr-B5aeAaLpzJPNvru0nhHA9bCI-WnywubQGfYcbHWkTGEHuWhr7ylzzIDBxxxzg761RwCBjP--z3xz--27-0uQqpfePOucM43enaywe92yi-xcuKfeGeWhUZGbWs86_cD0a5JJA1iyZqFRaROLHkBkj7JcCaCzGcGCe3CedrXvu1f7UhBcAx4L4r2KkMAjdJCoZeNSTajqZ28IgAlpnEOEVEXL6vBgA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "activ3")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "lol")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
