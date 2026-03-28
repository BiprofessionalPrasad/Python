# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:50:56 2019

@author: pgaiton
"""
import os

path = 'C:/Users/pgaiton/Videos/'
os.chdir(path)

from moviepy.editor import *

clip = VideoFileClip("SampleVideo_1280x720_1mb.mp4")
clip.write_gif("1.gif")