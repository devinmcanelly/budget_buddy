FROM quay.io/devinmcanelly/pydevbase 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD app/ /app
COPY ipython_config.py /root/.ipython/profile_default/ipython_config.py
WORKDIR /app
RUN chmod -R 777 /app
CMD ["ipython", "main.py"]