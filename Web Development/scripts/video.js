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
