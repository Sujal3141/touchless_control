import cv2
import time
from hand_tracking import HandMouseController

def main():
    cap = cv2.VideoCapture(0)

    # Set lower webcam resolution
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height

    controller = HandMouseController()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = controller.process_frame(frame)
        cv2.imshow("Touchless Mouse", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) == ord('q'):
            break

        time.sleep(0.015)  # Cap to ~60 FPS (helps CPU)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
