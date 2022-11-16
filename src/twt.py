from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

import os


class VideoExtract:
    """Extract audio from video file.


    Returns:
        None: None return.
    """    

    converter_queue = [] # Cola. Podríamos añadir videos nuevos durante la ejecución se queire.
                         # Queue. We can add videos while application is running.


    def __init__(self) -> None:
        self.to_format = 'mp3'
        self.dataset_name = 'MyAudioDataset'
        self.folder_to_save = './'

    def __str__(self) -> str:
        return f'Converting Format: {self.to_format}'




    def add_to_queue(self, videos_route: list):
        """Add file to queue

        Args:
            videos_route (list): List with paths of the videos to extract the audio. 

        Raises:
            ValueError: A different object was passed to a list.
        """        

        if type(videos_route).__name__ == 'list':
            for route in videos_route:
                if os.path.isfile(os.path.abspath(route)):
                    self.converter_queue.append(os.path.abspath(route))

        else: 
            raise ValueError('(ErrorType) Only Support List.')



        
    def to_audio(self):
        """Extract the audio from the video.
        """        
        

        if len(self.converter_queue) == 0:
            print('WARNING: The list is empty. Make sure you are adding files to the queue. You may be passing wrong urls.')

        else:
            for file_q_c, file_q in enumerate(self.converter_queue):
                clip = VideoFileClip(file_q)
                clip = clip.subclip(1, 10)

                if os.path.isdir(os.path.abspath(self.folder_to_save)):
                    try:
                        os.mkdir(f'{os.path.abspath(self.folder_to_save)}/audioexport')

                    except:
                        pass
                        

                self.folder_to_save = f'{os.path.abspath(self.folder_to_save)}/audioexport'


                save_route_clip = os.path.abspath(f'{self.folder_to_save}/{file_q_c}-{self.dataset_name}')

                clip.write_videofile(f'{save_route_clip}.mp4') # guardo el video en mp3 independientemente de en qué formato esté inicialmente.
                ffmpeg_extract_audio(f'{save_route_clip}.mp4', f'{save_route_clip}.{self.to_format}')

                # os.remove(f'{save_route_clip}.mp4') # Elimina finalmente todo. Comentado para el testeo.

                        
            




        




# convert = VideoExtract() # Instancia del cliente.
# convert.add_to_queue(['C:/Users/ferdh/Downloads/datatest/TWP-CLAVERO.mp4']) # Añado contenido a la cola.

# converting = convert.to_audio()