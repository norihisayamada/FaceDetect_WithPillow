#This app is an image detection app using Streamlit

first of all,
It was working in my local environment,
I could not deploy Face Detect using Streamlit, so I will describe the measures I took at that time.

These problems were solved by installing opencv-python-headless==4.4.0.44 and changing the interpreter to Python3.8 when using pillow8.0.1
When using this file, the numpy package is installed by specifying the version, but it is not so important.

Please refer to 'requirements.txt' for specifying the version of each package.



reference
https://share.streamlit.io/ohmoriyusuke/trimming-opencv-streamlit/main.py
