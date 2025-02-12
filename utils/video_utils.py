import cv2
import os

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return []

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        print("Error: No frames to save!")
        return

    os.makedirs(os.path.dirname(output_video_path), exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Try 'MJPG' if 'mp4v' fails
    height, width, _ = output_video_frames[0].shape

    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

    if not out.isOpened():
        print(f"Error: Could not open VideoWriter for {output_video_path}")
        print(f"Codec: {'mp4v'} | FPS: 24 | Resolution: {width}x{height}")
        return  # Exit function early

    for frame in output_video_frames:
        out.write(frame)

    out.release()
    print(f"Video successfully saved at {output_video_path}")



