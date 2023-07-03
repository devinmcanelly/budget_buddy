FROM continuumio/miniconda3
RUN conda install openpyxl ipython
# later pandas jupyterlab 
ADD app/ /app
WORKDIR /app
RUN chmod -R 777 /app
CMD ["ipython", "main.py"] 
