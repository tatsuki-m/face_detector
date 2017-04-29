#!/usr/bin/env python
# coding:UTF-8
import subprocess
from datetime import datetime

# 音声をレコードするためのクラス
class RecordVoice():
    def __init__(self):
        self.isRecording = 0
        print("init")
    def startRecording(self):
        self.isRecording = 1
        fileName = datetime.now().strftime('%Y%m%d%H%M%S')
        # subprocess.call("arecord -f cd -c 2 -D dsnoop " + fileName, shell=True)
        subprocess.call("touch " + fileName, shell=True)
    def endRecording(self):
        print("send voice to server")
        # subprocess.call("pkill arecord")
        print("remove wav from dir")
        # subprocess.call("rm *.wav")
        self.isRecording = 0
