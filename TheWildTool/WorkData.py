import os
import time

from threading import Thread

from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import IPython
from scipy.io import wavfile

import matplotlib.pyplot as plt
import numpy as np

from yt_dlp import YoutubeDL




class VideoExtract:
    """Extract audio from video file.


    Returns:
        None: None return.
    """    

    converter_queue = [] # Cola. Podríamos añadir videos nuevos durante la ejecución se queire.
                         # Queue. We can add videos while application is running.


    def __init__(self) -> None:
        self.dataset_name = 'MyAudioDataset'
        self.save_route = './'

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



        
    def to_audio(self, remove_original = True):
        """Extract the audio from the video.

        Args:
            remove_original (bool, optional): After conversion, delete the video. Defaults to True.

        Raises:
            FileNotFoundError: The save path does not exist.
        """                
        

        if len(self.converter_queue) == 0:
            print('WARNING: The list is empty. Make sure you are adding files to the queue. You may be passing wrong urls.')

        else:
            for file_q_c, file_q in enumerate(self.converter_queue):
                file_format = os.path.basename(file_q).split('.')[-1]
                new_file = f'{os.path.dirname(os.path.abspath(file_q))}/{file_q_c}.{file_format}'
                
                base_route = f'{os.path.dirname(os.path.abspath(file_q))}'
                os.rename(file_q, new_file)
                file_q = new_file

                if os.path.isdir(os.path.abspath(self.save_route)):
                    try:
                        os.mkdir(f'{base_route}/{self.dataset_name}-AudioExport/')

                    except:
                        pass

                else:
                    raise FileNotFoundError('(SaveRouteError) Please change the save path to a correct one, or delete your confuguration so that it assigns itself.')
                        

                r = f'{os.path.abspath(self.save_route)}/{self.dataset_name}audioexport'


                save_route_clip = os.path.abspath(f'{base_route}/{file_q_c}-{self.dataset_name}')

                loading = True
                print(file_q)

                video_clip = VideoFileClip(file_q)
                video_clip_audio = video_clip.audio

                while loading:
                    converter_thread = Thread(target = lambda: video_clip_audio.write_audiofile(f'{save_route_clip}.wav'))
                    converter_thread.start()
                    
                    while loading:
                        for loading_icon in [' - ', ' \ ', ' | ', ' / ']:
                            print(f'Extract audio from files... {loading_icon}', end='\r')
                            time.sleep(.5)
                            if converter_thread.is_alive() is False:

                                loading = False



                if remove_original:
                    os.remove(file_q)
                    print(f'\n\n{file_q} fue elimiando.')
                print(f'\n\nSuccessfully saved {file_q_c}-{self.dataset_name}.wav\ninside the folder {os.path.dirname("f{save_route_clip}.wav")}')



class ProccessAudio:
    """Extract info from your audio files.
    """    



    def __init__(self) -> None:
        self.dataset_name = 'MyDataset'
        self.save_route = './'


    extract_queue = []
    wav_array = []


   
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
                        
            if len(self.extract_queue) == 0:
                print('WARNING: The queue is empty. You can add audios to the queue using ProccessAudio.add_to_queue. REMEMBER: Only support wav files.')

            else:
                print(f'\nAdd to queue success. Total queue {len(self.extract_queue)}')

        else:
            raise ValueError('(ErrorType) Only Support List.')






        for file_audio_route in self.extract_queue:
            self.wav_array.append(wavfile.read(file_audio_route))
        




    # Con lo anterior, tenemos los audios wav cargados. De aquí para abajo, comenzaremos ahora sí a trabajar con ellos.
    def listen(self, index: int):
        """Show audio in a notebook.

        Args:
            index (int): Index of element belonging to extract_queue.

        Raises:
            IndexError: Index out of range.

        Returns:
            IPython.display.Audio: The audio file to show. Use print.
        """            

        if index > len(self.wav_array) - 1 or index < 0:
            raise IndexError(f'(IndexOutOfRange) Pls, give a valid index. Remember: len of wav files to read is {len(self.wav_array)} ')
        else:
            return IPython.display.Audio(self.wav_array[index][1].T, rate=self.wav_array[index][0])




    def view(self, index: int, grid = False, save = False, image_size = (20, 10), **kwargs):
        """It generates a graph that represents the decibels of your audio over time.

        Args:
            index (int): Indicate your element inside the queue!
            grid (bool, optional): Activate or deactivate the grid of your chart. Defaults to False.
            save (bool, optional): Save the graph in its save_route. Defaults to False.
            image_size (tuple, optional): Image size (it is not presented in pixels. It is useful to download this if you don't have a good graphic). Defaults to (20, 10).
            **kwargs (optional).

        Raises:
            IndexError: The last index does not correspond to any of the queue list.
        """        

        

        if index > len(self.wav_array) - 1 or index < 0:
            raise IndexError(f'(IndexOutOfRange) Pls, give a valid index. Remember: len of wav files to read is {len(self.wav_array)} ')

        else:
            samples = len(self.wav_array[index][1]) # Muestras. (Un array. Esto vendría a representar el eje Y)
            time_x = np.arange(0, samples/self.wav_array[index][0], 1/self.wav_array[index][0]) # Esto representa el tiempo. La duración del audio, el eje X.


            fig, ax = plt.subplots(figsize = image_size)
            fig.patch.set_facecolor('white')

            ax.plot(time_x, self.wav_array[index][1], c = 'tab:blue') # "Estampamos" los datos.
            ax.set_title(f'View at {self.dataset_name}')
            ax.set_xlabel('Seconds [s]')
            ax.set_ylabel('dB Amplitud [dB]')

            ax.grid(grid)

            fig.tight_layout()
            plt.show()

            if save: # If the user wants to save
                if 'format' in kwargs: # If the user give the format
                    fig.savefig(f'{os.path.abspath(self.save_route)}/{index}-{self.dataset_name}-Figure.{kwargs["format"]}')
                    print('TheWildTool: Image saved.')

                else:
                    raise ValueError('(FormatError) You do not give the saving format. The value is given with kw format="myformat"')







class GenerateDataset:
    """Generates datasets based on multimedia content from the Internet. 
    """    

    def __init__(self) -> None:
        self.format_yt_dlp = 'worst[height>144]' # Config of YT-DLP
        self.save_route = './'
        self.dataset_name = 'MyDataset'


    def youtube(self, playlist: str, delete_original = True, video_mode = False):
        """Generate a dataset based on a youtube playlist.

        Args:
            playlist (str): Playlist URL.
            delete_original (bool, optional): If video mode is false, the video file are removed. Defaults to True.
            video_mode (bool, optional): It will generate a video dataset. It maximizes the "medium" video quality, where it is not so low, but enough to train a model (maybe even very high). 3 hours of video usually weighs 150mb's. Defaults to False.

        Raises:
            ValueError: The url passed is wrong (it is not a playlist).
        """        

        if 'playlist?list=' not in playlist:
            raise ValueError('(URLPlaylist) be sure to pass the correct url of your YOUTUBE playlist.')

        else:
            save_folder = f'{os.path.abspath(self.save_route)}/{self.dataset_name}/'
            
            try:
                os.mkdir(save_folder)
            except:
                pass


            # Config dict.
            options = {
                'format' : self.format_yt_dlp,
                'outtmpl': f'{os.path.abspath(self.save_route)}/{self.dataset_name}/%(title)s.mp4',
                'ignoreerrors': True # Sometimes this is useful for when the playlist has premiers, but if it is for debugging leave it activated.
            }
            
            with YoutubeDL(options) as ytdl:
                ytdl.download(playlist)


            files_list = os.listdir(save_folder)
            files_list_abs = []

            for file_name in files_list:
                files_list_abs.append(f'{save_folder}/{file_name}') # List of files with absolute url.


            if video_mode:
                for file_c, file_route in enumerate(files_list_abs):
                    file_format = os.path.basename(file_route).split('.')[-1]
                    os.rename(file_route, f'{os.path.dirname(file_route)}/{file_c}.{file_format}')
                    print('TheWildTool: The video dataset has been generated!!!!')

            else:
                extract = VideoExtract()
                extract.add_to_queue(files_list_abs)
                extract.dataset_name = self.dataset_name


                extract.to_audio(remove_original = delete_original)
                print('TheWildTool: The audio dataset has been generated!!!!')