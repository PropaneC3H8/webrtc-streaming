FROM python:3.12

WORKDIR /app
COPY rtsp_webrtc_gateway.py requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python", "rtsp_webrtc_gateway.py"]