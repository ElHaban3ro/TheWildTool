from TheWildTool.WorkData import VideoExtract



convert = VideoExtract() # Instancia del cliente.
convert.add_to_queue(['C:/Users/ferdh/Downloads/datatest/TWP-CLAVERO.mp4']) # Añado contenido a la cola.
convert.save_folder = 'C:/Users/ferdh/Downloads/datatest'



converting = convert.to_audio()