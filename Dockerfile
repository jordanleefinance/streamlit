FROM python:3.9-slim

EXPOSE 8080

WORKDIR /Github/streamlit

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY Website/stinslepicture.py ./stinslepicture.py

ENTRYPOINT ["streamlit", "run"]

CMD ["stinslepicture.py"]