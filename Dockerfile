FROM alephdata/followthemoney
RUN pip3 install alephclient sqlalchemy
CMD alephclient
