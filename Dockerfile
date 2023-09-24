FROM python:3.11.4
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN mkdir -p /data
COPY . .
EXPOSE 5000
ENV FLASK_APP=./app/exercise_api.py
ENTRYPOINT [ "python", "./app/exercise_api.py" ]