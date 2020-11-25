<template>
  <div>
    <a-card>
     <!-- <p id='status'>Loading model...</p>-->
      <a>PxxxNxx</a>
      <canvas id="canvas" width="320" height="240"></canvas>
      <video id="video" width="320" height="240" autoplay style="display: none"></video>

      <!--<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/addons/p5.sound.min.js"></script>-->

      <button @click="init()">
        init
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
      },
      init(){
        // Grab elements, create settings, etc.
        var video = document.getElementById("video");
//        var elment=document.createElement("CANVAS")
//        elment.id = "canvas";
//        elment.width = 32;
//        elment.height = 24;
//        var cardelment=document.getElementById("card");
//        cardelment.appendChild(elment);
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
          ctx.drawImage(video, 0, 0, 100, 80);
          // We can call both functions to draw all keypoints and the skeletons
          drawKeypoints();
          drawSkeleton();
          window.requestAnimationFrame(drawCameraIntoCanvas);

        }
        // Loop over the drawCameraIntoCanvas function

        drawCameraIntoCanvas();

        // Create a new poseNet method with a single detection
        const poseNet = ml5.poseNet(video, modelReady);
        poseNet.on("pose", gotPoses);

        // A function that gets called every time there's an update from the model
        function gotPoses(results) {
          poses = results;
          console.log('ps',poses);
        }

        function modelReady() {
          console.log("model ready");
          poseNet.multiPose(video);
        }

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
                ctx.stroke();
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
              ctx.stroke();
            }
          }
        }


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
