FROM python:3.8-alpine

COPY ./requirements.txt .

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r ./requirements.txt

ENV INFRA_DATA="tofu-controller-rules!"

ENV APP_ENV="${{values.environment}}"

COPY ./src /src

EXPOSE 5000

CMD ["python3", "/src/app.py"]


