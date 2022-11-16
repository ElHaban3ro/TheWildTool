from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

import os


class VideoExtract:
    """
    Extract video info.
    """

    converter_queue = []


    def __init__(self) -> None:
        self.to_format = 'MP3'
        self.dataset_name = 'MyAudioDataset'

    def __str__(self) -> str:
        return f'Converting Format: {self.to_format}'




    def add_to_queue(self, videos_route: list):

        if type(videos_route).__name__ == 'list':
            for route in videos_route:
                if os.path.isfile(os.path.abspath(route)):
                    self.converter_queue.append(os.path.abspath(route))

        else: 
            raise ValueError('(ErrorType) Only Support List.')



        
    def to_audio(self):
        if len(self.converter_queue) == 0:
            print('WARNING: The list is empty. Make sure you are adding files to the queue. You may be passing wrong urls.')

        else:
            for file_q_c, file_q in enumerate(self.converter_queue):
                clip = VideoFileClip(file_q)
                clip.subclip(1, 10)

                save_route_clip = os.path.abspath(f'./{file_q_c}-{self.dataset_name}.mp3')
                clip.write_videofile(save_route_clip)

                ffmpeg_extract_audio(save_route_clip, './test.mp3')


            




        




convert = VideoExtract()
convert.add_to_queue(['./DataRaw/TWP-CLAVERO.mp4', 'test'])


converting = convert.to_audio()


print()