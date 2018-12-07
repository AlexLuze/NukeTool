#-*-coding:utf-8 -*-
# !/usr/bin/env python
# Author: AlexLuze
# IDE: PyCharm
# CreateTime: 2018/12/7
import os
import json
with open('config.json','r') as file:
    filePath = json.load(file)
nukePythonPath = filePath['nukePythonPath']
renderPyPath = filePath['renderPath']

filePath = 'E:/GF/comp/EP02/shot050/GFT_EP02_shot050_comp.nk'


def firstStep():
    if '/' in nukePythonPath:
        nukePath = nukePythonPath.split("/")
        renderPath = renderPyPath.split("/")
    elif '\\' in nukePythonPath:
        nukePath = nukePythonPath.replace('\\', '/')
        nukePath = nukePath.split("/")
        renderPath = renderPyPath.replace('\\', '/')
        renderPath = renderPath.split("/")
    else:
        pass
    
    new_nukePath = "'"
    for length in range(len(nukePath)):
        if length == 0:
            new_nukePath = new_nukePath + nukePath[length] + "/" + '"'
        elif length == len(nukePath) - 1:
            new_nukePath = new_nukePath + nukePath[length] + '"' + "'"
        elif length != 0 and length != len(nukePath) - 1:
            new_nukePath = new_nukePath + nukePath[length] + "/"
    
    new_renderPath = "'"
    for length in range(len(renderPath)):
        if length == 0:
            new_renderPath = new_renderPath + renderPath[length] + "/" + '"'
        elif length == len(renderPath) - 1:
            new_renderPath = new_renderPath + renderPath[length] + '"' + "'"
        elif length != 0 and length != len(renderPath) - 1:
            new_renderPath = new_renderPath + renderPath[length] + "/"
    
    final_nukePath = new_nukePath.strip("'")  # getfinal_nukePath
    
    final_renderPath = new_renderPath.strip("'")  # getfinal_renderPath
    print "final_renderPath:",final_nukePath
    print "final_renderPath：",final_renderPath

    os.system('%s %s %s' % (final_nukePath,final_renderPath,filePath) )
firstStep()