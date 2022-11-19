from TheWildTool.WorkData import VideoExtract

extract = VideoExtract()
extract.add_to_queue([r'C:\Users\ferdh\Downloads\datatest\TWP-CLAVERO.mp4', r'C:\Users\ferdh\Downloads\datatest\TWP-ALEXELMASCAPITO.mp4'])
print(extract.converter_queue)

extract.to_audio(remove_original = False, audio_fps=6)