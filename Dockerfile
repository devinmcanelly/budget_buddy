FROM ubi8/python-311


COPY init.sh /init.sh
RUN ./init.sh

# Everything below here should stay the same
RUN conda install openpyxl ipython
# later pandas jupyterlab
ADD app/ /app
COPY ipython_config.py /root/.ipython/profile_default/ipython_config.py
WORKDIR /app
CMD ["ipython", "main.py"]