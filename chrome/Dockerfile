FROM selenium/node-chrome:4.0.0-rc-2-prerelease-20210916

ENV TZ Asia/Shanghai

USER root

RUN apt-get -qqy update
RUN apt-get -qqy install ffmpeg
RUN apt-get -qqy install pip

USER 1200

# 界面 和 vnc配置,vnc连接密码为 secret
ENV SCREEN_WIDTH 1360
ENV SCREEN_HEIGHT 1020
ENV SCREEN_DEPTH 24
ENV SCREEN_DPI 96
ENV DISPLAY :99.0
ENV DISPLAY_NUM 99
ENV START_XVFB true
ENV START_NO_VNC true

# 复制代码文件安装python依赖
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/

# 复制项目启动脚本到supervisord
COPY start-selenium-node.sh /opt/bin/
