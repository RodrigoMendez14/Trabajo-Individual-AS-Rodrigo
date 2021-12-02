FROM ubuntu

RUN apt -qq update && apt -qq -y install python3 && apt -qq -y install python3-pip && pip install mysql-connector && mkdir /appAS && apt -qq upgrade 

#RUN apt -qq -y install apt-utils && apt -qq -y install software-properties-common && apt -qq -y install gnupg && apt -qq -y install curl && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" && apt-get -qq -y update && apt -qq -y install docker-ce

COPY ./main_Rodrigo_AS.py /appAS 

CMD python3 /appAS/main_Rodrigo_AS.py
