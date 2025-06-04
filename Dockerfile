FROM agnohq/python:3.12

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends software-properties-common pciutils lshw

RUN curl -fsSL https://ollama.com/install.sh | sh

ARG USER=app
ARG APP_DIR=/app

ENV APP_DIR=${APP_DIR}
ENV OLLAMA_HOME=${APP_DIR}/.ollama

# Create user and home directory
RUN groupadd -g 61000 ${USER} \
  && useradd -g 61000 -u 61000 -ms /bin/bash -d ${APP_DIR} ${USER} \
  && echo "${USER}:1234" | chpasswd \
  && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR ${APP_DIR}

# Copy requirements.txt
COPY requirements.txt ./

# Install requirements
RUN uv pip sync requirements.txt --system

# Copy project files
COPY . .

# Set permissions for the /app directory
RUN chown -R ${USER}:${USER} ${APP_DIR}

# Set permissions for the .ollama directory
RUN mkdir -p ${APP_DIR}/.ollama && chown -R ${USER}:${USER} ${APP_DIR}/.ollama

RUN chmod +x /app/scripts/prod/ollama_setup.sh && /app/scripts/prod/ollama_setup.sh

# Switch to non-root user
USER ${USER}

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["chill"]
