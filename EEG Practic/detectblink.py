from pylsl import StreamInlet, resolve_stream
import pyautogui
import time

# 1. Look for the EEG stream on the network
print("Scanning for EEG stream...")
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

# 2. Settings (You'll tune these when the real Muse arrives)
THRESHOLD = 120.0  # Spike height to count as a blink
COOLDOWN = 0.6     # Seconds to wait before allowing another blink trigger
last_blink_time = 0

print("Connected to stream! Ready for blinks...")

while True:
    # sample: [TP9, AF7, AF8, TP10]
    sample, timestamp = inlet.pull_sample()
    
    # We check AF7 and AF8 (indices 1 and 2) because they sit on the forehead
    frontal_channels = [sample[1], sample[2]]
    
    for val in frontal_channels:
        if val > THRESHOLD:
            current_time = time.time()
            if current_time - last_blink_time > COOLDOWN:
                print("BLINK DETECTED! Action: Spacebar")
                pyautogui.press('space')
                last_blink_time = current_time
            break # Exit loop once blink is handled for this sample