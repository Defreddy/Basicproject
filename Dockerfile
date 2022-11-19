FROM python:3.11.0-slim
RUN apk add build-base linux-headers
RUN python -m pip install -q --upgrade pip setuptools wheel
WORKDIR /code
EXPOSE 8000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.apicalls:app", "--host", "0.0.0.0", "--port", "8051"]
