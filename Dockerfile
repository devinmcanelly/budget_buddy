FROM continuumio/miniconda3
RUN conda install openpyxl pandas jupyterlab
ADD budget.xlsx app.py .
ENTRYPOINT ["/bin/bash"] 