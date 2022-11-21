
  

#  The Wild Tool. (Summary and Docs)

  

*Downtool is an open sources project developed mainly in python. Currently (November 2022) it is under development, therefore, you may encounter options that are not there or that are buggier than GTA the trilogy when it came out.*

  


[![License: MIT](https://img.shields.io/badge/License-MIT-yellowgreen.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-310/) [![PyPi Package](https://img.shields.io/badge/PyPi_Package-pip_install_MovieTool-yellow.svg?style=flat-square&logo=pypi)](https://pypi.org/project/TheWildTool/) [![GitGub Repositorie](https://img.shields.io/badge/GitHub_Repositorie-MovieTool-gray.svg?style=flat-square&logo=github)](https://github.com/ElHaban3ro/TheWildTool/)
  

##  Summary

  

TheWildTool is a tool developed with the main objective of saving time when working with audio datasets. Either to prepare them (segmentation of your raw audio and more), to get them (get content from the internet like YouTube and more) or to train a model with them (train a model with your dataset created with the above and more).

  

As already said, TheWildTool covers all these sections to have your space much tidier and cleaner. Only a few libraries are sometimes necessary.

  

TheMovieTool makes use of FFMPEG, therefore, for scalability, our repository and package already comes with it. We will update it as we update the tools.

  

  

##  Classes Summary

  

-  ***ProccessAudio:*** It processes the audio to obtain different types of information in order to train a model.

-  ***GenerateDataSet:*** Generate extraid datasets of key sites!

-  ***VideoExtract:*** Process your videos into audio.

  

  

##  Installation

- Using pypi:
```bash
pip install TheWildTool
```

or clonning repository (no recommended)

  

```bash
git clone https://github.com/ElHaban3ro/TheWildTool
```

and installing the dependencies
```bash
py -m pip install -r TheWildTool/requirements.txt
```

  

  

##  TheWildTool Origin

  

*Comming Soon...*

  

  

***

  

  

#  Documents

  

##  **ProccessAudio:**

  

*Processes the audios and operates with them.*

  

  

> ProccessAudio | <type: class>

***Import:***
```python
from TheWildTool.WorkData import ProccessAudio
audiop =  ProdcessAudio()
```


***Methods:***

  

  

- >  **add_to_queue**

	*Add your audios to the list, and then work with them.*
	```python
	ProccessAudio.add_to_queue(route_files:  list)
	```
	-  ***route_files:*** list of audio file paths. **(.mp3)**

  

  

- > **queue_to_array**

	*Transforms the tail array into numpy arrays. If you do not process the audios with this method you will not be able to see to them.*
	```python
	ProccessAudio.queue_to_array()
	```


-  > **listen**

	*Show audio in a notebook.*
	```python
	ProccessAudio.listen(index:  int)
	```
	-  ***index:*** Index of element belonging to extract_queue.


-  > **see**

	*It generates a graph that represents the decibels of your audio over time.*
	```python
	ProccessAudio.see(index:  int,  grid  =  False,  save  =  False,  image_size  =  (20,  10),  **kwargs)
	```
	-  ***index:*** Index of element belonging to extract_queue.

	-  ***grid*** (bool, optional): Activate or deactivate the grid of your chart. Defaults to False.

	  

	-  ***save*** (bool, optional): Save the graph in its save_route. Defaults to False.

	  

	-  ***image_size*** (tuple, optional): Image size (it is not presented in pixels. It is useful to download this if you don't have a good graphic). Defaults to (20, 10).

	-  *****kwargs*** (optional).

![AudioProccess Example](https://i.imgur.com/Z9LgW2p.png)

- > ***segment***

  Cut a long audio into small segments that you use to train a model or whatever else you decide. 
	```python
	ProccessAudio.segment(index:int, segment_file:str)
	```
	- ***index (int):*** Index of your element in the queue.

	- ***segment_file (str):*** Path of the segmentation file for that mp3 file in the list.

	To do the segmentation we make use of a file with a certain syntax to standardize the segmentation. Here is how the file would look like ```myVideo.aseg```
		
	```
	[DATASET NAME][list, of, persons, that, is, in, the, audio][time_type: h:m:s, m:s, s][Video Name]
	# Comment with "#"


	! Eminem # "!" Instance of speaker.
	- 00:00:25 > 00:01:03 # Segment time to speaker.
	```
	
	***a example? oki:***
	
	```
	[TheWildProject Dataset][Jordi, Nacho, Other][h:m:s][TWP Clavero]

	! Jordi
	- 00:00:13 > 00:01:27

	! Nacho
	- 00:01:30 > 02:23:56 # (hace el podcast!! 😱 xd)
	```
  

##  **VideoExtract:**
*Extract audio from video files.*

  

  

> VideoExtract | ***<type: class>***
> 
***Import:***
```python
from TheWildTool.WorkData import VideoExtract
videos =  VideoExtract()
```

***Methods:***

- > **add_to_queue**

	*Add your audios to the list, and then work with them.*
	```python
	ProccessAudio.add_to_queue(route_files:  list)
	```
	-  ***route_files:*** list of audio file paths. **(.mp3)**

  

-  > **to_audio**

	*Extract the audio from the video.*
	```python
	ProccessAudio.to_audio(remove_original  =  True,  audio_bitrate  =  '10k')
	```
	-  ***remove_original:(boolm optional)*** After conversion, delete the video.

	-  ***audio_bitrate (str, optional):*** String of the amount of bitrate your audio has. The string should be something like "50k", "777k" or "5k", but keep in mind that more Bitrate represents more weight in the file (but more quality).

  


  

##  **GenerateDataset**
*Generates datasets based on multimedia content from the Internet.*

  

> GenerateDataset | ***<type: class>***

***Import:***
```python
from TheWildTool.WorkData import GenerateDataset
dataset =  GenerateDataset()
```

***Methods:***

-  > **youtube**

	*Generate a dataset (obviously not prepared) based on a youtube playlist.*

	```python
	GenerateDataset.youtube(playlist:  str,  delete_original  =  True,  video_mode  =  False)
	```
	-  ***playlist (str):*** Playlist URL.

	-  ***delete_original (bool, optional):*** If video mode is false, the video file are removed.

	-  ***video_mode (bool, optional):*** It will generate a video dataset. It maximizes the "medium" video quality, where it is not so low, but enough to train a model (maybe even very high). 3 hours of video usually weighs 150mb's.

  
  



  

***

  

  

[-----> More Examples Here <-----](https://colab.research.google.com/drive/1ewrPBijlpl3YSqPT6Io5Ho8X1W2Kylkx?usp=sharing) Google Colab

  

  

***

  

***

  

  

#  ***¿Some error? Contact me***

  

  

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro)

  

  

[![Contact Discord](https://img.shields.io/badge/Discord-JOIN_TO_MY_DISCORD_SERVER-lightblue?style=for-the-badge&logo=discord)](https://discord.gg/NGp9YbYJ8F)

  

  

[![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)