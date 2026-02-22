import time
import random
from pylsl import StreamInfo, StreamOutlet

# 1. Setup Stream: Muse 2 has 4 channels (TP9, AF7, AF8, TP10) at 256Hz
info = StreamInfo('PetalMetrics_EEG', 'EEG', 4, 256, 'float32', 'muse01')
outlet = StreamOutlet(info)

print("Simulated Muse 2 is now streaming...")

while True:
    # Generate background noise (Standard EEG is roughly -50 to 50 microvolts)
    sample = [random.uniform(-30, 30) for _ in range(4)]
    
    # Randomly inject a "Blink" spike (Blinks are massive: 100-200+ microvolts)
    if random.random() > 0.98:
        print("!! Simulating Blink Signal !!")
        sample = [200.0, 200.0, 200.0, 200.0] 
        
    outlet.push_sample(sample)
    time.sleep(1.0 / 256.0) # Maintain 256Hz frequency