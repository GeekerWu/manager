<template>
  <div>
    <a-card title="channel" style="width: 100%">
      <a-form layout="inline">
        <div >
          channel count
        </div>
        <a-input v-model="inputvalue" ></a-input>
        <button @click="inputchange()">
          create channel
        </button>
        <button @click="loadinit()">
          init load
        </button>
        <button @click="posesent()">
          save init
        </button>
        <button @click="deleteinit()">
          delete init
        </button>
        <p>
          {{ this.posedata}}
        </p>
        <button @click="wssent()">
          ws send
        </button>
        <button @click="poseset()">
          pose set
        </button>
        <p>
          {{ this.socketdata}}
        </p>
        <!--<a-input v-model="min" @change="rangechange"></a-input>-->
        <!--<a-slider  range :value="[min,max]" :disabled="disabled" />-->
        <!--<a-input v-model="max" @change="rangechange"></a-input>-->

        <div>
            <a-row :gutter="48">
              <a-form-item   v-for="i in channellist":label="'channel '+i.channel.toString()+':'">
                <br/>
                <div >
                  <a-col  :md="4" :sm="24">
                    <a-form-item  :label=" 'name'"><a-input v-model="i.channel_name" @change="rangechange"></a-input></a-form-item>
                  </a-col>
                  <a-col  :md="6" :sm="24">
                    <p>curr val: {{i.currval}}
                      <!--    <a-form-item  :label=" 'curr val: '+i.currval">-->
                      <!--  <a-form-item  :label="i.currval">
                        </a-form-item>-->
                      <a-slider   :min="parseInt(i.min)" :max="parseInt(i.max)" v-model="i.currval" @change="sliderchange(i)" :disabled="disabled" />
                    </p>
                  </a-col>
                  <a-col :md="4" :sm="24">
                    <a-form-item  :label=" 'min:'"><a-input v-model="i.min" @change="rangechange"></a-input> </a-form-item>
                  </a-col>
                  <a-col :md="4" :sm="24">
                    <a-form-item  :label=" 'max:'"><a-input  v-model="i.max" @change="rangechange"></a-input></a-form-item>
                    <!--<a-form-item  :label=" 'name'"><a-input v-model="i.channel_name" @change="rangechange"></a-input></a-form-item>-->
                  </a-col>
                </div>
              </a-form-item>
            </a-row>
        </div>
      </a-form>
    </a-card>
    <a-card>
       <div id="zone_joystick">
       <!-- <div v-if="this.position!=''" id="debug">-->
          <div  id="debug">
          <ul v-if="this.position!=''">
            <li class="position">
              position :
              <ul>
                <li class="x">x : {{this.position.position.x}}</li>
                <li class="y">y : {{this.position.position.y}}</li>
              </ul>
            </li>
            <li class="force">force : {{this.position.force}}</li>
            <li class="pressure">pressure : {{this.position.pressure}}</li>
            <li class="distance">distance :  {{this.position.distance}}</li>
            <li class="angle">
              angle :<!--{{this.position.direction.angle}}-->
              <ul>
                <li >radian : <span v-if='this.position.angle.radian' >{{this.position.angle.radian}}</span></li>
                <li class="degree">degree : {{this.position.angle.degree}}</li>
              </ul>
            </li>
            <li class="direction">
              direction :{{this.position.pressure}}
              <ul>
                <li class="x">x : {{this.position.direction.x}}</li>
                <li class="y">y : {{this.position.direction.y}}</li>
                <li class="angle">angle : {{this.position.direction.angle}}</li>
              </ul>
            </li>
            <li class="direction">
              vector :
              <ul>
                <li class="x">x : {{this.position.vector.x}}</li>
                <li class="y">y : {{this.position.vector.y}}</li>
              </ul>
            </li>
            <div class="dump"></div>
          </ul>

        </div>
        <div class="zone dynamic active"><h1>dynamic</h1></div>
        <div class="zone semi"><h1>semi</h1></div>
        <div class="zone static"><h1>static</h1></div>
      </div>
    </a-card>
  </div>
</template>
<script>
  import AInput from "ant-design-vue/es/input/Input";
  import nipplejs from "nipplejs";
  import {poseset,saveinit,loadinit,deleteinit}from "@/api/poseapi.js"
  export default {
    components: {AInput,nipplejs},
    name: 'tester5',
    data() {
      return {
        disabled:false,
        socketdata:'',
        inputvalue:'',
        channellist:[],
        min:70,
        max:170,
        defaultval:120,
        posedata:'',
        joystick:null,
        position:'',
        els:null,
        nbEvents:0,



      }
    },
    mounted(){
        this.elDebug=document.getElementById('debug');
        /*this.els={
          position: {
            x: this.elDebug.querySelector('.position .x .data'),
              y: this.elDebug.querySelector('.position .y .data')
          },
          force: this.elDebug.querySelector('.force .data'),
            pressure: this.elDebug.querySelector('.pressure .data'),
            distance: this.elDebug.querySelector('.distance .data'),
            angle: {
            radian: this.elDebug.querySelector('.angle .radian .data'),
              degree: this.elDebug.querySelector('.angle .degree .data')
              degree: this.elDebug.querySelector('.angle .degree .data')
          },
          direction: {
            x: this.elDebug.querySelector('.direction .x .data'),
              y: this.elDebug.querySelector('.direction .y .data'),
              angle: this.elDebug.querySelector('.direction .angle .data')
          }
        };*/

      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
                this.socketdata=(this.socketdata+'\n'+JSON.stringify(data)).substr(-400,400);
//                console.log(data);
            });
      this.drawjoystick();
    },

    methods: {
      loadinit(){
        this.channellist=[];
        this.posedata='';
        this.socketdata='';
        loadinit().then(res => {
          console.log(res)
          var item
          for(item in res.res){
            res.res[item].currval=parseInt(res.res[item].currval);
          }
          this.channellist=res.res
          return res
        }).catch(err => {
          console.log(err)
        })
      },
      drawjoystick(){
        console.log('draw joystick');
        /*var options = {
          zone: document.getElementById('zone_joystick'),
        };*/
        let joyCon = document.querySelector("#zone_joystick");
        // let joyCon =document.getElementById('zone_joystick'),
        // eslint-disable-next-line no-debugger
        let joyoptions = {
          mode: "dynamic",// 'dynamic', 'static' or 'semi'
          size: 100,
          color:"#3e3232d9",
          /*position: {
            left: "50%",
            top: "50%"
          },//在容器内垂直居中显示*/

          // zone: s('.zone.dynamic'),

          multitouch: true,

          zone: joyCon //如果不提提供zone容器元素，那么默认动态生成的元素是注入在body中的。
        };
        this.joystick = nipplejs.create(joyoptions);
        this.bindNipple();
        // Get debug elements and map them
      },
      joydump(evt){
        var that=this;
        var elDump = this.elDebug.querySelector('.dump');
         setTimeout(function() {
            if (elDump.children.length > 4) {
              elDump.removeChild(elDump.firstChild);
            }
            var newEvent = document.createElement('div');
            newEvent.innerHTML = '#' + that.nbEvents+ ' : <span class="data">' +
              evt + '</span>';
            elDump.appendChild(newEvent);
           that.nbEvents += 1;
          }, 0);
      },
      bindNipple(){
        var that=this;
        this.joystick.on('start end', function(evt, data) {
          that.joydump(evt.type);
          that.position=data;

          /*that.debug(data);*/
        }).on('move', function(evt, data) {
          /*that.debug(data);*/
          that.position=data;
          console.log(that.position);
        }).on('dir:up plain:up dir:left plain:left dir:down ' +
          'plain:down dir:right plain:right',
          function(evt, data) {
            that.joydump(evt.type);
            that.position=data;
          }
        ).on('pressure', function(evt, data) {
          that.position=data;
          /*  that.debug({
              pressure: data
            });*/
        });
      },

      /*debug(obj) {

          function parseObj(sub, el) {
            for (var i in sub) {
              if (typeof sub[i] === 'object' && el) {
                parseObj(sub[i], el[i]);
              } else if (el && el[i]) {
                el[i].innerHTML = sub[i];
              }
            }
          }

        console.log(obj);
        this.position=obj;
        setTimeout(function() {
            parseObj(obj, this.els);
          }, 0);
      },*/


      deleteinit(){
//        console.log(this.inputvalue);
        var deletechannel=this.inputvalue
        var regdig = /^[0-9]*$/
        console.log('deletechannel ', deletechannel)
        if (!regdig.test( deletechannel) ||  deletechannel.length == 0) {
          console.log('not int');
        }else{
          deleteinit(deletechannel).then(res => {
            console.log(res)
            this.channellist=res.res
            return res
          }).catch(err => {
            console.log(err)
          })
        }
        this.loadinit();
      },
      sliderchange(i){
       console.log('i:',i);
        this.$socket.emit('message',{'username':this.username,'msg':i});
      },
      rangechange(){
      },
      inputchange(){
        this.channellist=[];
        console.log(this.inputvalue);
        var channle_count=this.inputvalue
        var regdig = /^[0-9]*$/
        console.log('input ', channle_count)
        if (!regdig.test( channle_count) ||  channle_count.length == 0) {
          console.log('not int');
        }else{
          for (var i=0;i<channle_count;i++){
            this.channellist.push({channel:i,min:this.min,max:this.max,currval:this.defaultval,channel_name:""});
          }
          console.log('channellist',this.channellist);
        }
      },
      posesent(){
        console.log('pose send');
        this.posedata=JSON.stringify(this.channellist);
        saveinit(this.channellist).then(res => {
          console.log(res)
          return res
        }).catch(err => {
          console.log(err)
        })
      },

      poseset(){
        console.log('pose send');
        this.posedata=JSON.stringify(this.channellist);
        poseset(this.channellist).then(res => {
          console.log(res)
          return res
        }).catch(err => {
          console.log(err)
        })
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
<style scoped>
  body {
    margin: 0;
    padding: 0;
    margin-top: 20px;
    max-width: 1024px;
    margin-left: auto;
    margin-right: auto;
  }

  #buttons {
    position: relative;
    border: solid 1px #aaa;
    display: inline-block;
    width: 100%;
    border-radius: 10px;
    height: 50px;
    overflow: hidden;
    margin-bottom: 20px;
    box-sizing: border-box;
  }

  .button {
    display: inline-block;
    background: #ccc;
    color: black;
    height: 50px;
    width: 33%;
    margin: 0;
    margin-right: -3px;
    text-align: center;
    line-height: 45px;
    font-size: 25px;
    cursor: pointer;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }

  .button:hover {
    background: #eee;
  }

  .button:active {
    background: #ddd;
  }

  .button.active {
    color: white;
    background: #888;
  }

  .button:nth-child(2) {
    width: 34%;
    border-left: solid 1px #aaa;
    border-right: solid 1px #aaa;
  }

  .highlight {
    display: none;
  }

  .highlight.active {
    display: block;
  }

  .zone {
    display: none;
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
  }

  .zone.active {
    display: block;
  }

  .zone > h1 {
    position: absolute;
    padding: 10px 10px;
    margin: 0;
    color: white;
    right: 0;
    bottom: 0;
  }

  .zone.dynamic {
    background: rgba(0, 0, 255, 0.1);
  }

  .zone.semi {
    background: rgba(255, 255, 255, 0.1);
  }

  .zone.static {
    background: rgba(255, 0, 0, 0.1);
  }

</style>