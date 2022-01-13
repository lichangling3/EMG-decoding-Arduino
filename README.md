# EMG-decoding-Arduino

## Introduction
The idea is to find a good setup to retrieve and measure the quality of EMG signals for further applications, for instance to control a robotic hand prosthesis based on forearm muscle contractions. The obtained results show that these Myoware sensors could be as good as the Noraxon sensors, with SNR value up to 6.8. 

## Organisation
This project is organized as follows :

- the repository **_src_** that includes several files trying to implement some signal processings and collection of the data to send to a stream outlet.
- the file **_Bachelor project report - Changling Li.pdf_** which is the report of this project that provides a full explanation of what has been done.
- the file **_collectsendEMG.py_** collects the EMG datasamples from the Arduino to send them into a stream outlet using the liblsl library. From there, any computer connected to the stream can retrieve the datasamples.
- the file **_send_bytes.py.ino_** collects the EMG datasamples from the Myoware sensors via Arduino to send them to the computer.

## How to use this project
After placing the Myoware sensors on your forearm, run the file send_bytes.py.ino in the Arduino IDE. Then, run the file collectsendEMG.py in the terminal. Once you are finished with the data collection, type Ctrl + C to stop the program.

## Libraries
- serial
- liblsl

