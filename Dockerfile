FROM python:latest
WORKDIR /users_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8081
CMD ["python", "app.py"]
