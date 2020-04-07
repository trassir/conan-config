FROM ubuntu:18.04
RUN mkdir /actions-runner
WORKDIR /actions-runner
RUN apt-get -q update \
    && apt-get install -qy \
        nodejs \
        npm \
        unzip \
        sudo
RUN apt-get install -qy \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
    && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable" \
    && apt-get -q update \
    && apt-get install -qy \
        docker-ce-cli
RUN apt-get install -qy git

RUN useradd -ms /bin/bash runner \
    && printf "runner:runner" | chpasswd \
    && adduser runner sudo \
    && echo "runner ALL= NOPASSWD: ALL" >> /etc/sudoers

#ENV AGENT_TOOLSDIRECTORY=/actions-runner/tool_cache
RUN echo "export AGENT_TOOLSDIRECTORY=/opt/hostedtoolcache" >> /home/runner/.bashrc

# CMD npm install @actions/toolcache-python-ubuntu-1804-x64@3.8.21582900205

# USER runner
# CMD cd tool_cache \
#     && sudo
