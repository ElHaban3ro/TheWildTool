import os
from TheWildTool.WorkData import VideoExtract, ProcessAudio



# convert = VideoExtract() # Instancia del cliente.
# convert.add_to_queue(['C:/Users/ferdh/Downloads/datatest/elmer.mp4']) # Añado contenido a la cola.
# convert.save_folder = 'C:/Users/ferdh/Downloads/datatest'

# converting = convert.to_audio()


files = os.listdir('C:/Users/ferdh/Downloads/datatest/audioexport')
files_abs = []
    
for file_r in files:
    files_abs.append(f'C:/Users/ferdh/Downloads/datatest/audioexport/{file_r}') # Para añadir la ruta absoluta. De esto se encarga el usuario.


a = ProcessAudio()
a.add_to_queue(files_abs)

