This file is part of the AutoAnime distribution.

Copyright (c) 2025 Kaif_00z



This program is free software: you can redistribute it and/or modify

it under the terms of the GNU General Public License as published by

the Free Software Foundation, version 3.



This program is distributed in the hope that it will be useful, but

WITHOUT ANY WARRANTY; without even the implied warranty of

MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU

General Public License for more details.



License can be found in <

https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

if you are using this following code then don't forgot to give proper

credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config

class Var: # Version

version = "v0.0.8"

# Telegram Credentials

API_ID = config("API_ID", default=16978078, cast=int)
API_HASH = config("API_HASH", default="91ccaf748f031b656bbf64ff47f990e3")
BOT_TOKEN = config("BOT_TOKEN", default="8155621239:AAGZF_wN_jXkK3fEOgzCHM5a19SUVFhLf4s")
SESSION = config("SESSION", default=None)

# Database Credentials

MONGO_SRV = config("MONGO_SRV", default="mongodb+srv://autoanime:autoanime@cluster0.iimy622.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Channels Ids

BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1001945054800, cast=int)
MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1002335038787, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", default=-1002674737457, cast=int)
CLOUD_CHANNEL = config("CLOUD_CHANNEL", default=-100235858844, cast=int)

FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default=0, cast=int) 
OWNER = config("OWNER", default=1077880102, cast=int)

# Other Configs

THUMB = config(
    "THUMBNAIL", default="https://envs.sh/s/6mkCjdFJApbEYZX8stsBuA/r4q.jpg")
FFMPEG = config("FFMPEG", default="ffmpeg")
CRF = config("CRF", default="25")
SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
LOG_ON_MAIN = config("LOG_ON_MAIN", default=False, cast=bool)

FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="", cast=str) # Dev Configs

DEV_MODE = config("DEV_MODE", default=False, cast=bool)

Indentation issue

