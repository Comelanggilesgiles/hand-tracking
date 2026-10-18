# Hand Tracking

Real-time hand tracking from your webcam in under 100 lines of Python.

## Description

Hand Tracking detects up to two hands in a live webcam feed and draws the 21 landmarks (wrist, knuckles and fingertips) on each one. It uses Google's MediaPipe for detection and OpenCV for video capture and display. The code is organised around a small `HandTracker` class, so you can reuse it as a base for finger counting, gesture control or a virtual mouse.

The project needs no API keys, no accounts and no internet connection once the packages are installed.

## Key Features

- Real-time detection of up to 2 hands
- 21 landmarks per hand with pixel coordinates
- Highlights the index fingertip with a green dot
- Live FPS counter
- Automatic camera detection (tries cameras 0, 1 and 2)
- Clean, reusable `HandTracker` class

## Screenshot

![Hand Tracking demo](/download.jpg)



## Requirements

- Windows 10 or 11 (also works on macOS and Linux with small changes)
- Python 3.9 to 3.12 (check with `python --version`)
- A webcam, or a phone used as a webcam with DroidCam or Iriun Webcam
- Git (only needed to clone the repo)

## Installation

1. Clone the repository and enter the folder:

   ```powershell
   git clone https://github.com/Comelanggilesgiles/hand-tracking.git
   cd hand-tracking
   ```

2. Create a virtual environment:

   ```powershell
   py -3.12 -m venv .venv
   ```

3. Activate it. If PowerShell blocks the script, run the second line first:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   .\.venv\Scripts\Activate.ps1
   ```

   Your prompt should now start with `(.venv)`.

4. Install the dependencies. This is a large download, so wait until it prints `Successfully installed`:

   ```powershell
   pip install -r requirements.txt
   ```

## Usage

```powershell
python hand_tracking.py
```

- A window opens showing your webcam feed.
- Hold up a hand to see the landmarks and the green index fingertip dot.
- Press **Q** to quit.

### Use it in your own code

```python
from hand_tracking import HandTracker

tracker = HandTracker(max_hands=1)
img = tracker.find_hands(img)           # draws landmarks
landmarks = tracker.find_positions(img) # [[id, x, y], ...]
```

### Landmark reference

| ID | Point       | ID | Point      |
|----|-------------|----|------------|
| 0  | Wrist       | 12 | Middle tip |
| 4  | Thumb tip   | 16 | Ring tip   |
| 8  | Index tip   | 20 | Pinky tip  |

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `No module named 'cv2'` | The virtual environment is not active or the install did not finish. Activate it and run `pip install -r requirements.txt` again. |
| `No camera found` | Turn on camera access in Windows Settings, Privacy and security, Camera. Close Zoom, Teams, Discord or the Windows Camera app. |
| No webcam on your PC | Use your phone with DroidCam or Iriun Webcam. |
| `INFO` and `W0000` log lines | Harmless TensorFlow Lite messages. Ignore them. |

## Tech Stack

- Python 3.12
- MediaPipe 0.10.14 (hand landmark detection)
- OpenCV 4.10 (video capture and drawing)
- NumPy 1.x

## Project Structure

```
hand-tracking/
  hand_tracking.py   main script and HandTracker class
  requirements.txt   pinned dependencies
  docs/              screenshots
  README.md
  .gitignore
```

## Ideas to Extend

- Finger counting
- Virtual mouse with `pyautogui`
- Volume control from thumb-to-index distance
- Gesture recognition (pinch, fist, open palm)

## License

Add a license of your choice (for example MIT) before sharing the project publicly.
