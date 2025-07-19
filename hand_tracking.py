import cv2
import mediapipe as mp
import pyautogui

class HandMouseController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.4,
            min_tracking_confidence=0.4,
            model_complexity=0  # lower complexity for CPU
        )
        self.screen_w, self.screen_h = pyautogui.size()

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            hand_landmarks = result.multi_hand_landmarks[0]
            index_finger_tip = hand_landmarks.landmark[8]

            x = int(index_finger_tip.x * frame.shape[1])
            y = int(index_finger_tip.y * frame.shape[0])

            screen_x = int(index_finger_tip.x * self.screen_w)
            screen_y = int(index_finger_tip.y * self.screen_h)

            pyautogui.moveTo(screen_x, screen_y)

            # Visual indicator (can comment out to reduce CPU load)
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        return frame
