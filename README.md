# HandWriteDataSetBuild 

![example](https://user-images.githubusercontent.com/63531857/100561705-6a87ad00-326e-11eb-8336-a4fdc3320f3a.jpg)
> The above image is an example output of this project. Built by concat 6 outputs togather and reverting color. Each character is collected from 
the lyric of a Bai folk song.

This project is the script for building handwriting dataset. A sub-project for Bai character dataset. 

### Before you want to contribute to this project, please contact me to get your unique **User ID** to avoid redundant work.


## Build requirement
```
pip install -r requirements.txt
```

You may need to create a data folder under main folder by
```
mkdir data
```

## Usage Example
```
python3 ./src/capture.py
```
which will pop out the window  
<img width="379" alt="Screen Shot 2020-11-29 at 5 47 29 PM" src="https://user-images.githubusercontent.com/63531857/100560527-f8619900-326a-11eb-9480-b648183128a4.png">

- label: the label of the image
- uid: your uid, to specify who made the image
- Number of images: how many images with this label you will create this time
Then click `Start Drawing` to write, which will show you the drawing window  
<img width="400" alt="Screen Shot 2020-11-29 at 6 18 11 PM" src="https://user-images.githubusercontent.com/63531857/100562022-4082ba80-326f-11eb-8e7f-7c1f6a44fd7a.png">


When you finish one image, press `n` to save current and start drawing next. 

When all images are finished, you will find all the png file in the folder `data` named as *(caution naming rule hasn't finalized)*
`<label>_<uid>_<batch>.png`

## Author
- Chen Li
- lichen@g.ucla.edu


## Acknowledgement
The picture of the Bai folk song
![example2](https://user-images.githubusercontent.com/63531857/100561835-cb16ea00-326e-11eb-894c-7cf06e0b5029.jpg)
