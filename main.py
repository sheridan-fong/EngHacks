import cv2
from gaze_tracking import GazeTracking

def focus_score(filepath):
    gaze = GazeTracking()
    video = cv2.VideoCapture(filepath)


    #Scoring Metric Criteria
    number_of_frames = 0
    centered_reads = 0
    while True:
        # We get a new frame from the video
        _, frame = video.read()

        if not _:
            break
        # We get the next frame before sending it to GazeTracking to speed up play back
        _, frame = video.read()
        if not _:
            break
        number_of_frames += 1

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""


        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
            centered_reads += 1

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("COMRADE", frame)

        #Press escape to close
        if cv2.waitKey(1) == 27:
            break

    focus_score = centered_reads/number_of_frames
