FROM ubuntu

RUN apt -qq update && apt -qq -y install python3 && apt -qq -y install python3-pip && pip install mysql-connector && mkdir /appAS && apt -qq upgrade 

COPY ./main_Rodrigo_AS.py /appAS 

CMD python3 /appAS/main_Rodrigo_AS.py
