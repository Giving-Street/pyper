ARG python_version=3.7
FROM python:$python_version
COPY . /app/
WORKDIR /app
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install
CMD poetry run python