FROM fedora:latest
RUN dnf install -y python3 python3-pip 

ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
ADD budget.xlsx main.py /.

ENTRYPOINT ["python3"]
CMD ["main.py"]