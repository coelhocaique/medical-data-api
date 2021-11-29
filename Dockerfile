FROM python:3.9.9

ADD src /app

RUN pip install sqlalchemy

RUN pip install psycopg2-binary

RUN pip install fastapi

RUN pip install "uvicorn[standard]"

RUN rm /usr/bin/X11/X11

CMD [ "python3", "app/main.py" ]