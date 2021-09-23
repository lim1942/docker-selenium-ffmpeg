import time
import subprocess

from selenium import webdriver


def run_test():
    print('====')
    driver = webdriver.Firefox()
    driver.fullscreen_window()
    driver.get('https://www.huya.com/381656')
    time.sleep(50)
    driver.close()
    print('-----')


def start_recording(filepath='/usr/src/app/1.mp4', screensize='1440x900'):
    cmd = ['/usr/bin/ffmpeg', '-y', '-f', 'alsa', '-ac', '2', '-i', 'pulse',  '-f', 'x11grab', '-framerate', '15',
           '-video_size', screensize, '-i', ':99+0,0', '-c:v', 'libx264', '-preset', 'veryfast', '-b:v', '320k',
           '-maxrate', '320k', '-bufsize', '640k', '-vf', '"format=yuv420p"', '-g', '30', '-c:a', 'aac', '-b:a', '128k',
           '-ar', '44100', '-threads', '12', filepath]
    # print()
    cmd = ' '.join(cmd)
    print(cmd)
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,  stderr=subprocess.DEVNULL, shell=True)
    return proc


def stop_recording(proc):
    out, err = proc.communicate(input=b'q\n', timeout=60)
    print(out,err)
    return out, err


if __name__ == '__main__':
    print('start - record')
    proc =start_recording()
    run_test()
    print('stop - record')
    stop_recording(proc)
