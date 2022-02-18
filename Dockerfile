ARG IMAGE=python
ARG TAG=3.9.10-slim

FROM ${IMAGE}:${TAG}

RUN apt-get update && apt-get install -y --no-install-recommends \
    # Required to build python packages
    build-essential

RUN \
    # Upgrade pip
    pip3 install --upgrade pip && \
    # Install poetry
    pip3 install "poetry==1.1.13" && \
    # Disable the virtualenv
    poetry config virtualenvs.create false && \
    # Create code staging folder
    mkdir -p /code && \
    # Create a data staging folder
    mkdir -p /mnt/data

# Set the current working directory
WORKDIR /code

# Copy the python project dependency file
COPY ["./pyproject.toml", "./"]

# Resolve and install poetry dependencies
RUN poetry install

# Copy the application into the container
COPY ./ ./

# Run the python script
CMD python main.py


