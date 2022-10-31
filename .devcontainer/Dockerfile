FROM mcr.microsoft.com/vscode/devcontainers/python:3.10-buster

USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$PATH:$HOME/.local/bin"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PYTHONUNBUFFERED 1

COPY --chown=vscode . .