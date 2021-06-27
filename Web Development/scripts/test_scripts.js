// // given a JSON
// var info = '[{"Name":"Sheridan Fong","Contact":12345678,"Age":17},{"Name":"Benjamin Sun","Contact":911,"Age":21}]'
//
// var question = '{"question":"How old are you?"}'
//
//
// // Begin accessing JSON data here
// var data = JSON.parse(info)
//
// console.log(data)
// console.log(data[0]["Name"])
//
// const app = document.getElementById('root')
//
// console.log(app)
//
// const Name = document.createElement('h1')
// Name.textContent = data[0]["Name"]
//
// const Age = document.createElement('p')
// Age.textContent = data[0]["Age"]
//
// app.appendChild(Name)
// app.appendChild(Age)


var sample = '{"focus_score":20, "focus_feedback":"Strong","content_score":35,"content_feedback": "STUFF", "audio_score":49,"audio_feedback":"THIS ONE MIGHT NOT WORK LMAO"}'

var data_test = JSON.parse(sample)

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
