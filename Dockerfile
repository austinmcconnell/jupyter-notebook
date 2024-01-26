FROM jupyter/minimal-notebook

RUN pip install --upgrade pip setuptools wheel && \
    pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy
WORKDIR /notebooks
