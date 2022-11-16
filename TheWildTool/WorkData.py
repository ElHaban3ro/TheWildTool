import os
import time

from threading import Thread

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import IPython
from scipy.io import wavfile


class VideoExtract:
    """Extract audio from video file.


    Returns:
        None: None return.
    """    

    converter_queue = [] # Cola. Podríamos añadir videos nuevos durante la ejecución se queire.
                         # Queue. We can add videos while application is running.


    def __init__(self) -> None:
        self.dataset_name = 'MyAudioDataset'
        self.save_folder = './'

    def __str__(self) -> str:
        return f'Converting Format: wav'




    def add_to_queue(self, videos_route: list):
        """Add file to queue

        Args:
            videos_route (list): List with paths of the videos to extract the audio. 

        Raises:
            ValueError: A different object was passed to a list.
        """        
        formats = ['mp4']

        if type(videos_route).__name__ == 'list':
            for route in videos_route:
                if os.path.isfile(os.path.abspath(route)):
                    if os.path.abspath(route).split('.')[-1] in formats: # is wav file.
                        self.converter_queue.append(os.path.abspath(route))


            print(f'\nAdd to queue success. Total queue {len(self.converter_queue)}')


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


                loading = True
                
                while loading:
                    converter_thread = Thread(target = lambda: ffmpeg_extract_audio(file_q, f'{save_route_clip}.wav'))
                    converter_thread.start()

                    while loading:
                        for loading_icon in [' - ', ' \ ', ' | ', ' / ']:
                            print(f'Extract audio from files... {loading_icon}', end='\r')
                            time.sleep(.5)
                            if converter_thread.is_alive() is False:
                                loading = False



                print(f'\n\nSuccessfully saved {file_q_c}-{self.dataset_name}.wav\ninside the folder {save_route_clip}')



class ProccessAudio:
    """Extract info from your audio files.
    """    



    def __init__(self) -> None:
        pass


    extract_queue = []
    wav_audios_objects = []





    
    def add_to_queue(self, route_files: list):
        """Adds a list of files to the queue.

        Args:
            route_file (str): List of routes.

            
        Raises:
            ValueError: You are passing another type of data that is not a list.
        """



        if type(route_files).__name__ == 'list':
            for route in route_files:

                if os.path.isfile(os.path.abspath(route)):
                    if os.path.abspath(route).split('.')[-1] == 'wav': # is wav file.
                        self.extract_queue.append(route)
                    
            print(f'\nAdd to queue success. Total queue {len(self.extract_queue)}')
        else:
            raise ValueError('(ErrorType) Only Support List.')




        if len(self.extract_queue) == 0:
            raise ValueError('(QueueEmpty) The queue is empty. You can add audios to the queue using ProccessAudio.add_to_queue')



        for file_audio_route in self.extract_queue:
            fs, read_audio_file = wavfile.read(file_audio_route) # Read wav file
            self.wav_audios_objects.append((read_audio_file, fs))
        





    # Con lo anterior, tenemos los audios wav cargados. De aquí para abajo, comenzaremos ahora sí a trabajar con ellos.

    def show(self, index: int):
        """Show audio in a notebook.

        Args:
            index (int): Index of element belonging to extract_queue.

        Raises:
            IndexError: Index out of range.

        Returns:
            IPython.display.Audio: The audio file to show. Use print.
        """            




        if index > len(self.wav_audios_objects) - 1 or index < 0:
            raise IndexError(f'(IndexOutOfRange) Pls, give a valid index. Remember: len of wav files to read is {len(self.wav_audios_objects)} ')

        else:
            return IPython.display.Audio(self.wav_audios_objects[index][0].T, rate=self.wav_audios_objects[index][1])


