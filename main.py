import cv2
from gaze_tracking import GazeTracking
from utils.FFMConverter import FFMConverter

def focus_score(uuid, input_filepath):

    output_filepath = fr"C:\Users\bsun7\Desktop\EngHack\COMRADE\data_out\tester.mp4"

    #Convert webm file to mp4
    ffm = FFMConverter()
    ffm.convert_to_mp4(input_filepath, output_filepath)
    gaze = GazeTracking()
    video = cv2.VideoCapture(output_filepath)


    #Scoring Metric Criteria
    number_of_frames = 0
    centered_reads = 0
    while True:
        # We get a new frame from the video
        _, frame = video.read()

        if not _:
            break
        # We get the next frame before sending it to GazeTracking to speed up play back
        # _, frame = video.read()
        # if not _:
        #     break
        number_of_frames += 1

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""


        if gaze.is_blinking():
            text = "Blinking"
            number_of_frames -= 1
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

    return {"Focus": focus_score}


print(focus_score("eeasd141f1254561faf", r"C:\Users\bsun7\Desktop\EngHack\COMRADE\data\recording.webm"))


def context_score(saved_response_filepath, input_response_filepath):
#Accepts two txt files containing one or more response
    
    import numpy as np
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    saved = []
    answers = []

    with open(saved_response_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            saved.append(line)
        

    with open(input_response_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            answers.append(line)

    tfidf = TfidfVectorizer(
        input='content',
        strip_accents='ascii',
        lowercase='True',
        stop_words='english',
        max_features = 50)

    
    saved_matrix = tfidf.fit_transform(saved)
    answer_matrix = tfidf.transform(answers)

    cosine_sim = cosine_similarity(answer_matrix, saved_matrix)

    return 100*np.max(cosine_sim)


