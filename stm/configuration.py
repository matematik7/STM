#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# stm/configuration.py
# 
# Holds configuration values.
# ----------------------------------------------------------------
# copyright (c) 2015 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cv2

class Configuration:
    def __init__(self):
        # file name prefix for folder or multi-image thumbnails
        self.name_prefix = ''
        
        # file name postfix for folder or multi-image thumbnails
        self.name_postfix = ''
        
        # file folder for folder or multi-image thumbnails
        self.folder = None
        
        # file format for folder or multi-image thumbnails
        # 'source' to keep original extension
        self.fileFormat = "png"
        
        # how much zooming is preffered
        self.zoominess = 0
        
        # target image size
        self.size = (100,100)
        
        # input file(s) or folder(s)
        self.input = None
        
        # parse folders recursively
        self.recursive = False
        
        # output file if specified
        self.output = None
        
        # image crop mode ('none', 'padd', 'crop', 'featured', 'smart')
        self.cropMode = 'smart'

        # color for padding mode
        self.paddColor = (255,255,255,0)
        
        # area for featured mode
        self.featured = None
        
        # allow padding in featured and smart modes
        self.allowPadd = False
        
        # mode for video thumbnails (time, "random", "random-still", 'ignore')
        self.videoMode = "random-still"

        # whether to save debug image
        self.debug = False
        
        # whether to show generated images names
        self.verbose = False
        
        # testing mode
        self.testing = False
        
        # face detection object
        self.faceCascade = None
