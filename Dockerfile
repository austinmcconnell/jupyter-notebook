FROM quay.io/jupyter/minimal-notebook:notebook-7.0.7

RUN pip install --upgrade pip setuptools wheel && \
    pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy
WORKDIR /notebooks
