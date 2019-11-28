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
      // player.width(this.videoW)   //设置播放器宽度

    },

    data() {
      return {
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
  }
</script>
