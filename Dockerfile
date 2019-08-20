FROM python
RUN apt-get update && \
  apt-get install sqlite3 -y && \
  apt-get install vim -y
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir numpy && \
    pip install --no-cache-dir Django && \
    pip install --no-cache-dir -r requirements.txt && \
    pip uninstall -y numpy  && \
    pip install numpy
COPY . .
RUN mkdir /usr/src/app/log 
RUN python /usr/src/app/manage.py migrate
RUN pip install --no-cache-dir rasa
RUN rasa init --no-prompt
ENTRYPOINT [ "python","/usr/src/app/manage.py" ]

