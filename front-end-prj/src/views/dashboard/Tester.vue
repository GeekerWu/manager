<template>
  <div>
    <div >
      <v-chart :forceFit="true" height="400" :data="data" :scale="scale">
        <v-tooltip :showTitle="false" />
        <v-axis dataKey="GDP" :label="axisLabel" />
        <v-legend dataKey="Population" :show="false" />
        <v-point
          position="GDP*LifeExpectancy"
          :color="pointColor"
          :size="pointSize"
          :vStyle="pointStyle"
          tooltip="Country*Population*GDP*LifeExpectancy"
          shape="circle"
        />
      </v-chart>
    </div>

    <div v-show="!isError">
      <video id="videobox" class="video-js vjs-default-skin vjs-big-play-centered vjs-16-9" controls preload="auto" webkit-playsinline="true" playsinline="true" type="application/x-mpegURL" allowsInlineMediaPlayback=YES  webview.allowsInlineMediaPlayback=YES  width='100%' ref='videoRef' x5-video-player-fullscreen="true" :poster="posterSrc" >
        <source id="sourceBox" :src="videoSrc">
        <p class="vjs-no-js">unsupport source</p>
      </video>
    </div>
    <div v-show="isError" class="errorTip"><p>got error</p></div>
  </div>
</template>

<script>
  import * as $ from 'jquery';
  import { Global } from 'viser-vue';

  import videojs from 'video.js'
  import 'videojs-contrib-hls'



  const scale = [{
    dataKey: 'LifeExpectancy',
    alias: '人均寿命（年）',
  }, {
    dataKey: 'Population',
    type: 'pow',
    alias: '人口总数',
  }, {
    dataKey: 'GDP',
    alias: '人均国内生产总值($)',
  }, {
    dataKey: 'Country',
    alias: '国家/地区',
  }];

  const colorMap = {
    'Asia': Global.colors[0],
    'Americas': Global.colors[1],
    'Europe': Global.colors[2],
    'Oceania': Global.colors[3],
  };
  const laeblFormatter = (value) => {
    return (value / 1000).toFixed(0) + 'k';
  };
  export default {
    mounted() {
        //support viser chart
       $.getJSON('https://viserjs.github.io/assets/data/bubble.json', (data) => {
        this.$data.data = data;
      });
      //support video js
      //为避免在初始化video时播放源是空的，报播放源错误，需要先给source 的src赋值
      var player = videojs('videobox',{
          bigPlayButton: true,
          textTrackDisplay: true,
          posterImage: true,
          errorDisplay: false,
          controlBar: false,
          playbackRates: [0.5, 1, 1.5, 2],
          ControlBar:{
            customControlSpacer: true
          }
        },
        function onPlayerReady(){
          this.play();
          setTimeout(() => {   //延时确保能监听到视频源错误
            var mediaError = this.error();
            if(mediaError!=null && mediaError.code){
              _this.isError=true
              Dialog.alert({
                message: 'sorry!player got some error.<br>please refresh again',
                confirmButtonText:'OK'
              }).then(() => {
                _this.goback();
              });
            }
          },1000);
        });
      // player.width(this.videoW)   //设置播放器宽度

    },

    data() {
      return {
        //support video js
//        videoSrc:'http://down.soundaer.com/live/stream_89003_sd/playlist.m3u8?k=d708550fbd49c58a1b8a8412c8623277&t=1553687908',
        videoSrc: 'http://live.hkstv.hk.lxdns.com/live/hks/playlist.m3u8',
//        posterSrc:'https://matrimony001.100msh.net.cn/public/code/material/mp-7261-1554175849.jpg',
        posterSrc:' ../../assets/offline.jpg',
        isError:false,

        //support viser chart
        data: [],
        scale,
        height: 400,
        axisLabel: {
          formatter: laeblFormatter,
        },
        pointColor: ['continent', val => colorMap[val]],
        pointSize: ['Population', [4, 65]],
        pointStyle: ['continent', {
          lineWidth: 1,
          strokeOpacity: 1,
          fillOpacity: 0.3,
          opacity: 0.65,
          stroke: val => colorMap[val],
        }],
      }
    },

    beforeDestroy(){
      const videoDom = this.$refs.videoRef;   //不能用document 获取节点
      videojs(videoDom).dispose();  //销毁video实例，避免出现节点不存在 但是flash一直在执行,也避免重新进入页面video未重新声明
    }
  }
</script>
