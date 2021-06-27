// HTPPS client functions

var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() {
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );
        anHttpRequest.send( null );
    }
}

// enter in link here
var client = new HttpClient();
client.get('localhost:8000/api/results', function(response) {
    alert("made it here!")
});


// Grabbing the data and outputting it to the screen

var sample = '{"focus_score":20, "focus_feedback":"Poor Focus. Spend more time looking and engaging with the camera then your surroundings","content_score":35,"content_feedback": "You used a lot of great words such as collaboration, teamwork and responsibility. Try using more words like enthusiastic", "audio_score":49,"audio_feedback":"You had great pronounciation and pace."}'

var data_test = JSON.parse(sample) // prior was sample (response should be where the current json data is)

console.log(data_test)

const application = document.getElementById('root')

const focusScore = document.createElement('h3')
const focusScoreDesc = document.createElement('p')
focusScore.textContent = "Focus Score : " 
focusScoreDesc.textContent = data_test["focus_score"] + "%"
// console.log(data_test.focus_score)

const focusFeedback = document.createElement('h3')
const focusFeedbackDesc = document.createElement('p')
focusFeedback.textContent = "Focus Feedback : " 
focusFeedbackDesc.textContent = data_test["focus_feedback"]
// console.log(data_test["focus_feedback"])

const contentScore = document.createElement('h3')
const contentScoreDesc = document.createElement('p')
contentScore.textContent = "Content Score : "
contentScoreDesc.textContent = data_test["content_score"] + "%"

const contentFeedback = document.createElement('h3')
const contentFeedbackDesc = document.createElement('p')
contentFeedback.textContent = "Content Feedback : "
contentFeedbackDesc.textContent = data_test["content_feedback"]

const audioScore = document.createElement('h3')
const audioScoreDesc = document.createElement('p')
audioScore.textContent = "Audio Score : " 
audioScoreDesc.textContent = data_test["audio_score"] +"%"

const audioFeedback = document.createElement('h3')
const audioFeedbackDesc = document.createElement('p')
audioFeedback.textContent = "Audio Feedback : " 
audioFeedbackDesc.textContent = data_test["audio_feedback"]

application.appendChild(focusScore)
application.appendChild(focusScoreDesc)
application.appendChild(focusFeedback)
application.appendChild(focusFeedbackDesc)
application.appendChild(contentScore)
application.appendChild(contentScoreDesc)
application.appendChild(contentFeedback)
application.appendChild(contentFeedbackDesc)
application.appendChild(audioScore)
application.appendChild(audioScoreDesc)
application.appendChild(audioFeedback)
application.appendChild(audioFeedbackDesc)
