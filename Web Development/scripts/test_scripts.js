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
client.get('http://some/thing?with=arguments', function(response) {
    alert("made it here!")
});


// Grabbing the data and outputting it to the screen

var sample = '{"focus_score":20, "focus_feedback":"Strong","content_score":35,"content_feedback": "STUFF", "audio_score":49,"audio_feedback":"THIS ONE MIGHT NOT WORK LMAO"}'

var data_test = JSON.parse(response) // prior was sample (response should be where the current json data is)

console.log(data_test)

const application = document.getElementById('root')

const focusScore = document.createElement('h3')
focusScore.textContent = "Focus Score : " + data_test["focus_score"]
// console.log(data_test.focus_score)

const focusFeedback = document.createElement('h3')
focusFeedback.textContent = "Focus Feedback : " + data_test["focus_feedback"]
// console.log(data_test["focus_feedback"])

const contentScore = document.createElement('h3')
contentScore.textContent = "Content Score : " + data_test["content_score"]

const contentFeedback = document.createElement('h3')
contentFeedback.textContent = "Content Feedback : "+ data_test["content_feedback"]

const audioScore = document.createElement('h3')
audioScore.textContent = "Audio Score : " + data_test["audio_score"]

const audioFeedback = document.createElement('h3')
audioScore.textContent = "Audio Feedback : " + data_test["audio_feedback"]

application.appendChild(focusScore)
application.appendChild(focusFeedback)
application.appendChild(contentScore)
application.appendChild(contentFeedback)
application.appendChild(audioScore)
application.appendChild(audioFeedback)
