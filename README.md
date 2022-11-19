
#  The Wild Tool. (Summary and Docs)

*Downtool is an open sources project developed mainly in python. Currently (November 2022) it is under development, therefore, you may encounter options that are not there or that are buggier than GTA the trilogy when it came out.*

  
  

##  Summary

TheWildTool is a tool developed with the main objective of saving time when working with audio datasets. Either to prepare them (segmentation of your raw audio and more), to get them (get content from the internet like YouTube and more) or to train a model with them (train a model with your dataset created with the above and more).

  

As already said, TheWildTool covers all these sections to have your space much tidier and cleaner. Only a few libraries are sometimes necessary.

  
  
  

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

  

-- ProccessAudio | ***type: class***

  
  

***Import:***

```python

from TheWildTool.WorkData import ProccessAudio

  

audiop =  ProdcessAudio()

```

  
  

***Methods:***

  

-  **...add_to_queue:**

```python

ProccessAudio.add_to_queue(route_files:  list)

```

-  ***route_files:*** list of audio file paths. **(.wav)**

*Add your audios to the list, and then work with them.*

  
  

-  **...listen:**

```python

ProccessAudio.listen(index:  int)

```

-  ***index:*** Index of element belonging to extract_queue.

*Show audio in a notebook.*

  
  

-  **...view:**

```python

ProccessAudio.view(index:  int,  grid  =  False,  save  =  False,  image_size  =  (20,  10),  **kwargs)

```

-  ***index:*** Index of element belonging to extract_queue.

-  ***grid*** (bool, optional): Activate or deactivate the grid of your chart. Defaults to False.

-  ***save*** (bool, optional): Save the graph in its save_route. Defaults to False.

-  ***image_size*** (tuple, optional): Image size (it is not presented in pixels. It is useful to download this if you don't have a good graphic). Defaults to (20, 10).

-  *****kwargs*** (optional).

  
  

*It generates a graph that represents the decibels of your audio over time.*

![AudioProccess Example](https://i.imgur.com/Z9LgW2p.png)

  
  






##  **VideoExtract:**

*Extract audio from video files.*

  

-- VideoExtract | ***type: class***

  
  

***Import:***

```python

from TheWildTool.WorkData import VideoExtract

  

videos =  VideoExtract()

```

  
  

***Methods:***

  

-  **...add_to_queue:**

```python

ProccessAudio.add_to_queue(route_files:  list)

```

-  ***route_files:*** list of audio file paths. **(.wav)**

*Add your audios to the list, and then work with them.*

  
  

-  **...to_audio:**

```python

ProccessAudio.to_audio(remove_original  =  True, audio_fps = 6)

```

-  ***remove_original:(boolm optional)*** After conversion, delete the video.
- ***audio_fps (int, optional):*** Frequency at which you want to save the audio. Remember: higher frequency, higher quality, but therefore, higher weight.

*Extract the audio from the video.*

  
  


  

##  **GenerateDataset**

*Generates datasets based on multimedia content from the Internet.*

  

-- GenerateDataset | ***type: class***

  
  

***Import:***

```python

from TheWildTool.WorkData import GenerateDataset

  

dataset =  GenerateDataset()

```

  
  

***Methods:***

  

-  **...youtube:**

```python

GenerateDataset.youtube(playlist: str, delete_original  = True, video_mode  = False)

```

-  ***playlist (str):*** Playlist URL.
- ***delete_original (bool, optional):*** If video mode is false, the video file are removed.
- ***video_mode (bool, optional):*** It will generate a video dataset. It maximizes the "medium" video quality, where it is not so low, but enough to train a model (maybe even very high). 3 hours of video usually weighs 150mb's.


*Generate a dataset based on a youtube playlist.*

  
***

  

[-----> More Examples Here <-----](https://colab.research.google.com/drive/1ewrPBijlpl3YSqPT6Io5Ho8X1W2Kylkx?usp=sharing) Google Colab

  

***

***

  
  

#  ***¿Some error? Contact me***

  
  

[![Contact Twitter](https://img.shields.io/badge/Twitter-ElHaban3ro-9cf.svg?style=for-the-badge&logo=twitter)](https://twitter.com/ElHaban3ro)

  

[![Contact Discord](https://img.shields.io/badge/Discord-JOIN_TO_MY_DISCORD_SERVER-lightblue?style=for-the-badge&logo=discord)](https://discord.gg/NGp9YbYJ8F)

  

[![Contact Discord](https://img.shields.io/badge/GitHub-ElHaban3ro-lightgray?style=for-the-badge&logo=github)](https://github.com/ElHaban3ro)