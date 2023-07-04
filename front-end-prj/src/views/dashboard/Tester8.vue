<template>
  <div>
    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-card title="anima create" style="width: 100%">
          <a-row :gutter="48">
            <a-col  :md="4" :sm="24">
              <a-form-item  label="anima name:">
                <a-input :allowClear="true" v-decorator="['animaname', {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>
            <a-col  :md="4" :sm="24">
              <a-form-item label="totaltime">
                <a-input-number id="inputNumber" v-model="timeline" :min="1" :max="99" />
                <!--{{timeline}}-->
              </a-form-item>
            </a-col>
            <a-col  :md="4" :sm="24">
              <button @click="changeanima()">
                changeanima
              </button>
            </a-col>
            <a-col  :md="4" :sm="24">
              <button @click="updateanima()">
                update keyframe
              </button>
            </a-col>

          </a-row>
          <a-row :gutter="48">
            <div id="echarts" style="height: 290px; width: 90%;"></div>
          </a-row>
            <a-form-item :label='"curr timestamp "+this.timestamp'>
              <a-slider :min="0" :max="parseInt(this.timeline)" v-model="timestamp" @change="timesliderchange(timestamp)" :disabled="disabled" />
            </a-form-item>
          <a-form layout="inline">
            <div >
              channel count
            </div>
            <a-input v-model="inputvalue" ></a-input>
           <!-- <button @click="loadinit()">
              initial load
            </button>-->
            <button @click="saveanima()">
              save keyframe
            </button>
            <div>
              <a-row :gutter="48">
                <!--<a-form-item  v-if='i.channel!=0&&i.channel!=2' v-for="i in channellist":label="'channel '+i.channel.toString()+':'">-->
                  <a-form-item  v-if='i.channel!=0&&i.channel!=2' v-for="i in channellist":label="'channel '+i.channel.toString()+':'">
                   <!-- <a-form-item  v-if='i.channel!=0&&i.channel!=2&&i.channel!=3&&i.channel!=7' v-for="i in channellist":label="'channel '+i.channel.toString()+':'">-->
                    <div >
                      <a-col  :md="4" :sm="24">
                        <a-form-item ><a-input v-model="i.channel_name" @change="rangechange"></a-input></a-form-item>
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
                        <a-form-item ><a-input v-model="i.min" @change="rangechange"></a-input> </a-form-item>
                      </a-col>
                      <a-col :md="4" :sm="24">
                        <a-form-item ><a-input  v-model="i.max" @change="rangechange"></a-input></a-form-item>
                        <!--<a-form-item  :label=" 'name'"><a-input v-model="i.channel_name" @change="rangechange"></a-input></a-form-item>-->
                      </a-col>
                    </div>
                  </a-form-item>
              </a-row>
            </div>
          </a-form>
        </a-card>
      </a-form>
    </a-spin>
    <a-card>
      <a-row :gutter="48">
        <!--<a-col v-show='showjoy' :md="12" :sm="24">-->
          <a-col  :md="12" :sm="24">
          <div id="zone_joystick">
            <button @click="reset('eyeball')">
              reset
            </button>
            <div class="zone dynamic active"><h1>eyeball</h1></div>
            <div class="zone semi"><h1>semi</h1></div>
            <div class="zone static"><h1>static</h1></div>
            <!-- <div v-if="this.position!=''" id="debug">-->
            <div  id="debug">
              <ul v-if="this.position!=''">
                <!--            <li class="position">
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
                              angle :&lt;!&ndash;{{this.position.direction.angle}}&ndash;&gt;
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
                            </li>-->
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
          </div>
        </a-col>

          <a-col  :md="12" :sm="24"><!--  <a-col v-show='showjoy' :md="12" :sm="24">-->
          <button @click="reset('head')">
            reset
          </button>
          <div id="zone_joystick2">
            <div class="zone dynamic active"><h1>head</h1></div>
            <div class="zone semi"><h1>semi</h1></div>
            <div class="zone static"><h1>static</h1></div>
            <!-- <div v-if="this.position!=''" id="debug">-->
            <div  id="debug2">
              <ul v-if="this.position2!=''">
                <!--            <li class="position">
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
                              angle :&lt;!&ndash;{{this.position.direction.angle}}&ndash;&gt;
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
                            </li>-->
                <li class="direction">
                  vector :
                  <ul>
                    <li class="x">x : {{this.position2.vector.x}}</li>
                    <li class="y">y : {{this.position2.vector.y}}</li>
                  </ul>
                </li>
                <div class="dump"></div>
              </ul>
            </div>
          </div>
        </a-col>
      </a-row>
    </a-card>
    <a-card>
    <button @click="searchtable()">
      searchtable
    </button>
    <button @click="playanima()">
      playanima
    </button>
    <button @click="deleteanima()">
      deleteanima
    </button>
      <ag-grid-vue
        style="width: 94%; height: 200px"
        class="ag-theme-alpine"
        :columnDefs="columnDef"
        :defaultColDef="defaultColDef"
        :rowData="rowData"
        :gridOptions="gridOptions"
        @grid-ready="onGridReady"
      >
      </ag-grid-vue>
    </a-card>
  </div>
</template>

<script>
  import "ag-grid-community/dist/styles/ag-grid.css";
  import "ag-grid-community/dist/styles/ag-theme-alpine.css";
  import { AgGridVue } from "ag-grid-vue";
  import {search} from "@/api/tableapi.js";
  import nipplejs from "nipplejs";
  import {playanima,saveanima,updateanima,loadinit,deleteanima}from "@/api/poseapi.js"
  import AInput from 'ant-design-vue/lib/input/Input'
  export default {
    name: 'tester8',
    components:{
      AgGridVue,
      AInput,
      nipplejs,
    },

    data() {
      return {
        showjoy:false,
        socketdata:'',//websocket 数据定义
        rowData:null,//展示数据定义
        columnDef:null,//字段定义
        gridApi: null,
        columnApi: null,
        gridApi2: null,
        columnApi2: null,
        gridOptions:'',//aggriud 功能定义
        queryParam: {}, // 查询参数
        timestamp:0,
        disabled:false,
        labelCol: {
          xs: { span: 24 },
          sm: { span: 7 }
        },
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 13 }
        },
        visible: false,
        confirmLoading: false,
        form: this.$form.createForm(this),

        inputvalue:'',
        currdataset:[],
        channellist:[],
        min:70,
        max:170,
        defaultval:120,
        posedata:'',
        joystick:null,
        position:'',
        joystick2:null,
        position2:'',
        els:null,
        nbEvents:0,
        timeline:0,
        valdaterule:{
            timeline:{
              rules: [{required: true, type:'number',max:2, message: 'in put number ,1-99'}]
            }
        },

        defaultColDef: {
          flex: 1,
          minWidth: 150,
          sortable: true,
          filter: true,
        },
        myChart:null,
        option:{
          title: {
            text: 'KeyframeCurve'
          },
          // 提示框
          tooltip: {},
          // 图例
          legend: {
            data: ['eyelidud','mouthud','neckleft','neckright','eyeud','eyelr','headud','headrate'],
            type: 'scroll',
            orient: 'vertical',
            right: 0,
            top: 60,
            bottom: 20,

          },
          // 表示x轴坐标
          xAxis: {
            data: ['1s', '2s', '3s', '4s', '5s', '6s']
          },
          // 表示y轴坐标
          yAxis: {
            type: 'value',
            min:350,
            max:600,
          },
          //
          series: [
            /*{
              name: 'channelname',
              type: 'line',
              data: [3500, 2200, 4500, 6500, 200, 3000]
            }*/
          ],
          dataZoom: [
            {
              type: 'slider',
              show: true,
              xAxisIndex: [0],
              start: 1,
              end: 100
            },
            {
              type: 'inside',
              xAxisIndex: [0],
              start: 1,
              end: 100
            },
           /* {
              type: 'slider',
              show: true,
              yAxisIndex: [0],
              left: '70%',
              start: 1,
              end: 100
            },

            {
              type: 'inside',
              yAxisIndex: [0],
              start: 1,
              end: 100
            }*/
          ],
        },

      }
    },
    beforeMount() {
      this.columnDef = [
        { field: "make" },
        { field: "model" },
        { field: "price" },
      ];

      this.rowData = [
        { make: "Toyota", model: "Celica", price: 35000 },
        { make: "Ford", model: "Mondeo", price: 32000 },
        { make: "Porsche", model: "Boxster", price: 72000 },
      ];
    },
    mounted(){
      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
                this.socketdata=this.socketdata+'\n'+JSON.stringify(data);
                /*console.log(this.socketdata);*/
            });
      this.elDebug=document.getElementById('debug');
      this.elDebug2=document.getElementById('debug2');
      this.drawjoystick();
      this.initCharts();
    },

    methods: {

      initCharts(){
        // 基于准备好的dom，初始化echarts实例
        this.myChart = this.$echarts.init(document.getElementById('echarts'));

        //Draw chart
        this.myChart.setOption(this.option);
      },

      drawjoystick(){
        console.log('draw joystick');
        /*var options = {
          zone: document.getElementById('zone_joystick'),
        };*/
        let joyCon = document.querySelector("#zone_joystick");
        let joyCon2 = document.querySelector("#zone_joystick2");
        // let joyCon =document.getElementById('zone_joystick'),
        // eslint-disable-next-line no-debugger
        let joyoptions = {
          mode: "dynamic",// 'dynamic', 'static' or 'semi'
          size: 300,
          color:"#3e3232d9",
          /*position: {
            left: "50%",
            top: "50%"
          },//在容器内垂直居中显示*/
          // zone: s('.zone.dynamic'),
          multitouch: true,
          zone: joyCon //如果不提提供zone容器元素，那么默认动态生成的元素是注入在body中的。
        };
        let joyoptions2 = {
          mode: "dynamic",// 'dynamic', 'static' or 'semi'
          size: 300,
          color:"#3e3232d9",
          /*position: {
            left: "50%",
            top: "50%"
          },//在容器内垂直居中显示*/
          // zone: s('.zone.dynamic'),
          multitouch: true,
          zone: joyCon2 //如果不提提供zone容器元素，那么默认动态生成的元素是注入在body中的。
        };
        this.joystick = nipplejs.create(joyoptions);
        this.joystick2 = nipplejs.create(joyoptions2);
        this.bindNipple();
        // Get debug elements and map them
      },
      /*joydump(evt){
        var that=this;
        var elDump = this.elDebug.querySelector('.dump');
        setTimeout(function() {
          if (elDump.children.length >=1) {
            elDump.removeChild(elDump.firstChild);
          }
          var newEvent = document.createElement('div');
          newEvent.innerHTML = '#' + that.nbEvents+ ' : <span class="data">' +
            evt + '</span>';
          elDump.appendChild(newEvent);
          that.nbEvents += 1;
        }, 0);
      },*/
      bindNipple(){
        var that=this;
        this.joystick.on('start end', function(evt, data) {
         /* that.joydump(evt.type);
          that.position=data;*/
          /*that.debug(data);*/
        }).on('move', function(evt, data) {
          /*that.debug(data);*/
          that.position=data;
          /*console.log(that.position.vector);*/
          /*console.log(that.position.vector.x.toFixed(2),that.position.vector.y.toFixed(2))*/
          var distance0=that.channellist[0].max-that.channellist[0].min;
          /*console.log('distance0:',parseInt(that.channellist[0].min)+distance0/2+distance0/2*that.position.vector.x.toFixed(2))*/
          var result=parseInt(parseInt(that.channellist[0].min)+distance0/2-distance0/2*that.position.vector.y.toFixed(2));
          /*console.log('result:',result)*/
          that.channellist[0].currval=result;
          var distance2=that.channellist[2].max-that.channellist[2].min;
          /*console.log('distance0:',parseInt(that.channellist[0].min)+distance0/2+distance0/2*that.position.vector.x.toFixed(2))*/
          var result2=parseInt(parseInt(that.channellist[2].min)+distance2/2+distance2/2*that.position.vector.x.toFixed(2));
          that.channellist[2].currval=result2;
          that.$socket.emit('message',{'username':this.username,'msg':that.channellist[0]});
          that.$socket.emit('message',{'username':this.username,'msg':that.channellist[2]});
        }).on('dir:up plain:up dir:left plain:left dir:down ' +
          'plain:down dir:right plain:right',
          function(evt, data) {
            /*that.joydump(evt.type);
            that.position=data;*/
          }
        ).on('pressure', function(evt, data) {
         /* that.position=data;*/
          /*  that.debug({
              pressure: data
            });*/
        });
        this.joystick2.on('start end', function(evt, data) {
          /* that.joydump(evt.type);
           that.position=data;*/
          /*that.debug(data);*/
        }).on('move', function(evt, data) {
          /*that.debug(data);*/
          that.position2=data;
          /*console.log(that.position.vector);*/
          /*console.log(that.position2.vector.x.toFixed(2),that.position2.vector.y.toFixed(2))*/
          var distance3=that.channellist[3].max-that.channellist[3].min;
          /*console.log('distance0:',parseInt(that.channellist[0].min)+distance0/2+distance0/2*that.position.vector.x.toFixed(2))*/
          var result3=parseInt(parseInt(that.channellist[3].min)+distance3/2+distance3/2*that.position2.vector.y.toFixed(2));
         /* console.log('result:',result3)*/
          that.channellist[3].currval=result3;
          var distance7=that.channellist[7].max-that.channellist[7].min;
          /*console.log('distance0:',parseInt(that.channellist[0].min)+distance0/2+distance0/2*that.position.vector.x.toFixed(2))*/
          var result7=parseInt(parseInt(that.channellist[7].min)+distance7/2+distance7/2*that.position2.vector.x.toFixed(2));
          that.channellist[7].currval=result7;
          that.$socket.emit('message',{'username':this.username,'msg':that.channellist[3]});
          that.$socket.emit('message',{'username':this.username,'msg':that.channellist[7]});

        }).on('dir:up plain:up dir:left plain:left dir:down ' +
          'plain:down dir:right plain:right',
          function(evt, data) {
            /*that.joydump(evt.type);
            that.position=data;*/
          }
        ).on('pressure', function(evt, data) {
          /* that.position=data;*/
          /*  that.debug({
              pressure: data
            });*/
        });
      },
      reset(val){
        var that=this
        if (val=='eyeball'){
          //reset eyeball position
            var distance0=that.channellist[0].max-that.channellist[0].min;
            var result=parseInt(parseInt(that.channellist[0].min)+distance0/2);
            that.channellist[0].currval=result;
            var distance2=that.channellist[2].max-that.channellist[2].min;
            var result2=parseInt(parseInt(that.channellist[2].min)+distance2/2);
            that.channellist[2].currval=result2;
            that.$socket.emit('message',{'username':this.username,'msg':that.channellist[0]});
            that.$socket.emit('message',{'username':this.username,'msg':that.channellist[2]});
        } else if(val=='head'){
          //reset head position
            var distance3=that.channellist[3].max-that.channellist[3].min;
            var result3=parseInt(parseInt(that.channellist[3].min)+distance3/2);
            that.channellist[3].currval=result3;
            var distance7=that.channellist[7].max-that.channellist[7].min;
            var result7=parseInt(parseInt(that.channellist[7].min)+distance7/2);
            that.channellist[7].currval=result7;
            that.$socket.emit('message',{'username':this.username,'msg':that.channellist[3]});
            that.$socket.emit('message',{'username':this.username,'msg':that.channellist[7]});
        }
      },
      loadinit(){
        this.channellist=[];
        this.posedata='';
        this.showjoy=true;
        this.socketdata='';
        loadinit().then(res => {
          console.log(res)
          var item
          for(item in res.res){
            /*console.log(res.res[item].currval);*/
            res.res[item].currval=parseInt(res.res[item].currval);
           /* item.currval=parseInt(item.currval)
            console.log(item.currval);*/
          }
          this.channellist=res.res
          return res
        }).catch(err => {
          console.log(err)
        })
      },
      changeanima(){
        var that=this;
        var timeserials=[];
        var series=[];
        series.push(
          {
            name:'curr keyframe',
            type:'line',
            color: '#f60100',
            markLine: {
              data: [
                {xAxis:this.timestamp
                  /*  function(){
                    console.log(this.timestamp)
                    if (this.timestamp>=0){
                      return this.timestamp
                    }else{
                      return 1
                    }
                  } */
                },
                /*{ xAxis: 16 },*/
                /*{coord:[new Date().getHours(),300]}*/
              ],
              label: {
                normal: {
                  show: true,
                  position: 'end',
                  formatter: new Date().getHours()
                },
              },
            }
          }
        );
        console.log('change anima');

        var animaname=this.form.getFieldValue('animaname');
        this.gridApi.setColumnDefs(
          [
            {
              field: 'animation_name',
              filterParams: {
                filterOptions: ['contains', 'startsWith', 'endsWith'],
                defaultOption: 'contains',
              },
            },
            {field: 'channel'},
            {field: 'channel_name'},
            {field: 'channel_value'},
            {field: 'time_stamp'},
            {field: 'timeline'},
          ])
        if(animaname===undefined||animaname==""){
          this.$notification.open({
            message: 'Notification',
            description:
              "animaname can't be null!",
            onClose: close,
          });
        }else{
          search( JSON.stringify({animaname:animaname}))
            .then(res => {
              console.log('search function calling')
              /*console.log(res.res)*/
              res.res.sort((a,b)=>{ return a.time_stamp-b.time_stamp})//升序
              that.gridApi.setRowData(res.res);
              that.currdataset=res.res;
              that.timeline=res.res[0]['timeline'];
              for (var timestamp=0;timestamp<parseInt(res.res[0]['timeline'])+1;timestamp++){
                /*console.log(timestamp)*/
                timeserials.push(String((timestamp*0.2).toFixed(1))+'S')
              }
              that.option.xAxis.data=timeserials
              /*console.log(that.option.xAxis.data)*/
              /*  series: [
                  {
                    name: 'channelname',
                    type: 'line',
                    data: [3500, 2200, 4500, 6500, 200, 3000]
                  }
                ],*/
              var checke_list=[]
              for(var i in res.res){
                // console.log(res.res[i].time_stamp)
                /*console.log(res.res[i].channel_name)*/
                if (checke_list.indexOf(res.res[i].channel_name)==-1){
                  //if newline
                  checke_list.push(res.res[i].channel_name);
                  // console.log(res.res[i].channel_value)
                  series.push({name:res.res[i].channel_name,type: 'line',data:[]})
                  var newline_index=series.findIndex(item=>item.name==res.res[i].channel_name);
                  if (parseInt(res.res[i].time_stamp)>0){
                    //if start from timestamp 3 add blank data to before timestamp
                    for(var j=0;j<parseInt(res.res[i].time_stamp);j++){
                      series[newline_index].data.push(null);
                    }
                  }
                  series[newline_index].data.push(parseInt(res.res[i].channel_value));
                }else{
                  //if exisit line
                  var oldline_index=series.findIndex(item=>item.name==res.res[i].channel_name);

                  //if stimestamp form 1 to 5 then need add 5-1-1 blank data
                  var step=parseInt(res.res[i].time_stamp)-series[oldline_index].data.length
                  if(step>1){
                    for(var k=0;k<step;k++){
                      series[oldline_index].data.push(null);
                    }
                  }
                  //push new channel value
                  series[oldline_index].data.push(parseInt(res.res[i].channel_value));
                }
              }
              that.option.series=series;
              //console.log(series);
              //redraw chart
              that.myChart.setOption(that.option);
              that.loadinit()
              return res.res
            }).catch(err => {
            console.log(err)
          })
        }
      },
      saveanima(){
        console.log('save anima');
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname=this.form.getFieldValue('animaname');
        for(var i in this.channellist){
          this.channellist[i].animaname=animaname;
          this.channellist[i].timeline=this.timeline;
          this.channellist[i].timestamp=this.timestamp;
        };
        console.log(this.channellist)
       /* this.posedata=JSON.stringify(this.channellist);*/
        saveanima(this.channellist).then(res => {
          console.log(res)
          return res
        }).catch(err => {
          console.log(err)
        })
      },
      updateanima(){
        var that=this;
        console.log('update anima');
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname=this.form.getFieldValue('animaname');
        for(var i in this.channellist){
          this.channellist[i].animaname=animaname;
          this.channellist[i].timeline=this.timeline;
          this.channellist[i].timestamp=this.timestamp;
        };
        console.log(this.channellist)
        /* this.posedata=JSON.stringify(this.channellist);*/
        if(animaname===undefined||animaname==""){
          this.$notification.open({
            message: 'Notification',
            description:
              "animaname can't be null!",
            onClose: close,
          });
        }else{
          updateanima(this.channellist).then(res => {
            console.log(res)
            that.changeanima();
            return res
          }).catch(err => {
            console.log(err)
          })
        }
      },

      playanima(){

        console.log('play anima');
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname=this.form.getFieldValue('animaname');
        console.log(animaname);
        /* this.posedata=JSON.stringify(this.channellist);*/
        if(animaname===undefined||animaname==""){
          this.$notification.open({
            message: 'Notification',
            description:
              "animaname can't be null!",
            onClose: close,
          });
        }else{
          playanima(JSON.stringify({animaname:animaname})).then(res => {
            console.log(res)
            return res
          }).catch(err => {
            console.log(err)
          })
        }

      },
      deleteanima(){
        console.log('play anima');
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname=this.form.getFieldValue('animaname');
        /* this.posedata=JSON.stringify(this.channellist);*/
        deleteanima(JSON.stringify({animaname:animaname})).then(res => {
          console.log(res)
          return res
        }).catch(err => {
          console.log(err)
        })
      },

      onGridReady(params){
        //ongrid ready
        this.gridApi = params.api;
        this.columnApi = params.columnApi;
        this.loadinit();
        this.searchtable();

      },
      animecreate(){
        console.log('anime create')
        this.visible = true;

       /* this.elDebug=document.getElementById('debug');
        this.drawjoystick();*/

      },

      rangechange(){
      },

      sliderchange(i){
        console.log('i:',i);
        this.$socket.emit('message',{'username':this.username,'msg':i});
      },
      timesliderchange(){
        var that=this;
        //console.log('before chartoption:',that.option.series[0].markLine.data[0].xAxis);
        that.option.series[0].markLine.data[0].xAxis=this.timestamp;
        //console.log('after chartoption:',that.option.series[0].markLine.data[0].xAxis);
        that.myChart.setOption(that.option);
        console.log('curr timestamp:',this.timestamp);
        /*console.log(this.currdataset);*/
        var filterarry=[].concat(that.currdataset);
        console.log(that.currdataset.length);
        console.log(filterarry.length);
        var item;
        //console.log(this.channellist);
        var tempindex=0;

        while(tempindex>-1){
          //get curr timestamp dataset
          tempindex=filterarry.findIndex(item=>item.time_stamp==that.timestamp);
          if(tempindex>-1){
            //get curr timestamp dataset
            item=filterarry[tempindex]
            var channelindex= that.channellist.findIndex(channelitem=>channelitem.channel==item.channel);

            //set relate channel status by channel number
            if(parseInt(item.channel_value)>0){
                console.log(that.channellist[channelindex].channel,item.channel_value);
                that.channellist[channelindex].currval=parseInt(item.channel_value);
                that.$socket.emit('message',{'username':that.username,'msg':that.channellist[channelindex]});
            };

          };
          filterarry.splice(0,tempindex+1);
          // console.log(that.currdataset.length);
        }
        /*console.log(that.currdataset.length);
        console.log(this.channellist);*/
      },
      loadingbytimeslider(){
        // console.log('curr timestamp:',this.timestamp);

      },


      test(){

        console.log(this.columnDef)

        this.gridApi.setColumnDefs([
          {field: 'animation_name' ,
            filterParams: {
            filterOptions: ['contains', 'startsWith', 'endsWith'],
            defaultOption: 'contains',
            },
          },
          {field: 'channel'},
          {field: 'channel_name'},
          {field: 'channel_value'},
          {field: 'time_stamp'},
        ])

      },
      websocketsent(){

        console.log('message send',{'username':this.username,'msg':'hahahahahha'})
//        this.$socket.emit('subscribe',{'username':this.username,'table':'Z_UI_ASN_GR'});
        this.socketdata=this.socketdata+'\n'+'hahahahahha';
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
      },
      searchtable () {
        var that=this
//                debugger
        console.log('searchtable');
        // const value = this.queryParam

        this.gridApi.setColumnDefs(
          [
            {
              field: 'animation_name',
              filterParams: {
                filterOptions: ['contains', 'startsWith', 'endsWith'],
                defaultOption: 'contains',
              },
            },
          {field: 'channel'},
          {field: 'channel_name'},
          {field: 'channel_value'},
          {field: 'time_stamp'},
          {field: 'timeline'},
        ])
//       debugger;
        /*console.log(this.rowData)
        console.log('search.parameter', this.queryParam)*/
        let paramters = {"pageNum": 1, "pageSize": 100000};
        search(Object.assign(paramters, this.queryParam))
          .then(res => {
            console.log('search function calling')
            /*console.log(res.res)*/
            /*that.rowData = res.res*/
            /*that.gridApi.setRowData(res.res)*/
            that.gridApi.setRowData(res.res)
            that.currdataset=res.res
            /*that.searchLoading = false;*/
//          that.$refs.table.clearSelected();
            /*that.$refs.agtable.clearSelected();*/
            //刷新 Ag-grid dataset
            /*that.rowData = res.result.list*/
            return res.result
          }).catch(err => {
          console.log(err)
        })
      },
    }
  }
</script>
<style scoped>
 /* .full-modal {
    .ant-modal {
      max-width: 100%;
      top: 0;
      padding-bottom: 0;
      margin: 0;
    }
    .ant-modal-content {
      display: flex;
      flex-direction: column;
      height: calc(100vh);
    }
    .ant-modal-body {
      flex: 1;
    }
  }*/

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
    color: #5d000b;
    right: 0;
    bottom: 0;
  }

  .zone.dynamic {
    /*background: rgba(0, 0, 255, 0.1);*/
    background: rgba(24, 144, 255, 0.2);

  }

  .zone.semi {
    background: rgba(255, 255, 255, 0.1);
  }

  .zone.static {
    background: rgba(255, 0, 0, 0.1);
  }

</style>