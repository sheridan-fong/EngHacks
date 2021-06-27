import cv2
from gaze_tracking import GazeTracking
from utils.FFMConverter import FFMConverter
import os
import wave


def get_uuid(uuid_filepath):
    with open(uuid_filepath, 'r') as uuid_file:
        return uuid_file.readlines()[1]


def focus_score(uuid):

    output_filepath = fr"C:\Users\bsun7\Desktop\EngHack\COMRADE\data_out\{uuid}.mp4"


    input_filepath = r'C:\Users\bsun7\Desktop\EngHack\COMRADE' + fr'\data\WEBM\{uuid}.webm'

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

    focus_score = centered_reads/number_of_frames *10
    focus_string = ""
    if focus_score > 10:
        focus_string = 'Nice! Your focus is great, keep it up!'
    elif focus_score > 8:
        focus_string = "Good. Try to focus on the camera some more"
    elif focus_score > 5:
        focus_string = "Focus more towards the camera"
    else:
        focus_string = "Poor Focus. Spend more time looking and engaging with the camera then your surroundings"

    return {"focus_score": focus_score, "focus_feedback":focus_string}




def speech_score(uuid):
    mysp = __import__('my-voice-analysis')

    cwd = r'C:\Users\bsun7\Desktop\EngHack\COMRADE'
    input_filepath = cwd + fr'\data_out\{uuid}.mp4'
    output_filepath = cwd + fr'\data\WAV\{uuid}.wav'

    ffm = FFMConverter()
    '''
    
    #Uncomment if it needs a file to overwrite to work

    try:
        with wave.open(output_filepath, 'rb') as file:
            pass
        except FileNotFoundError:
            print('eyo')
            with wave.open(output_filepath, 'wb') as file:
                file.setnchannels(2)
                file.setsampwidth(2)
                file.setframerate(41000)

    '''
    ffm.convert_to_wav(input_filepath, output_filepath)

    p = fr'{uuid}'
    c = cwd + fr'\data\WAV'

    rating = mysp.myspgend(p,c)

    pauses = mysp.mysppaus(p,c)

    speed = mysp.myspsr(p,c)

    articulation = mysp.myspatc(p,c)


    pronounce = mysp.mysppron(p,c)

    pauses_response = []
    speed_response = []
    articulation_response = []

    speed_dict = {
    '0': [0,'Too Slow'],
     '1': [25, 'Slow'],
     '2': [50, 'Slow'],
     '3': [75, 'Good Speed, could be a bit faster'],
     '4': [100, 'Perfect Speed'],
     '5': [75, 'Good speed, could be a little slower'],
     '6': [50, 'Fast'],
     '7': [25, 'Fast'],
     '8': [0, 'Too fast']}


    articulation_dict = {
    '0': [0,'Too Slow'],
     '1': [0, 'Too Slow'],
     '2': [25, 'Slow'],
     '3': [50, 'Slow'],
     '4': [75, 'Good Articluation, could be a bit faster'],
     '5': [100, 'Perfect Articluation'],
     '6': [75, 'Good Articulation, could be a little slower'],
     '7': [50, 'Fast'],
     '8': [25, 'Fast'],
     '9': [0, 'Too fast']}


    if pauses > 100:
        pauses_response = [0, 'Too many pauses']
    elif pauses > 80:
        pauses_response = [25, 'Too many pauses']
    elif pauses > 60:
        pauses_response = [50, 'Just a few too many pauses']

    elif pauses > 40:
        pauses_response = [75, 'Good, try to reduce the amount of pauses']

    else:
        pauses_response = [100, 'Very few pauses, well done!']

    try:
        speed_response = speed_dict[str(speed)]
    except KeyError:
        speed_response = [0, 'Too fast']

    try:
        articulation_response = articulation_dict[str(articulation)]
    except KeyError:
        articluation_response = [0, 'Too fast']


    percentages = [pauses_response[0], speed_response[0], articulation_response[0], pronounce]

    mean_percent = sum(percentages)/len(percentages)

    feedback_statement = 'Feedback for Speed: ' + speed_response[1] + ' Feedback for Articulation: ' + articulation_response[1] + ', Feedback for Pausing: ' + pauses_response[1] + ', Pronounce Rating (out of 100): ' + str(pronounce)


    return {'audio_score': mean_percent, 'audio_feedback': feedback_statement}




def context_score(uuid):
#Accepts two txt files containing one or more response

    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import speech_recognition as sr

    input_filepath = r'C:\Users\bsun7\Desktop\EngHack\COMRADE' + fr'\data\WAV\{uuid}.wav'

    current_question_filepath = r'C:\Users\bsun7\Desktop\EngHack\COMRADE' + fr'\data\current_question.txt'
    question_csv_filepath = r'C:\Users\bsun7\Desktop\EngHack\COMRADE' + fr'\data\question_matrix.csv'

    question_series = pd.read_csv(question_csv_filepath, squeeze=True, index_col = 0, header = 0)

    current_question = ''
    with open(current_question_filepath, 'r') as index_file:

        current_question = index_file.readlines()[0].rstrip("\n")

    responses_filepath = r"C:\Users\bsun7\Desktop\EngHack\COMRADE\data" + question_series[current_question]




    recognizer = sr.Recognizer()
    audio_clip = sr.AudioFile("{}".format(input_filepath))

    with audio_clip as source:
        audio_file = recognizer.record(source)

    result = recognizer.recognize_google(audio_file)

    saved = []
    answers = [r'{}'.format(result)]

    with open(responses_filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            saved.append(line)



    tfidf = TfidfVectorizer(
        input='content',
        strip_accents='ascii',
        lowercase='True',
        stop_words='english',
        max_features = 50)


    saved_matrix = tfidf.fit_transform(saved)
    answer_matrix = tfidf.transform(answers)

    cosine_sim = cosine_similarity(answer_matrix, saved_matrix)

    max_cosine_sim = cosine_sim.max()

    se = pd.Series(answer_matrix.todense().tolist()[0], index=tfidf.get_feature_names())

    largest = [k for k,v in se.nlargest().to_dict().items() if v > 0]
    smallest = [k for k,v in se.nsmallest().to_dict().items() if v == 0]


    score_list = 'Great job using these words: '

    for item in (largest):
        if item == largest[-1]:
            score_list += ('and ' + item + '. ')
        else:
            score_list += (item + ', ')

    score_list += 'Try to use some of these words to strenghten your response: '
    for item in (smallest):
        if item == smallest[-1]:
            score_list += ('and ' + item + '. ')
        else:
            score_list += (item + ', ')

    percentage = round(200*max_cosine_sim, 2)
    if percentage > 100:
        percentage = 100


    return {'content_score':percentage, 'content_feedback':score_list}


uuid_filepath = r'C:\Users\bsun7\Desktop\EngHack\COMRADE\data\current_question.txt'
uuid = get_uuid(uuid_filepath)


json_dict = {}

focus_dict = focus_score(uuid)
json_dict.update(focus_dict)

speech_dict = speech_score(uuid)
json_dict.update(speech_dict)

context_dict = context_score(uuid)
json_dict.update(context_dict)

print("\n\n\n\n\n\n\n\n", json_dict)

