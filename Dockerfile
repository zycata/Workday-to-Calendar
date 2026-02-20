# using a single dockerfile to make one container cause it's way easier
# frontend
FROM node:24 AS build-stage
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY /backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY backend/ ./backend/

COPY --from=build-stage /app/frontend/dist ./frontend/dist
ENV PYTHONPATH=/app
EXPOSE 5100

# Start Gunicorn
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5100", "backend.api:app"]
