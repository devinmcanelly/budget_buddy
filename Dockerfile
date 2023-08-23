FROM localhost/pydevbase 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD app/ /app
WORKDIR /app
RUN chmod -R 777 /app
CMD ["ipython", "main.py"]
