# Python libs.
import os

# External libs.
from moviepy.editor import VideoFileClip, AudioFileClip
import IPython
import matplotlib.pyplot as plt
import numpy as np
from yt_dlp import YoutubeDL


# Our libs
from .TWTErrors import * # Errors classes



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
        return f'Converting Format: mp3'




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
                    if os.path.abspath(route).split('.')[-1] in formats: # is mp3 file.
                        self.converter_queue.append(os.path.abspath(route))


            print(f'\nAdd to queue success. Total queue {len(self.converter_queue)}')


        else: 
            raise ValueError('(ErrorType) Only Support List.')



        
    def to_audio(self, remove_original = True, audio_bitrate = '20k'):
        """Extract the audio from the video.

        Args:
            remove_original (bool, optional): After conversion, delete the video. Defaults to True.
            audio_fps (int, optional): Frequency at which you want to save the audio. Remember: higher frequency, higher quality, but therefore, higher weight.
            audio_fps (str, optional): String of the amount of bitrate your audio has. The string should be something like "50k", "777k" or "5k", but keep in mind that more Bitrate represents more weight in the file (but more quality).

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



                save_route_clip = os.path.abspath(f'{base_route}/{self.dataset_name}-AudioExport/{file_q_c}-{self.dataset_name}')
                try:
                    os.mkdir(f'{base_route}/{self.dataset_name}-AudioExport/')

                except:
                    pass



                video_clip = VideoFileClip(os.path.normpath(file_q))
                video_clip_audio = video_clip.audio


                file_destin = os.path.normpath(f'{save_route_clip}.mp3')


                print(os.path.normpath(file_q))
                print(file_destin)
                target = video_clip_audio.write_audiofile(file_destin, bitrate = audio_bitrate, ffmpeg_params = ['-ac', '2'])
                video_clip.close()

                if remove_original:
                    os.remove(file_q)
                    print(f'\n\n{file_q} fue elimiando.')
                print(f'\n\nSuccessfully saved {file_q_c}-{self.dataset_name}.mp3\ninside the folder {os.path.dirname(f"{save_route_clip}.mp3")}')



class ProccessAudio:
    """Extract info from your audio files.
    """    



    def __init__(self) -> None:
        self.dataset_name = 'MyDataset'
        self.save_route = './'


    extract_queue = []
    mp3_array = []


   
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
                    if os.path.abspath(route).split('.')[-1] == 'mp3': # is mp3 file.
                        self.extract_queue.append(route)
                        
            if len(self.extract_queue) == 0:
                print('WARNING: The queue is empty. You can add audios to the queue using ProccessAudio.add_to_queue. REMEMBER: Only support mp3 files.')

            else:
                print(f'\nAdd to queue success. Total queue {len(self.extract_queue)}')

        else:
            raise ValueError('(ErrorType) Only Support List.')




    def queue_to_array(self):
        """Transforms the tail array into numpy arrays. If you do not process the audios with this method you will not be able to see to them.
        """
        for file_audio_route in self.extract_queue:
            print('Reading file as Array...', '\r')

            # TODO: ¿Aumentando el buffersize?
            audio = AudioFileClip(file_audio_route)
            a_array = audio.to_soundarray()
            self.mp3_array.append(a_array)
            print('Read!', '\r')




    # Con lo anterior, tenemos los audios mp3 cargados. De aquí para abajo, comenzaremos ahora sí a trabajar con ellos.
    def listen(self, index: int):
        """Show audio in a notebook.

        Args:
            index (int): Index of element belonging to extract_queue.

        Raises:
            IndexError: Index out of range.

        Returns:
            IPython.display.Audio: The audio file to show. Use print.
        """            

        try:
            return IPython.display.Audio(self.extract_queue[index])
        except IndexError:
            raise IndexError(f'(IndexOutOfRange) Pls, give a valid index. Remember: len of mp3 files to read is {len(self.mp3_array)} ')




    def see(self, index: int, grid = False, save = False, image_size = (20, 10), **kwargs):
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

        

        try:
            samples = len(self.mp3_array[index]) # Muestras. (Un array. Esto vendría a representar el eje Y)
            time_x = np.arange(0, samples/44100, 1/44100) # Esto representa el tiempo. La duración del audio, el eje X.


            fig, ax = plt.subplots(figsize = image_size)
            fig.patch.set_facecolor('white')

            ax.plot(time_x, self.mp3_array[index], c = 'tab:blue') # "Estampamos" los datos.
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

        except IndexError:
            raise IndexError(f'(IndexOutOfRange) Pls, give a valid index. Remember: len of mp3 files to read is {len(self.mp3_array)} ')


    def segment(self, index:int, segment_file:str):
        """Cut a long audio into small segments that you use to train a model or whatever else you decide.

        Args:
            index (int): Index of your element in the queue.
            segment_file (str): Path of the segmentation file for that mp3 file in the list.

        Raises:
            ValueError: File with segmentation information.
            NoHeaderError: Your file does not contain a header with the proper syntax. Check the documentation to learn more.
            TimeTypeError: The time format is wrong or not yet supported.
        """        
        tuple_list = []

        try:
            f_to_seg = self.extract_queue[index]
            # a_to_seg = self.mp3_array[index] # Too bigger size. :/

        except IndexError:
            raise ValueError(f'(OutOfIndexError) The index provided does not belong to any of the list. Remember that the length of the list is {len(self.extract_queue)}.')
        
        if os.path.isfile(segment_file): # File exist
            # Name == file???? 
            with open(segment_file, 'r+') as segments:
                lines = segments.readlines()
                # Line 0 is the meta info line.
                meta_info = lines[0].split('][') # Return 3 objects list.
                try:
                    info_dict = {'datasetName': meta_info[0][1:], 'entities': meta_info[1].split(', '), 'timeType': meta_info[2], 'videoName': meta_info[3][:-2]} # Header!
                except IndexError:
                    raise NoHeaderError()


                lines_inline = ''

                for line in lines[1:]:
                    if '\n' in line[:1]: # empty
                        continue
                    elif line[0] == '#': # Commented line.
                        continue
                    
                    lines_inline = f'{lines_inline} {line}'
                
                segments_list = lines_inline.split('!')[1:] # Split by entitie.

                for segment in segments_list:
                    segment = segment.strip().replace('\n', '').split('-') # Separate "key value".
                    

                    speaker = segment[0].strip()
                    if '#' in speaker: # To comments.
                        speaker = speaker[:speaker.find('#')].strip() # Redundancy, yesssssss (To eliminate unexpected blank spaces)

                    speaker_segment = segment[1].strip()
                    if '#' in speaker_segment:
                        speaker_segment = speaker_segment[:speaker_segment.find('#')].strip()

                    speaker_segment = speaker_segment.split('>')


                    if info_dict['timeType'] == 'h:m:s':
                        from_segment = speaker_segment[0].strip().split(':') # From time.
                        from_h = int(from_segment[0]) * 3600 # Hours to seconds
                        from_m = int(from_segment[1]) * 60 # Minutes to seconds
                        from_s = int(from_segment[2]) # Seconds
                        from_abs = from_h + from_m + from_s

                        to_segment = speaker_segment[1].strip().split(':') # To time.
                        to_h = int(to_segment[0]) * 3600 # Hours to seconds
                        to_m = int(to_segment[1]) * 60 # Minutes to seconds
                        to_s = int(to_segment[2]) # Seconds
                        to_abs = to_h + to_m + to_s


                    elif info_dict['timeType'] == 'm:s':
                        from_segment = speaker_segment[0].strip().split(':') # From time.
                        from_m = int(from_segment[0]) * 60 # Minutes to seconds
                        from_s = int(from_segment[1]) # Seconds
                        from_abs = from_m + from_s

                        to_segment = speaker_segment[1].strip().split(':') # To time.
                        to_m = int(to_segment[0]) * 60 # Minutes to seconds
                        to_s = int(to_segment[1]) # Seconds
                        to_abs = to_m + to_s



                    elif info_dict['timeType'] == 's':
                        from_segment = speaker_segment[0].strip().split(':') # From time.
                        from_s = int(from_segment[0]) # Seconds
                        from_abs = from_s

                        to_segment = speaker_segment[1].strip().split(':') # To time.
                        to_s = int(to_segment[0]) # Seconds
                        to_abs = to_s

                    else:
                        raise TimeTypeError()

                    if speaker in info_dict['entities']:
                        tuple_list.append({speaker: (from_abs, to_abs)})
                    else:
                        print(f'WARNING: We found an unknown speaker ({speaker}), it will not be added to the list of segments.\n')



        if len(tuple_list) >= 1: # At least one segment found in the file.
            audio_clip = AudioFileClip(self.extract_queue[index])
            rate = audio_clip.fps
            for segment_c, segment_time in enumerate(tuple_list):
                segment_values = list(segment_time.values())[0]
                from_v = segment_values[0]
                to_v = segment_values[1]
                speaker = list(segment_time.keys())[0]
                
                clip = audio_clip.subclip(from_v, to_v) # Cut clip!!!
                clip_route_dir = f'{os.path.abspath(self.save_route)}/{self.dataset_name}-Clips'
                try:
                    os.mkdir(f'{clip_route_dir}')
                except:
                    pass

                clip_route_file = f'{clip_route_dir}/{speaker}-{segment_c}-{self.dataset_name}-Clip.mp3'
                clip.write_audiofile(clip_route_file) # SAVE CLIP!!!!

            clip.close() # Close file.

        print('\nSegmentation completed\n')



class GenerateDataset:
    """Generates datasets based on multimedia content from the Internet. 
    """    

    def __init__(self) -> None:
        self.format_yt_dlp = 'worst[height>144]' # Config of YT-DLP
        self.save_route = './'
        self.dataset_name = 'MyDataset'
        self.audio_bitrate = '20k'


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
                
                extract.to_audio(remove_original = delete_original, audio_bitrate = self.audio_bitrate)
                print('TheWildTool: The audio dataset has been generated!!!!')