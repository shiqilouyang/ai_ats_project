FROM harbor.classba.cn/base/python:3.7

COPY ../1/ai_ats_project /ai_ats_project


WORKDIR /ai_ats_project/app

RUN easy_install --upgrade pip

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r ./requirements.txt

EXPOSE 8080

CMD gunicorn -w16 -b 0.0.0.0:8080  --access-logfile ./log/log --worker-connections 1000 -k 'gevent' -preload  app:app
