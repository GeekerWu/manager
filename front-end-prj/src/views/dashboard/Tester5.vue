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
  </div>
</template>
<script>
  import AInput from "ant-design-vue/es/input/Input";
  import {saveinit,loadinit,deleteinit}from "@/api/poseapi.js"
  export default {
    components: {AInput},
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
      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
                this.socketdata=(this.socketdata+'\n'+JSON.stringify(data)).substr(-400,400);
//                console.log(data);
            });
    },

    methods: {
      loadinit(){
        this.channellist=[];
        this.posedata='';
        this.socketdata='';
        loadinit().then(res => {
          console.log(res)
          this.channellist=res.res
          return res
        }).catch(err => {
          console.log(err)
        })
      },
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
//        console.log('i:',i);
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
