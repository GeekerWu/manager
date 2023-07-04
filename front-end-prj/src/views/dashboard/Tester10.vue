<template>
  <div>
    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-card title="event create" style="width: 100%">
          <a-row :gutter="48">
            <a-col :md="4" :sm="24">
              <a-form-item label="event name:">
                <a-input :allowClear="true"
                         v-decorator="['eventname', {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>
            <a-col :md="4" :sm="24">
              <a-form-item label="event condition:">
                <a-input :allowClear="true"
                         v-decorator="['eventcondition', {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>
            <a-col :md="4" :sm="24">
              <a-form-item label="anima name:">
                <a-input :allowClear="true"
                         v-decorator="['animaname', {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>
            <a-col :md="4" :sm="24">
              <a-form-item label="total keyfame">
                <a-input-number id="inputNumber" v-model="timeline" :min="1" :max="99" />
                <!--{{timeline}}-->
              </a-form-item>
            </a-col>
            <!--<a-col :md="4" :sm="24">
            <button @click="loadvoice()">
              load voice
            </button>
            </a-col>-->
            <a-col :md="4" :sm="24">
              <button @click="loadanima()">
                load animation
              </button>
            </a-col>
            <a-col :md="4" :sm="24">
              <button @click="updateevent()">
                update event
              </button>
            </a-col>
          </a-row>

          <a-row :gutter="48">
            <a-col :md="8" :sm="24">
              <ag-grid-vue
                style="width: 100%; height: 200px"
                class="ag-theme-alpine"
                :columnDefs="voicecolumnDef"
                :defaultColDef="defaultColDef"
                :rowData="voicerowData"
                :gridOptions="voicegridOptions"
                :rowSelection="voicerowSelection"
                @row-selected="onRowSelected"
                @selection-changed="onSelectionChanged"
                @grid-ready="voiceonGridReady"
              >
              </ag-grid-vue>
            </a-col>
            <a-col :md="4" :sm="24">
              <a-form-item label="total voice">
                <a-input-number id="voice" :allowClear="false" @change='voicecountchange()' v-model="voicecount"
                                :min="0" :max="3" />
                <!--{{timeline}}-->
              </a-form-item>
            </a-col>
            <a-col :md="6" :sm="24">
              <ag-grid-vue
                style="width: 100%; height: 200px"
                class="ag-theme-alpine"
                :columnDefs="selectcolumnDef"
                :defaultColDef="defaultColDef"
                :rowData="selectrowData"
                :gridOptions="selectgridOptions"
                @grid-ready="selectonGridReady"
              >
              </ag-grid-vue>
            </a-col>



<!--    current antd version(1.4.0-beta.0) not support table transfer(1.5.0 needed)      :render="item => item.title"-->
          <!--  <a-transfer
              :data-source="voiceasset"
              :target-keys="targetKeys"
              :disabled="disabled"
              :render="item => item.title"
              :show-search="showSearch"
              :filter-option="(inputValue, item) => item.title.indexOf(inputValue) !== -1"
              :show-select-all="false"
              @change="handleChange"
            >
            </a-transfer>
            <a-switch
              un-checked-children="disabled"
              checked-children="disabled"
              :checked="disabled"
              style="margin-top: 16px"
              @change="triggerDisable"
            />
            <a-switch
              un-checked-children="showSearch"
              checked-children="showSearch"
              :checked="showSearch"
              style="margin-top: 16px"
              @change="triggerShowSearch"
            />-->



           <!-- <a-col :md="4" :sm="24">
              &lt;!&ndash; <a-form-item  label="voice name:">
                 <a-input :allowClear="false" v-decorator="['voicename', {rules: [{required: true, message: 'not null!'}]}]" />
               </a-form-item>&ndash;&gt;
              <a-form-item v-for="i in voicelist" :label="'voice name:'">
                <a-input :allowClear="false"
                         v-decorator="[i.name, {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>-->
          </a-row>

          <a-row :gutter="48">
            <div id="echarts" style="height: 290px; width: 90%;"></div>
          </a-row>
          <a-form-item :label='"KeyFrame "+(this.timestamp*0.2).toFixed(1)+ "s "'>
            <a-slider :min="0" :max="parseInt(this.timeline)" v-model="timestamp" @change="timesliderchange(timestamp)"
                      :disabled="disabled" />
          </a-form-item>
         <!-- /* {name: selectedRow.text,duration:selectedRow.duration,voicestart:0}*/-->
          <a-form-item v-for="i in voicelist" :label='i.name+" play at "+(i.voicestart*0.2).toFixed(1)+ "s "'>
            <a-slider :min="0" :max="parseInt(timeline)" v-model="i.voicestart"
                      @change="voicesliderchange(i)" :disabled="disabled" />
          </a-form-item>
          <a-form layout="inline">

            <button @click="save_event()">
              save keyframe
            </button>
          </a-form>
        </a-card>
      </a-form>
    </a-spin>
    <a-card>
      <button @click="searchtable()">
        searchtable
      </button>
      <button @click="playevent()">
        play event
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
  import 'ag-grid-community/dist/styles/ag-grid.css'
  import 'ag-grid-community/dist/styles/ag-theme-alpine.css'
  import { AgGridVue } from 'ag-grid-vue'
  import { searchevent, play_event, update_event } from '@/api/eventapi.js'
  import { searchvoice} from '@/api/voiceapi.js'
  import { search } from '@/api/tableapi.js'
  import { playanima, saveanima, updateanima, loadinit, deleteanima } from '@/api/poseapi.js'
  import AInput from 'ant-design-vue/lib/input/Input'

  export default {
    name: 'tester10',
    components: {
      AgGridVue,
      AInput,
    },

    data() {
      return {
        voicerowSelection:'multiple',
        voicelist:[],
         /* {name: selectedRow.text,duration:selectedRow.duration,voicestart:0}*/
      // {key: string.isRequired,title: string.isRequired,description: string,disabled: bool}

        voiceasset:[
          {key:'1',title:'voice1',description:'1',disabled:false},
          {key:'2',title:'voice2',description:'3',disabled:false},
          {key:'3',title:'voice3',description:'2',disabled:false},
        ],
        targetKeys: [],
        disabled: false,
        showSearch: true,
        leftColumns:[
          {
            dataIndex: 'title',
            title: 'Name',
          },
          {
            dataIndex: 'description',
            title: 'Description',
          },
        ],
        rightColumns:[
          {
            dataIndex: 'title',
            title: 'Name',
          },
        ],



        showjoy: false,
        socketdata: '',//websocket 数据定义
        rowData: null,//展示数据定义
        voicerowData: null,//展示数据定义
        selectrowData:null,
        columnDef: null,//字段定义
        voicecolumnDef: null,
        selectcolumnDef: null,
        gridApi: null,
        columnApi: null,
        voicegridApi: null,
        voicecolumnApi: null,
        selectgridApi: null,
        selectcolumnApi: null,
        gridOptions: '',//aggriud 功能定义
        voicegridOptions:'',
        selectgridOptions:'',
        queryParam: {}, // 查询参数
        timestamp: 0,
        voicestart: 0,
        disabled: false,
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

        inputvalue: '',
        currdataset: [],
        channellist: [],
        min: 70,
        max: 170,
        defaultval: 120,
        posedata: '',
        joystick: null,
        position: '',
        joystick2: null,
        position2: '',
        els: null,
        nbEvents: 0,
        timeline: 0,
        voicecount: 0,
        valdaterule: {
          timeline: {
            rules: [{ required: true, type: 'number', max: 2, message: 'in put number ,1-99' }]
          }
        },

        defaultColDef: {
          flex: 1,
          minWidth: 150,
          sortable: true,
          filter: true
        },
        //myechart obj
        myChart: null,
        option: {
          title: {
            text: 'KeyframeCurve'
          },
          // 提示框
          tooltip: {},
          // 图例
          legend: {
            data: ['eyelidud', 'mouthud', 'neckleft', 'neckright', 'eyeud', 'eyelr', 'headud', 'headrate'],
            type: 'scroll',
            orient: 'vertical',
            right: 0,
            top: 60,
            bottom: 20

          },
          // 表示x轴坐标
          xAxis: {
            data: ['1s', '2s', '3s', '4s', '5s', '6s']
          },
          // 表示y轴坐标
          yAxis: {
            type: 'value',
            min: 350,
            max: 600
          },
          //
          series: [
            /* {
               name: 'channelname',
               type: 'line',
               data: [3500, 2200, 4500, 6500, 200, 3000],
             },*/
            {
              name: 'markarea',
              type: 'line',
              markArea: {
                itemStyle: {
                  color: 'rgba(50,176,255,0.4)'
                },
                data: [
                  [
                    {
                      name: 'voice area',
                      xAxis: this.timestamp
                    },
                    {
                      xAxis: this.timestamp + 3

                    }
                  ]

                ]
              }
            },
            {
              name: 'curr keyframe',
              type: 'line',
              color: '#f60100',
              markLine: {
                data: [
                  {
                    xAxis: function() {
                      console.log(this.timestamp)
                      if (this.timestamp >= 0) {
                        return this.timestamp
                      } else {
                        return 1
                      }
                    }
                  }
                  /*{ xAxis: 16 },*/
                  /*{coord:[new Date().getHours(),300]}*/
                ],
                label: {
                  normal: {
                    show: true,
                    position: 'end',
                    formatter: new Date().getHours()
                  }
                }
              }
            }
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
            }
          ]
        }

      }
    },
    beforeMount() {
      this.columnDef = [
        { field: 'make' },
        { field: 'model' },
        { field: 'price' }
      ]

      this.rowData = [
        { make: 'Toyota', model: 'Celica', price: 35000 },
        { make: 'Ford', model: 'Mondeo', price: 32000 },
        { make: 'Porsche', model: 'Boxster', price: 72000 }
      ]
    },
    mounted() {
      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
        this.socketdata = this.socketdata + '\n' + JSON.stringify(data)
        /*console.log(this.socketdata);*/
      })
      this.initCharts()
    },

    methods: {

      onRowSelected(event) {
        /*console.log(event.node.data)
        window.alert(
          'row ' +
          event.node.data.text +
          ' selected = ' +
          event.node.isSelected()
        );*/
      },
      onSelectionChanged(event) {
        var selectedRow =this.voicegridApi.getSelectedRows();
        // console.log(selectedRow);
        this.selectgridApi.setRowData(selectedRow);
        var rowCount = event.api.getSelectedNodes().length;
        this.voicecount=rowCount;
        this.voicelist = []
        for (var i = 0; i < this.voicecount; i++) {
          this.voicelist.push({name:selectedRow[i].text,duration:selectedRow[i].duration,voicestart:0})
        }
        // window.alert('selection changed, ' + rowCount + ' rows selected');
      },

      voicecountchange() {
        console.log('voicecountchange', this.voicecount)
      },
      initCharts() {
        // 基于准备好的dom，初始化echarts实例
        this.myChart = this.$echarts.init(document.getElementById('echarts'))
        //Draw chart
        this.myChart.setOption(this.option)
      },
      loadinit() {
        this.channellist = []
        this.posedata = ''
        this.showjoy = true
        this.socketdata = ''
        loadinit().then(res => {
          // console.log(res)
          var item
          for (item in res.res) {
            /*console.log(res.res[item].currval);*/
            res.res[item].currval = parseInt(res.res[item].currval)
            /* item.currval=parseInt(item.currval)
             console.log(item.currval);*/
          }
          this.channellist = res.res
          return res
        }).catch(err => {
          console.log(err)
        })
      },
      loadvoice(){
        var that=this
//                debugger
        console.log('loadvoice');
        //set select col define
        this.selectgridApi.setColumnDefs(
          [
            {field: 'text',headerCheckboxSelection: false,checkboxSelection: false},
            {field: 'duration'},
          ])
        //set voice col define
        this.voicegridApi.setColumnDefs(
          [
            // {field: 'asset_id'},
            {field: 'text',headerCheckboxSelection: true,checkboxSelection: true},
            // {field: 'asset_path'},
            {field: 'duration'},
            {field: 'language_type'},
            {field: 'mean'},
            // {field: 'steps'},

          ])
//                    debugger;
        /*console.log(this.rowData)
        console.log('search.parameter', this.queryParam)*/
        let paramters = {"pageNum": 1, "pageSize": 100000};
        searchvoice(Object.assign(paramters, this.queryParam))
          .then(res => {
            console.log('search function calling')
            // console.log(res.res)
            that.voicegridApi.setRowData(res.res)
            that.selectgridApi.setRowData([])
            return res.result
          }).catch(err => {
          console.log(err)
        })

      },
      loadanima() {
        var that = this
        var timeserials = []
        var series = []
        series.push(
          {
            name: 'curr keyframe',
            type: 'line',
            color: '#f60100',
            markLine: {
              data: [{ xAxis: this.timestamp }],
              label: {
                normal: {
                  show: true,
                  position: 'end',
                  formatter: new Date().getHours()
                }
              }
            }
          }
        )
        // console.log('voice list',this.voicelist);
        for(var i in this.voicelist){
          // console.log(Math.round(this.voicelist[i].duration/0.2))
          series.push(
            {
              name: this.voicelist[i].name,
              type: 'line',
              markArea: {
                itemStyle: {
                  /*color: 'rgba(50,176,255,0.4)'*/
                },
                data: [
                  [
                    {
                      name: this.voicelist[i].name,
                      xAxis: that.timestamp
                    },
                    {
                      xAxis: that.timestamp + Math.round(this.voicelist[i].duration/0.2)
                    }
                  ]
                ]
              }
            }
          )
        }

        console.log('load anima')

        var animaname = this.form.getFieldValue('animaname')
        if (animaname === undefined || animaname == '') {
          this.$notification.open({
            message: 'Notification',
            description:
              'animaname can\'t be null!',
            onClose: close
          })
        } else {
          search(JSON.stringify({ animaname: animaname }))
            .then(res => {
              console.log('search function calling')
              /*console.log(res.res)*/
              res.res.sort((a, b) => {
                return a.time_stamp - b.time_stamp
              })//升序
              /* that.gridApi.setRowData(res.res);*/
              that.currdataset = res.res
              that.timeline = res.res[0]['timeline']
              for (var timestamp = 0; timestamp < parseInt(res.res[0]['timeline']) + 1; timestamp++) {
                /*console.log(timestamp)*/
                timeserials.push(String((timestamp * 0.2).toFixed(1)) + 's')
              }
              that.option.xAxis.data = timeserials
              var checke_list = []
              for (var i in res.res) {
                // console.log(res.res[i].time_stamp)
                /*console.log(res.res[i].channel_name)*/
                if (checke_list.indexOf(res.res[i].channel_name) == -1) {
                  //if newline
                  checke_list.push(res.res[i].channel_name)
                  // console.log(res.res[i].channel_value)
                  series.push({ name: res.res[i].channel_name, type: 'line', data: [] })
                  var newline_index = series.findIndex(item => item.name == res.res[i].channel_name)
                  if (parseInt(res.res[i].time_stamp) > 0) {
                    //if start from timestamp 3 add blank data to before timestamp
                    for (var j = 0; j < parseInt(res.res[i].time_stamp); j++) {
                      series[newline_index].data.push(null)
                    }
                  }
                  series[newline_index].data.push(parseInt(res.res[i].channel_value))
                } else {
                  //if exisit line
                  var oldline_index = series.findIndex(item => item.name == res.res[i].channel_name)

                  //if stimestamp form 1 to 5 then need add 5-1-1 blank data
                  var step = parseInt(res.res[i].time_stamp) - series[oldline_index].data.length
                  if (step > 1) {
                    for (var k = 0; k < step; k++) {
                      series[oldline_index].data.push(null)
                    }
                  }
                  //push new channel value
                  series[oldline_index].data.push(parseInt(res.res[i].channel_value))
                }
              }
              //console.log(series);
              that.option.series = series
              //redraw chart
              that.myChart.setOption(that.option)
              that.loadinit()
              return res.res
            }).catch(err => {
            console.log(err)
          })
        }
      },
      updateevent() {
        var that = this
        var eventlist=[]
        console.log('update event')
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname = this.form.getFieldValue('animaname')
        var eventname = this.form.getFieldValue('eventname')
        var eventcondition = this.form.getFieldValue('eventcondition')


        if (animaname === undefined || animaname == '') {
          this.$notification.open({
            message: 'Notification',
            description:
              'animaname can\'t be null!',
            onClose: close
          })
        } else if (eventname === undefined || eventname == '') {
          this.$notification.open({
            message: 'Notification',
            description:
              'eventname can\'t be null!',
            onClose: close
          })
        }else if (eventcondition === undefined || eventcondition == '') {
          this.$notification.open({
            message: 'Notification',
            description:
              'eventcondition can\'t be null!',
            onClose: close
          })
        }else {
          for(var i in this.voicelist){
            // console.log(this.voicelist[i])
            //item['event_name'],item['event_condition'] ,item['animation'],item['voice'],item['voice_start']
            eventlist.push({
              event_name:eventname,
              event_condition:eventcondition,
              animation:animaname,
              voice:this.voicelist[i].name,
              voice_start:this.voicelist[i].voicestart,
            })
          }
          console.log(eventlist)
          /* this.posedata=JSON.stringify(this.channellist);*/
          update_event(eventlist).then(res => {
            console.log(res)
            // that.loadanima()
            return res
          }).catch(err => {
            console.log(err)
          })
        }
      },

      playevent() {
        console.log('play anima')
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var eventname = this.form.getFieldValue('eventname')
        console.log(eventname)
        /* this.posedata=JSON.stringify(this.channellist);*/
        if (eventname === undefined || eventname == '') {
          this.$notification.open({
            message: 'Notification',
            description:
              'eventname can\'t be null!',
            onClose: close
          })
        } else {
          play_event(JSON.stringify({ eventname: eventname })).then(res => {
            console.log(res)
            return res
          }).catch(err => {
            console.log(err)
          })
        }
      },
      deleteanima() {
        console.log('play anima')
        /*console.log('header :',this.form.getFieldValue('animaname'),this.timeline,this.timestamp);*/
        var animaname = this.form.getFieldValue('animaname')
        /* this.posedata=JSON.stringify(this.channellist);*/
       /* deleteanima(JSON.stringify({ animaname: animaname })).then(res => {
          console.log(res)
          return res
        }).catch(err => {
          console.log(err)
        })*/
      },

      onGridReady(params) {
        //ongrid ready
        this.gridApi = params.api
        this.columnApi = params.columnApi
        this.loadinit();
        this.searchtable();
        this.loadvoice();

      },
      voiceonGridReady(params) {
        //ongrid ready
        this.voicegridApi = params.api
        this.voicecolumnApi = params.columnApi
       /* this.loadinit()
        this.searchtable()*/

      },
      selectonGridReady(params) {
        //ongrid ready
        this.selectgridApi = params.api
        this.selectcolumnApi = params.columnApi
        /*this.loadinit()
        this.searchtable()*/

      },
      animecreate() {
        console.log('anime create')
        this.visible = true

        /* this.elDebug=document.getElementById('debug');
         this.drawjoystick();*/

      },

      rangechange() {
      },

      voicesliderchange(voiceitem) {
        var that = this
        // console.log('voice item', voiceitem.name)
        // console.log(that.option.series)
        // console.log(that.option.series.findIndex(item => item.name == voiceitem.name))
        var serindex=that.option.series.findIndex(item => item.name == voiceitem.name);
        that.option.series[serindex].markArea.data[0][0].xAxis = voiceitem.voicestart
        that.option.series[serindex].markArea.data[0][1].xAxis = voiceitem.voicestart + Math.round(voiceitem.duration/0.2)
        //console.log('after chartoption:',that.option.series[0].markLine.data[0].xAxis);
        that.myChart.setOption(that.option)
        /*console.log('i:',i);*/
        /*this.$socket.emit('message',{'username':this.username,'msg':i});*/
      },
      timesliderchange() {
        var that = this
        //console.log('before chartoption:',that.option.series[0].markLine.data[0].xAxis);
        that.option.series[0].markLine.data[0].xAxis = this.timestamp
        //console.log('after chartoption:',that.option.series[0].markLine.data[0].xAxis);
        that.myChart.setOption(that.option)
        console.log('curr timestamp:', this.timestamp)
        /*console.log(this.currdataset);*/
        var filterarry = [].concat(that.currdataset)
        console.log(that.currdataset.length)
        console.log(filterarry.length)
        var item
        //console.log(this.channellist);
        var tempindex = 0
        while (tempindex > -1) {
          //get curr timestamp dataset
          tempindex = filterarry.findIndex(item => item.time_stamp == that.timestamp)
          if (tempindex > -1) {
            //get curr timestamp dataset
            item = filterarry[tempindex]
            var channelindex = that.channellist.findIndex(channelitem => channelitem.channel == item.channel)

            //set relate channel status by channel number
            if (parseInt(item.channel_value) > 0) {
              console.log(that.channellist[channelindex].channel, item.channel_value)
              that.channellist[channelindex].currval = parseInt(item.channel_value)
              that.$socket.emit('message', { 'username': that.username, 'msg': that.channellist[channelindex] })
            }
          }
          filterarry.splice(0, tempindex + 1)
          console.log(that.currdataset.length)
        }
        console.log(that.currdataset.length)
        console.log(this.channellist)
      },
      loadingbytimeslider() {
        //console.log('curr timestamp:',this.timestamp);
      },
      websocketsent() {
        console.log('message send', { 'username': this.username, 'msg': 'hahahahahha' })
        this.socketdata = this.socketdata + '\n' + 'hahahahahha'
        this.$socket.emit('message', { 'username': this.username, 'msg': 'hahahahahha' })
      },
      searchtable() {
        var that = this
        console.log('searchtable')
        //`asset_id` `event_name` `event_condition``animation` `voice``voice_start`
        this.gridApi.setColumnDefs(
          [
            { field: 'asset_id' },
            {
              field: 'event_name',
              filterParams: {
                filterOptions: ['contains', 'startsWith', 'endsWith'],
                defaultOption: 'contains'
              }
            },

            { field: 'event_condition' },
            { field: 'animation' },
            { field: 'voice' },
            { field: 'voice_start' }
          ])
//       debugger;
        /*console.log(this.rowData)
        console.log('search.parameter', this.queryParam)*/
        let paramters = { 'pageNum': 1, 'pageSize': 100000 }
        searchevent(Object.assign(paramters, this.queryParam))
          .then(res => {
            console.log('search function calling')
            that.gridApi.setRowData(res.res)
            that.currdataset = res.res
            return res.result
          }).catch(err => {
          console.log(err)
        })
      }
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