from django.http import StreamingHttpResponse as stream
from .camera import Camera


camera = Camera()


def video(request):
    return stream(camera.get_stream(),
                  content_type="multipart/x-mixed-replace;boundary=frame")

