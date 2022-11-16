import os
import time

from threading import Thread

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio


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
        self.save_folder = './'

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

        Raises:
            FileNotFoundError: The save path does not exist.
        """                
        

        if len(self.converter_queue) == 0:
            print('WARNING: The list is empty. Make sure you are adding files to the queue. You may be passing wrong urls.')

        else:
            for file_q_c, file_q in enumerate(self.converter_queue):

                if os.path.isdir(os.path.abspath(self.save_folder)):
                    try:
                        os.mkdir(f'{os.path.abspath(self.save_folder)}/audioexport')

                    except:
                        pass

                else:
                    raise FileNotFoundError('(SaveRouteError) Please change the save path to a correct one, or delete your confuguration so that it assigns itself.')
                        

                self.save_folder = f'{os.path.abspath(self.save_folder)}/audioexport'


                save_route_clip = os.path.abspath(f'{self.save_folder}/{file_q_c}-{self.dataset_name}')

                print('')

                
                while True:
                    converter_thread = Thread(target = lambda: ffmpeg_extract_audio(file_q, f'{save_route_clip}.{self.to_format}'))
                    converter_thread.start()

                    while True:
                        for loading_icon in [' - ', ' \ ', ' | ', ' / ']:
                            print(f'Extract audio... {loading_icon}', end='\r')
                            time.sleep(.5)
                            if converter_thread.isAlive() is False:
                                break

                    break



                print(f'Successfully saved {file_q_c}-{self.dataset_name}.{self.to_format} inside the folder {save_route_clip}')

                # os.remove(f'{save_route_clip}.mp4') # Elimina finalmente todo. Comentado para el testeo.
