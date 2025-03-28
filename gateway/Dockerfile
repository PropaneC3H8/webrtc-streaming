FROM python:3.12

WORKDIR /app
COPY rtsp_webrtc_gateway.py requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxt6 \
    libxrender1 \
    libxi6 \
    libglu1-mesa

CMD ["python", "rtsp_webrtc_gateway.py"]