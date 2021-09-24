# -*- coding: UTF-8 -*-
from aip import AipSpeech
import pyaudio
import wave

input_filename = "rest-api-asr_python_audio_16k.wav"  # 麦克风采集的语音输入
input_filepath = 'D:\\谷歌下载\\'# 输入s文件的path
in_path = input_filepath + input_filename

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = '' #百度智能云申请的  APPID AK SK      https://console.bce.baidu.com/

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

'''语音识别部分'''


def Speech():
    def get_file_content(filePath):
        with open(filePath, "rb") as fp:
            return fp.read()

    keyword = client.asr(get_file_content(in_path), 'pcm', 16000, {'dev_ped': 1537})
    #print(keyword)
    print(keyword['err_no'])
    print(keyword['err_msg'])
    if keyword['err_no'] == 0:
        print(keyword['result'][0])


'''语音采集部分'''


def get_audio(filepath):
    aa = str(input("是否开始录音？   （是/否）"))
    if aa == str("是"):
        CHUNK = 256
        FORMAT = pyaudio.paInt16
        CHANNELS = 1  # 声道数
        RATE = 11025  # 采样率
        RECORD_SECONDS = 10  # 采集时间（s）
        WAVE_OUTPUT_FILENAME = filepath  # 输出文件名和路径
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*" * 10, "开始录音：请在10秒内输入语音")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*" * 10, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    elif aa == str("否"):
        exit()
    else:
        print("无效输入，请重新选择")
        get_audio(in_path)


if __name__ == '__main__':
    for i in range(1):
        get_audio(in_path)
        Speech()
