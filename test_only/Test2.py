import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Load the data

list_file = [file for file in glob.glob('Input' + './*.{}'.format('csv'))]
filenames = [os.path.splitext(os.path.basename(filepath))[0] for filepath in list_file] # splitext() return (filename, extension)
