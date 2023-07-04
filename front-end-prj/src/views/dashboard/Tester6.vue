<template>
  <div>
    <a-card id="card">
     <!-- <p id='status'>Loading model...</p>-->
      <a>PoseNet</a>
      <br/>
      <!--<canvas id="canvas" width="320" height="240"></canvas>-->
      <video id="video" width="640" height="480" autoplay style="display: none"></video>
<!--      <video id="video" width="640" height="480" autoplay style="display: none"></video>-->
      <!--<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/addons/p5.sound.min.js"></script>-->
     <!-- <button @click="hp()">
        hp
      </button>-->
      <button @click="pn()">
        pn
      </button>
      <button @click="closed()">
        close
      </button>
    </a-card>
    <!--<title>Getting Started with ml5.js</title>-->
   <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0">-->
    <!-- p5 -->
  </div>
</template>
<script>
  import AInput from "ant-design-vue/es/input/Input";
  import {saveinit,loadinit,deleteinit}from "@/api/poseapi.js"
  import ACard from "ant-design-vue/es/card/Card";
  import ml5 from 'ml5';
  export default {
    components: {
      ACard,
      ml5,
      AInput},
    name: 'tester5',
    data() {
      return {
        disabled:false,
        socketdata:'',
        inputvalue:'',
        channellist:[],
        min:20,
        max:50,
        defaultval:30,
        posedata:'',
        printpose:0,
      }
    },
    mounted(){
      console.log('ml5 version:', ml5.version);
      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
                this.socketdata=this.socketdata+'\n'+JSON.stringify(data);
                console.log(data);
            });
    },
    methods: {
      closed(){
        console.log('closed');
        var card = document.getElementById("card");
        card.removeChild(document.getElementById("canvas"))
      },
     /* hp(){
        let handpose;
        let video;
        let predictions = [];

        function setup() {
          createCanvas(640, 480);
          video = createCapture(VIDEO);
          video.size(width, height);
          handpose = ml5.handpose(video, modelReady);

          // This sets up an event that fills the global variable "predictions"
          // with an array every time new hand poses are detected
          handpose.on("predict", results => {
            predictions = results;
          });

          // Hide the video element, and just show the canvas
          video.hide();
        }

        function modelReady() {
          console.log("Model ready!");
        }

        function draw() {
          image(video, 0, 0, width, height);

          // We can call both functions to draw all keypoints and the skeletons
          drawKeypoints();
        }

// A function to draw ellipses over the detected keypoints
        function drawKeypoints() {
          for (let i = 0; i < predictions.length; i += 1) {
            const prediction = predictions[i];
            for (let j = 0; j < prediction.landmarks.length; j += 1) {
              const keypoint = prediction.landmarks[j];
              fill(0, 255, 0);
              noStroke();
              ellipse(keypoint[0], keypoint[1], 10, 10);
            }
          }
        }
      },*/


      pn(){
        // Grab elements, create settings, etc.
        var that =this
        var video = document.getElementById("video");
        var elment=document.createElement("CANVAS")
        elment.id = "canvas";
        elment.width = 640;
        elment.height = 480;
        var cardelment=document.getElementById("card");
        cardelment.appendChild(elment);
        var canvas = document.getElementById("canvas");
        var ctx = canvas.getContext("2d");

        // The detected positions will be inside an array
        let poses = [];


        // Create a webcam capture
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
          navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            video.srcObject = stream;
            video.play();
          });
        }
        // A function to draw the video and poses into the canvas.
        // This function is independent of the result of posenet
        // This way the video will not seem slow if poseNet
        // is not detecting a position
        function drawCameraIntoCanvas() {
          // Draw the video element into the canvas
          ctx.drawImage(video, 0, 0, 640, 480);
          // We can call both functions to draw all keypoints and the skeletons
          drawKeypoints();
          drawSkeleton();
          window.requestAnimationFrame(drawCameraIntoCanvas);

        }
        // Loop over the drawCameraIntoCanvas function

        drawCameraIntoCanvas();

        // Create a new poseNet method with a single detection
        var option={
          architecture: 'MobileNetV1',
          imageScaleFactor: 0.3,
          outputStride: 16,
          flipHorizontal: false,
          minConfidence: 0.5,
          maxPoseDetections: 1,
          scoreThreshold: 0.5,
          nmsRadius: 20,
          detectionType: 'multiple',
          inputResolution: 513,
          multiplier: 0.75,
          quantBytes: 2,
        };;
        const poseNet = ml5.poseNet(video, option,modelReady);
        poseNet.on("pose", gotPoses);

        // A function that gets called every time there's an update from the model
        function gotPoses(results) {
          poses = results;
         console.log(that.printpose);
          that.printpose= parseInt(that.printpose)+1;
          if (that.printpose<5) {
            console.log('ps', poses);
          }
        }

        function modelReady() {

            console.log("model ready");

          poseNet.multiPose(video);
        }
        var angle=50
        // A function to draw ellipses over the detected keypoints
        function drawKeypoints() {
          // Loop through all the poses detected
          for (let i = 0; i < poses.length; i += 1) {
            // For each pose detected, loop through all the keypoints
            for (let j = 0; j < poses[i].pose.keypoints.length; j += 1) {
              let keypoint = poses[i].pose.keypoints[j];
              // Only draw an ellipse is the pose probability is bigger than 0.2
              if (keypoint.score > 0.2) {
                ctx.beginPath();
                ctx.arc(keypoint.position.x, keypoint.position.y, 10, 0, 2 * Math.PI);
                ctx.strokeStyle ="red";
                ctx.lineWidth =3;
                ctx.stroke();

                if(keypoint.part=='nose'){
                  console.log('nose',keypoint.position.x);
                  if (keypoint.position.x<400){
                    if (angle!=70){

                      that.wssentpose(70);
                      angle=70
                    }

                  }else if (keypoint.position.x>400){
                    if (angle!=120){
                      that.wssentpose(120);
                      angle=120
                    }

                  }
                }

              }
            }
          }
        }

        // A function to draw the skeletons
        function drawSkeleton() {
          // Loop through all the skeletons detected
          for (let i = 0; i < poses.length; i += 1) {
            // For every skeleton, loop through all body connections
            for (let j = 0; j < poses[i].skeleton.length; j += 1) {
              let partA = poses[i].skeleton[j][0];
              let partB = poses[i].skeleton[j][1];
              ctx.beginPath();
              ctx.moveTo(partA.position.x, partA.position.y);
              ctx.lineTo(partB.position.x, partB.position.y);
              ctx.strokeStyle ="yellow";
              ctx.lineWidth =3;
              ctx.stroke();
            }
          }
        }


      },
      wssentpose(pose){
        console.log('message send')
//        this.$socket.emit('subscribe',{'username':this.username,'table':'Z_UI_ASN_GR'});
        this.$socket.emit('message',{'username':'pose','msg':pose});
//                    this.$socket.emit('test',{'username':this.username,'table':'Z_UI_ASN_GR'});
//                    this.sockets.subscribe('response', (data) => {
//                        console.log('server sent response from onSwitchChange function');
//                        console.log(data,'if data change,can call refresh function locally');
//                    });
//                    this.sockets.subscribe('refreshdata', (data) => {
//                        console.log(data,'if data change,can call refresh function locally');
//                        this.renderChart(data)
//                    });
      },

      wssent(){
        console.log('message send')
//        this.$socket.emit('subscribe',{'username':this.username,'table':'Z_UI_ASN_GR'});
        this.$socket.emit('message',{'username':this.username,'msg':'hahahahahha'});
//                    this.$socket.emit('test',{'username':this.username,'table':'Z_UI_ASN_GR'});
//                    this.sockets.subscribe('response', (data) => {
//                        console.log('server sent response from onSwitchChange function');
//                        console.log(data,'if data change,can call refresh function locally');
//                    });
//                    this.sockets.subscribe('refreshdata', (data) => {
//                        console.log(data,'if data change,can call refresh function locally');
//                        this.renderChart(data)
//                    });
      }
    }
  }
</script>
