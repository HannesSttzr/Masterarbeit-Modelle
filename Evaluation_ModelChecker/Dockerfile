FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
    autoconf \
    bison \
    build-essential \
    clang \
    cmake \
    curl \
    cvc4 \
    cython3 \
    flex \
    gawk \
    git \
    gperf \
    graphviz \
    default-jre \
    libboost-filesystem-dev \
    libboost-python-dev \
    libboost-system-dev \
    libffi-dev \
    libgmp3-dev \
    libreadline-dev \
    nano \
    pkg-config \
    python3 \
    python3-pip \
    sudo \
    tar \
    tcl-dev \
    time \
    wget \
    xdot \
    zlib1g-dev

# Create download folder
RUN mkdir /home/downloads

# Get nuXmv
RUN wget https://es-static.fbk.eu/tools/nuxmv/downloads/nuXmv-2.0.0-linux64.tar.gz -O /home/downloads/nuXmv-2.0.0-linux64.tar.gz
RUN tar -xvzf /home/downloads/nuXmv-2.0.0-linux64.tar.gz -C /home

# Get NuSMV
RUN wget https://nusmv.fbk.eu/distrib/NuSMV-2.6.0-linux64.tar.gz -O /home/downloads/NuSMV-2.6.0-linux64.tar.gz
RUN tar -xvzf /home/downloads/NuSMV-2.6.0-linux64.tar.gz -C /home

# Get PdTRAV
RUN wget http://fmgroup.polito.it/quer/research/tool/pdtrav-2.5.tar.gz -O /home/downloads/pdtrav-2.5.tar.gz
RUN tar -xvzf /home/downloads/pdtrav-2.5.tar.gz -C /home

# Get BTOR2Tools
WORKDIR /home
RUN git clone https://github.com/Boolector/btor2tools.git
WORKDIR /home/btor2tools
RUN git checkout b8456dda4780789e882f5791eb486f295ade4da4
RUN ./setup-deps.sh
RUN ./configure.sh --btor2aiger
WORKDIR /home/btor2tools/build
RUN make

# Get Aiger
WORKDIR /home
RUN git clone https://github.com/arminbiere/aiger.git
WORKDIR /home/aiger
RUN git checkout 5f8ce5ca5fc42a06e5d713309f99195a740ac2b4
RUN ./configure.sh && make

# Get Yosys
WORKDIR /home
RUN git clone https://github.com/YosysHQ/yosys.git
WORKDIR /home/yosys
RUN git checkout 5c7a1eda92269aaad372a662b0e32758b2a4e014
RUN make

# Get Boolector
WORKDIR /home
RUN git clone https://github.com/Boolector/boolector.git
WORKDIR /home/boolector
RUN git checkout 4fe47dd5a6ef91df6dca4bad81326f992dc3fbab
RUN ./contrib/setup-lingeling.sh
RUN ./contrib/setup-cadical.sh
RUN ./contrib/setup-cms.sh
RUN ./contrib/setup-picosat.sh
RUN ./contrib/setup-btor2tools.sh
RUN ./configure.sh 
WORKDIR /home/boolector/build
RUN make

# Get AVR
RUN ln -s /usr/bin/python3 /usr/bin/python
WORKDIR /home
RUN git clone https://github.com/aman-goel/avr.git
WORKDIR /home/avr
RUN git checkout 92362931700b66684418a991d018c9fbdbebc06f
RUN chmod -R u+r+x /home/avr
RUN ./build.sh

# Get ABC
WORKDIR /home
RUN git clone https://github.com/berkeley-abc/abc.git
WORKDIR /home/abc
RUN git checkout 336b41a0636a78bedf80f9d3b2db30d53ad648fc
RUN make

# Get Pono
WORKDIR /home
RUN git clone https://github.com/upscale-project/pono.git
WORKDIR /home/pono
RUN git checkout 8b2a94649f5ea1161260a611de4b49e6f5d92b98
WORKDIR /
RUN mkdir /home/pono/deps
RUN wget https://mathsat.fbk.eu/download.php?file=mathsat-5.6.8-linux-x86_64.tar.gz -O /home/downloads/mathsat.tar.gz
RUN tar -xvzf /home/downloads/mathsat.tar.gz -C /home/pono/deps --transform 's:^[^/]*:mathsat:'
WORKDIR /home/pono
RUN ./contrib/setup-smt-switch.sh --with-msat
RUN ./contrib/setup-bison.sh
RUN ./contrib/setup-flex.sh
RUN ./contrib/setup-btor2tools.sh
RUN ./configure.sh --with-msat
WORKDIR /home/pono/build
RUN make

# Setup commands
WORKDIR /
RUN ln -s /home/nuXmv-2.0.0-Linux/bin/nuXmv /usr/bin/nuXmv
RUN ln -s /home/NuSMV-2.6.0-Linux/bin/NuSMV /usr/bin/NuSMV
RUN ln -s /home/pdtrav-2.5/pdtrav /usr/bin/pdtrav
RUN ln -s /home/btor2tools/build/bin/btor2aiger /usr/bin/btor2aiger
RUN ln -s /home/aiger/aigtoaig /usr/bin/aigtoaig
RUN ln -s /home/yosys/yosys /usr/bin/yosys
RUN ln -s /home/boolector/build/bin/boolector /usr/bin/boolector
RUN ln -s /home/boolector/build/bin/btormc /usr/bin/btormc
RUN ln -s /home/abc/abc /usr/bin/abc
RUN ln -s /home/pono/build/pono usr/bin/pono

# Get models
COPY ./models /home/models

# Get models
COPY ./MasterModelle /home/MasterModelle

# Cleanup
RUN rm -r /home/downloads
WORKDIR /home