FROM python:3.5.2
RUN pip install --upgrade pip && pip install pandas==0.19.2
RUN pip uninstall numpy -y && pip install numpy==1.11.1