# from TheWildTool.WorkData import GenerateDataset

# gen = GenerateDataset()
# gen.dataset_name = 'uwu'
# gen.save_route = r'C:\Users\ferdh\Downloads\datatest'
# gen.youtube('https://www.youtube.com/playlist?list=PLOYDNc5FY_0q8i9a7akJRjU8g6LWZ2kZh', delete_original=True, video_mode = False)








# from TheWildTool.WorkData import VideoExtract

# extract = VideoExtract()
# extract.add_to_queue([r'C:\Users\ferdh\Downloads\datatest\twp-clavero.mp4'])
# extract.to_audio(remove_original = False)



# from TheWildTool.WorkData import ProccessAudio

# v = ProccessAudio()
# v.add_to_queue([r'C:\Users\ferdh\Downloads\datatest\MyAudioDataset-AudioExport\0-MyAudioDataset.mp3'])
# v.see(456)




# import os
# a =os.path.normpath(r'C:\Users\ferdh\Downloads\datatest\MyDataset/0.mp4')
# print(a)}




from TheWildTool.WorkData import ProccessAudio

v = ProccessAudio()
v.add_to_queue([r'C:\Users\ferdh\Downloads\datatest\MyAudioDataset-AudioExport\0-MyAudioDataset.mp3'])

v.segment(0, r'C:\Users\ferdh\Desktop\Projects\TheWildTool\TWP-CLAVERO-SEG.aseg')