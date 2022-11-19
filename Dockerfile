FROM python:3.11.0-slim
#RUN apt-get install -y build-essential linux-headers
RUN python -m pip install -q --upgrade pip setuptools wheel
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./.env /code
CMD ["uvicorn", "app.apicalls:app", "--host", "0.0.0.0", "--port", "8051"]
CMD ["pwd"]
CMD ["ls -all"]
