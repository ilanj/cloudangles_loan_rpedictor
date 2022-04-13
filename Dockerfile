FROM python:3.7
WORKDIR /code/deploy
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./predictor.py /code/deploy/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]