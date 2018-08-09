FROM python:3
COPY requirements.txt /requirements.txt
RUN python3.5 - m pip install --upgrade pip
RUN python3.5 -m pip install -r requirements.txt
COPY start.sh /start.sh
EXPOSE 8000
CMD ["/start.sh"]
# done!
