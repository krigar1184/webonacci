FROM python:3.7 as local
ENV PROJECT_ROOT /usr/src/app
WORKDIR $PROJECT_ROOT

# Install poetry
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
COPY pyproject.toml $PROJECT_ROOT
RUN $HOME/.poetry/bin/poetry config settings.virtualenvs.create false
RUN $HOME/.poetry/bin/poetry install


FROM python:3.7 as test
ENV PROJECT_ROOT /usr/src/app
WORKDIR $PROJECT_ROOT

# Install poetry
RUN apt-get -y update && \
    apt-get -y --no-install-recommends install curl
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
COPY pyproject.toml $PROJECT_ROOT
RUN $HOME/.poetry/bin/poetry config settings.virtualenvs.create false
RUN $HOME/.poetry/bin/poetry install
COPY . $PROJECT_ROOT

CMD pytest
