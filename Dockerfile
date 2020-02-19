FROM python:3.7-stretch
WORKDIR /benchmark
COPY benchmark.py ./
RUN pip install dicttoxml xmltodict msgpack pyyaml matplotlib numpy
CMD [ "python", "./benchmark.py" ]