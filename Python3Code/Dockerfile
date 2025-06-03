FROM --platform=linux/amd64 ubuntu:20.04
FROM --platform=linux/amd64 python:3.8.8

RUN apt-get update
RUN apt-get install sudo
RUN apt-get install git -y

COPY requirements.txt /src/requirements.txt
COPY requirements.txt /src/requirements_git.txt

RUN apt-get install python3-pip -y
RUN pip3 install pip --upgrade
RUN pip3 install Cython

RUN xargs -L 1 pip3 install < /src/requirements.txt
RUN xargs -L 1 pip3 install < /src/requirements_git.txt

WORKDIR /root
RUN python3 --version

# Copy project files (optional - you can also use volume mounting)
# COPY . /root/

# Set bash as the default command instead of Python CLI
CMD ["/bin/bash"]

