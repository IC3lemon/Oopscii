import cv2
import time
from oops import *

def frame_to_pil(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(frame_rgb)

def stream_webcam_to_ascii():
    START = time.time()
    cap = cv2.VideoCapture(0)  
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Oopsie, Failed to open webcam.")
        return

    fps = 16
    delay = 1.0 / fps

    try:
        while True:
            start = time.time()
            ret, frame = cap.read()
            
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            pil_image = frame_to_pil(frame)
            ascii_output = textify(pil_image)

            os.system('cls')
            print(f'समय : {time.time() - START}')
            print(ascii_output)
            print('scroll up nigga, and dont resize, it fucks shit up')
            elapsed = time.time() - start
            time.sleep(max(0, delay - elapsed))

    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        cap.release()

if __name__ == "__main__":
    stream_webcam_to_ascii()
