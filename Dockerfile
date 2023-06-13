
FROM python:3.10.6

ADD main.py .
ADD data_manager.py .
ADD flight_data.py .
ADD flight_search.py .

RUN pip install datetime requests mysql-connector-python

CMD ["python", "./main.py"]