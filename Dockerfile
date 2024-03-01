FROM python:3.13.0a4-slim
# Or any preferred Python version.

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./setup.sh /code/setup.sh

RUN chmod +x setup.sh

RUN ./setup.sh

COPY ./app /code/app

CMD ["python", "/code/app/convert.py"]