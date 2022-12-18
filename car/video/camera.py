import cv2
import os


face_cascade_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(face_cascade_file)


class Camera:

    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
  
    def _add_faces(self, image):
        """Detect and highlight faces in an image."""
        return # Disabled due to low computing power on the Pi
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    def _get_frame(self):
        success, image = self.video.read()
        if not success:
            print('Cannot read from video camera.')
            return False
        self._add_faces(image)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tostring()

    def get_stream(self):
        while True:
            frame = self._get_frame()
            if frame:
                yield(b'--frame\n'
                    b'Content-Type: image/jpeg\n\n' + frame + b'\n\n')
