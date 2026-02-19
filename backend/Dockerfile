FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# overengineered? Yes. Well built? uhhhh... Yes.
COPY requirements.txt . 

RUN pip install --no-cache-dir -r backend/requirements.txt 

RUN pip install gunicorn 
COPY . . 

# port to expose
EXPOSE 5100 

# because workspace is /backend/api.py it's backend.api
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5100", "api:app"]
# running from your own terminal would result in: 
# gunicorn -w 4 -b 0.0.0.0:5100 backend.api:app
# debug version would be:
# gunicorn --bind 0.0.0.0:5100 --access-logfile - --error-logfile - backend.api:app

