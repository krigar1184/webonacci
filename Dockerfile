FROM python:3.7

ENV PROJECT_ROOT /usr/src/app

WORKDIR $PROJECT_ROOT

# Install poetry
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY pyproject.toml $PROJECT_ROOT

RUN $HOME/.poetry/bin/poetry config settings.virtualenvs.create false
RUN $HOME/.poetry/bin/poetry install

COPY . /usr/src/app
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
