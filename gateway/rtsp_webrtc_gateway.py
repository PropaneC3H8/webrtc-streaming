import asyncio
import json
import os
from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.signaling import TcpSocketSignaling
import cv2
import numpy as np
from av import VideoFrame

class VideoStreamTrack(MediaStreamTrack):
    kind = "video"

    def __init__(self, rtsp_url):
        super().__init__()
        self.cap = cv2.VideoCapture(rtsp_url)

    async def recv(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                await asyncio.sleep(1/30)
                continue

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV_I420)
            video_frame = VideoFrame.from_ndarray(frame, format='yuv420p')
            video_frame.pts = None
            video_frame.time_base = "1/30"
            return video_frame

async def run():
    rtsp_url = os.getenv("CAMERA_RTSP_URL", "rtsp://rtspstream.com/parking")
    signaling = TcpSocketSignaling('signaling', 9001)

    await signaling.connect()
    offer = await signaling.receive()

    pc = RTCPeerConnection()
    pc.addTrack(VideoStreamTrack(rtsp_url))

    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    await signaling.send(pc.localDescription)
    await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(run())