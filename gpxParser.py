import gpxpy
import pandas as pd
from gpx_converter import Converter
import glob
import os


fileDir = 'GPX'
#change the directory to the one containing the Gpx files
os.chdir(fileDir)
#scan of the repository containing the gpx files
GPXList = glob.glob('./*.gpx')
os.chdir('..')

for GPX in GPXList:
    #Parsing of the name to keep it coherent between the two folders
    parsedGpx_path = 'ParsedGPX/' + GPX.join(GPX[2:].split('.')[:-1]) + '.csv'#supresses the .// and the extension from the file name and append the CSV extension as well as the destination folder
    print("Création de : "+parsedGpx_path)
    
    #Convert the Gpx file in a panda DataFrame
    gpxDataFrame = Converter(input_file='./'+fileDir+GPX[1:]).gpx_to_dataframe()
    #Convert the DataFrame to CSV to store it
    gpxCSV = gpxDataFrame.to_csv()

    #creation of the CSV File
    parsedGPX = open(parsedGpx_path,"w")
    parsedGPX.write(gpxCSV)
    parsedGPX.close()
    print(parsedGpx_path+' créé')