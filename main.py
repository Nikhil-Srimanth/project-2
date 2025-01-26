from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
import threading
import cv2
from ultralytics import YOLO
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech rate

def announce_object(predictions):
    if predictions:
        message = f"You have a {', '.join(predictions)} in front of you."
        
        # Use pyttsx3 to announce the message
        engine.say(message)
        engine.runAndWait()

def object_detection_yolo(video_source, frame_callback, stop_event):
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        return

    last_announced = set()

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detected_objects = set()

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = int(box.cls[0])
                detected_objects.add(model.names[cls])
                label = f"{model.names[cls]}: {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        frame_callback(frame)

        new_objects = detected_objects - last_announced
        if new_objects:
            threading.Thread(target=announce_object, args=(list(new_objects),)).start()
            last_announced.update(new_objects)

    cap.release()

class StartButton(Button):
    pass

class StopButton(Button):
    pass

class ObjectDetectionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        
        self.image = Image()  # Image widget for displaying camera preview
        
        self.start_button = StartButton(text="Start Detection", on_press=self.start_detection)
        self.stop_button = StopButton(text="Stop Detection", on_press=self.stop_detection)
        
        self.stop_button.disabled = True  
        
        self.layout.add_widget(self.image)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.stop_button)

        self.video_source = 0  # Camera index
        self.stop_event = threading.Event() 

        return self.layout

    def start_detection(self, instance):
        self.start_button.disabled = True
        self.stop_button.disabled = False

        threading.Thread(target=self.run_object_detection, daemon=True).start()

    def stop_detection(self, instance):
        self.stop_event.set()
        
        self.start_button.disabled = False
        self.stop_button.disabled = True

    def run_object_detection(self):
        object_detection_yolo(self.video_source, self.update_frame, self.stop_event)

    def update_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        frame_rgb = cv2.flip(frame_rgb, 0)  # 1 flips the frame horizontally
        

        Clock.schedule_once(lambda dt: self.update_image_texture(frame_rgb))

    def update_image_texture(self, frame):
        from kivy.graphics.texture import Texture
        height, width, _ = frame.shape
        texture = Texture.create(size=(width, height), colorfmt='rgb')
        texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        self.image.texture = texture

if __name__ == "__main__":
    ObjectDetectionApp().run()
