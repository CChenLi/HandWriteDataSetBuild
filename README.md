# HandWriteDataSetBuild 

![example](https://user-images.githubusercontent.com/63531857/100561286-52635e00-326d-11eb-8423-5f75e2b9fb62.png)
> The above image is an example. Built by concat 6 output togather.

The script for building hand write dataset. A sub-project for Bai character dataset.


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
Then click `Start Drawing` to write  
When you finish one image, press `n` to save current and start drawing next
