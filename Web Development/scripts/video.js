// setting up the video ---------------------------------------------------------------------------

let camera_start_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");
let submit = document.querySelector("#submit");

let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];
let video_local = null;

camera_start_button.addEventListener('click', async function() {
   	camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });    // security option to grant or deny access to their cameras or microphones
	video.srcObject = camera_stream;
});

start_button.addEventListener('click', function() {
    console.log("here")
    // set MIME type of recording as video/webm
    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });

    // event : new recorded video blob available
    media_recorder.addEventListener('dataavailable', function(e) {
		blobs_recorded.push(e.data);
    });

    // event : recording stopped & all blobs sent
    media_recorder.addEventListener('stop', function() {
    	// create local object URL from the recorded video blobs
    	video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));
    	download_link.href = video_local;
        console.log(blobs_recorded)
    });

    // start recording with each recorded blob having 1 second video
    media_recorder.start(1000);
});

function stop(stream) {
    stream.getTracks().forEach(track => track.stop());
}

stop_button.addEventListener('click', function() {
	media_recorder.stop();
    stop(video.srcObject);
});

submit.addEventListener('click', function() {
    var blob = new Blob(blobs_recorded, { 'type' : 'video/webm' });

    console.log("start sending binary data...");
    var form = new FormData();
    form.append('video', blob);

    $.ajax({
        url: 'http://localhost:8000/api/upload/file/',
        type: 'POST',
        data: form,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log('response' + JSON.stringify(data));
        },
        error: function () {
        // handle error case here
        }
    });
});

// adding in the specific question ------------------------------------------
var sample = '{"question":"This is the question"}'

var data_test = JSON.parse(sample)

console.log(data_test)

const app_question = document.getElementById('question_here')

const question = document.createElement('h1')
question.textContent = data_test["question"]

app_question.appendChild(question)

// adding in the button click function ----------------------------------
function clickedButton(){
    alert("You button was pressed");
    var client = new HttpClient();
    client.get('http://some/thing?with=arguments', function(response) {
      // the data is in "response"
      var response_parsed = JSON.parse(response)

      // going to have to replace old child with new child
      // https://www.w3schools.com/XML/met_node_replacechild.asp
      // https://www.w3schools.com/jsref/met_node_replacechild.asp
      const generated_question = document.createElement('h1')
      generated_question.textContent = data_test["question"]

      // generating first met_node_replacechild
      var first_node = document.getElementById('question_here').childNodes[0];

      first_node.replaceChild(generated_question, first_node.childNodes[0]);


      alert("get request done")
  });
};

// code from stack overflow -----------------------------
// link: https://stackoverflow.com/questions/247483/http-get-request-in-javascript
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


// alternative way https://zetcode.com/javascript/jsonurl/
