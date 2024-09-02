FROM python:3.11.9-alpine3.20

WORKDIR /code

COPY . /code/
COPY src/fishmlserv/main.py /code/
COPY requirements.txt /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN git install git+


CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8949"]
