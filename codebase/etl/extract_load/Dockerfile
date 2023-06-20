FROM public.ecr.aws/lambda/python:3.9-arm64
# FROM python:3.9
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./src/ ./src
COPY ./main.py ./main.py
COPY .env .
COPY ./settings.py ./settings.py

CMD ["main.lambda_handler"]