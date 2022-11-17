from TheWildTool.WorkData import VideoExtract
from yt_dlp import YoutubeDL
import random
import os
import time


options = {
        'format': 'worst[height>144]',
        'outtmpl': f'./content/ContentVideoTest/%(title)s.mp4', 
        'ignoreerrors': True # Sometimes this is useful for when the playlist has premiers, but if it is for debugging leave it activated.
}

with YoutubeDL(options) as ydl:
  ydl.download('https://www.youtube.com/playlist?list=PLOYDNc5FY_0rl9bG9PONozysgubuJ7fuk')



files = os.listdir('./content/ContentVideoTest/')
files_abs_test = []

for file_r in files:
    files_abs_test.append(f'./content/ContentVideoTest/{file_r}') # Para añadir la ruta absoluta. De esto se encarga el usuario.


cClient = VideoExtract()
cClient.add_to_queue(files_abs_test)
print(cClient.converter_queue)




cClient.save_route = './content/ContentVideoTest'
cClient.to_audio(remove_original = False)