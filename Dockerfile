FROM quay.io/jupyter/minimal-notebook:notebook-7.0.7

# Install build dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install pipenv

# Install project dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system --deploy

# Create settings directory
RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/jupyterlab_code_formatter/

# Enable/disable extensions
RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements"

WORKDIR /notebooks
