import os
import shutil

import pandas as pd

from xml.dom import minidom
from collections import Counter

from pandas.core.indexes.base import Index

dirpath = r"./data"
savepath = r"./slice_data"


# 获取xml文件中信息
def readXml(path):
    doc = minidom.parse(path)
    
    result = []
    name = doc.getElementsByTagName("name")

    for nodelist in name:
        for node in nodelist.childNodes:
            result.append(node.data)
    return list(set(result))

def saveImgXml(labels, xmlPath, imgPath):
    for label in labels:
        saveDir = os.path.join(savepath,label)
        xml = os.path.join(saveDir, xmlPath.split("\\")[-1])
        img = os.path.join(saveDir,imgPath.split("\\")[-1]) 
        print(xml)
        if os.path.exists(saveDir):
            pass
        else:
            os.mkdir(saveDir)
        shutil.copy(xmlPath, xml)
        shutil.copy(imgPath, img)




for root, dirs, files in os.walk(dirpath):
    for file in files:
        if file.endswith("xml"):
            xmlPath = os.path.join(root,file)
            imgPath = xmlPath.replace("xml","jpg")
            labels = readXml(xmlPath)
            saveImgXml(labels, xmlPath, imgPath)
        else:
            continue