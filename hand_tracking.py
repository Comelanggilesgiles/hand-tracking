import cv2
import mediapipe as mp
import time


class HandTracker:
    def __init__(self, static_mode=False, max_hands=2,
                 detection_confidence=0.7, tracking_confidence=0.7):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=static_mode,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_styles = mp.solutions.drawing_styles
        self.results = None

    def find_hands(self, img, draw=True):
        """Detect hands and draw landmarks on the image."""
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_styles.get_default_hand_landmarks_style(),
                        self.mp_styles.get_default_hand_connections_style()
                    )
        return img

    def find_positions(self, img, hand_no=0):
        """Return list of [id, x, y] for each of the 21 landmarks."""
        landmark_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hand_no]
            h, w, _ = img.shape
            for idx, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([idx, cx, cy])
        return landmark_list


def open_camera():
    """Try camera indexes 0, 1, 2 and return the first one that works."""
    for index in (0, 1, 2):
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.isOpened():
            ok, _ = cap.read()
            if ok:
                print(f"Using camera {index}")
                return cap
        cap.release()
    return None


def main():
    cap = open_camera()
    if cap is None:
        print("No camera found. Check Windows camera permissions, "
              "close other apps using the camera, or connect a webcam.")
        return

    tracker = HandTracker()
    prev_time = 0

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read from camera")
            break

        img = tracker.find_hands(img)
        landmarks = tracker.find_positions(img)

        if landmarks:
            # Draw a circle on the index fingertip (landmark 8)
            x, y = landmarks[8][1], landmarks[8][2]
            cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)

        # FPS display
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        cv2.putText(img, f"FPS: {int(fps)}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        cv2.imshow("Hand Tracking", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
