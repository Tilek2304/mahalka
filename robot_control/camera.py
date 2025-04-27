import cv2
from django.http import StreamingHttpResponse

# class VideoCamera:
#     def __init__(self):
#         self.cap = cv2.VideoCapture(0)
    
#     def get_frame(self):
#         success, image = self.cap.read()
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

# def video_feed(request):
#     return StreamingHttpResponse(
#         gen(VideoCamera()),
#         content_type='multipart/x-mixed-replace; boundary=frame'
#     )

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

class VideoCamera:
    def __init__(self):
        # Для USB камеры
        self.cap = cv2.VideoCapture(0)
        
        # Для Raspberry Pi Camera Module
        # self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)