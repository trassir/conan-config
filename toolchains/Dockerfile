# inspired by https://github.com/conan-io/conan-docker-tools/blob/master/gcc_9/Dockerfile

FROM ubuntu:eoan

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH} \
    CC=gcc-9 \
    CXX=g++-9

RUN dpkg --add-architecture i386

# various system tools
RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
        sudo \
        git \
        curl \
        wget \
        ca-certificates \
        zlib1g:i386 # for running the arm-gcc/arm-as itself

# python build requirements
RUN apt-get -qq install -y --no-install-recommends \
    g++-9-multilib \
    make \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    ninja-build \
    libssl-dev \
    libffi-dev \
    libsqlite3-dev

RUN groupadd 1001 -g 1001 \
    && useradd -ms /bin/bash conan -g 1001 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

RUN wget --no-check-certificate --quiet https://cmake.org/files/v3.16/cmake-3.16.4-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.16.4-Linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-3.12/Help \
    && cp -fR cmake-3.16.4-Linux-x86_64/* /usr \
    && rm -rf cmake-3.16.4-Linux-x86_64 \
    && rm cmake-3.16.4-Linux-x86_64.tar.gz



RUN wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.5 \
    && pyenv global 3.7.5 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan/profiles \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc

# TODO: conan config install
COPY config/profiles/hi3520dv300 /home/conan/.conan/profiles/hi3520dv300
