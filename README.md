# GUI Demo of Image Scrolling
## Description
This is another exercise in PyQt5 I came up with to practice displaying many images in a GUI in such a way that I could scroll through them all at once. This project contains nothing more than that, and was created purely as a proof-of-concept for myself that I could easily reimplement later down the line.

Instead of creating many labels within the QScrollArea widget or trying to manage the display of multiple images, I took all the images I wanted and concatenated them into image. I was having trouble using this all-in-one image that I had preprocessed to be displayed in the Scroll widget so I ended up saving it to disk and re-reading it by suppling it's path as input to a QPixmap widget. I couldn't figure out how to convert it to a QPixmap or QImage straight from the ndarray format. 

Pictures sampled are from houses dataset: https://github.com/emanhamed/Houses-dataset

![Screenshot of GUI](https://raw.githubusercontent.com/cehusted/GUI-image-scroll/master/House_scroll.PNG)

### To get this running:
* Download both .py files, put in same directory
* pip install the PySide2 package
* Open command prompt to directory, type "python scroll-image-test.py"
