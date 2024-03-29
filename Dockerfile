# ARG PYTHON_VERSION=3.11-slim-bullseye

# FROM python:${PYTHON_VERSION}

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN mkdir -p /code

# WORKDIR /code

# COPY requirements.txt /tmp/requirements.txt
# RUN set -ex && \
#     pip install --upgrade pip && \
#     pip install -r /tmp/requirements.txt && \
#     rm -rf /root/.cache/

# COPY funderfest/ /code/

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "funderfest.wsgi"]


ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1RUN mkdir -p /code

WORKDIR /code
COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \    
    rm -rf /root/.cache/

COPY funderfest/ /code/

RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
CMD ["/code/run.sh"]