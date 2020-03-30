FROM ubuntu:18.04
RUN mkdir /actions-runner
#ENV AGENT_TOOLSDIRECTORY=/opt/hostedtoolcache
#ENV AGENT_TOOLSDIRECTORY=/actions-runner/tool_cache
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
        docker-ce \
        docker-ce-cli \
        containerd.io \
    && service docker start
RUN apt-get install -qy git

RUN useradd -ms /bin/bash runner \
    && printf "runner:runner" | chpasswd \
    && adduser runner sudo \
    && echo "runner ALL= NOPASSWD: ALL" >> /etc/sudoers

# USER runner
# CMD cd tool_cache \
#     && sudo npm install @actions/toolcache-python-ubuntu-1804-x64@3.8.21582900205
