import cv2
import pandas as pd
from datetime import datetime

def count_objects(results):
    if results[0].boxes is None:
        return 0
    return len(results[0].boxes)

def object_wise_count(results, model):
    counts = {}
    if results[0].boxes is None:
        return counts

    classes = results[0].boxes.cls.cpu().numpy()

    for cls in classes:
        name = model.names[int(cls)]
        counts[name] = counts.get(name, 0) + 1

    return counts

def save_history(count):
    data = {"Time": datetime.now(), "Objects": count}
    pd.DataFrame([data]).to_csv("history.csv", mode='a', header=False, index=False)

def draw_info(frame, count):
    cv2.putText(frame, f"Objects: {count}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    return frame