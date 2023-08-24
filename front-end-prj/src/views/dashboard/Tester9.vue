<template>
  <div>
    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-card title="voice asset" style="width: 100%">
          <a-row :gutter="48">
            <a-col  :md="4" :sm="24">
              <a-form-item  label="Text:">
                <a-input :allowClear="true" v-decorator="['speechtext', {rules: [{required: true, message: 'not null!'}]}]" />
              </a-form-item>
            </a-col>
            <a-col  :md="4" :sm="24">
              <a-form-item  label="language:">
              <a-dropdown-button @click="handleButtonClick" v-decorator="['currlanguage', {rules: [{required: true, message: 'only zh/jp/en'}]}]">
                {{this.currlanguage}}
                <template #overlay>
                  <a-menu @click="handleMenuClick">
                    <a-menu-item key="zh">
                      <UserOutlined />
                      zh
                    </a-menu-item>
                    <a-menu-item key="en">
                      <UserOutlined />
                      en
                    </a-menu-item>
                    <a-menu-item key="jp">
                      <UserOutlined />
                      jp
                    </a-menu-item>
                  </a-menu>
                </template>
              </a-dropdown-button>
              </a-form-item>
            </a-col>
            <a-col  :md="4" :sm="24">
              <button @click="get_voice()">
                get voice
              </button>
            </a-col>
            <a-col  :md="4" :sm="24">
              <button @click="playvoice()">
                playvoice
              </button>
            </a-col>
            <a-col  :md="4" :sm="24">
              <button @click="savevoice()">
                save voice
              </button>
            </a-col>
          </a-row>
            <a-form-item :label='"Pitch shift steps "+this.steps'>
              <a-slider :min="-5" :max="5" v-model="steps" @change="timesliderchange(steps)" :disabled="disabled" />
            </a-form-item>
          <a-form layout="inline">
            <div >
              Speech Mean
            </div>
            <a-input v-model="speechmean" ></a-input>

            <div>
              <a-row :gutter="48">
                <!--<a-form-item  v-if='i.channel!=0&&i.channel!=2' v-for="i in channellist":label="'channel '+i.channel.toString()+':'">-->
                  <a-form-item  v-if='i.channel!=0&&i.channel!=2&&i.channel!=3&&i.channel!=7' v-for="i in channellist":label="'channel '+i.channel.toString()+':'">
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
      Voice Asset
      <br/>
    <button @click="searchtable()">
      searchtable
    </button>
    <button @click="playasset()">
      playasset
    </button>
      <ag-grid-vue
        style="width: 94%; height: 200px"
        class="ag-theme-alpine"
        :columnDefs="columnDef"
        :rowData="rowData"
        :gridOptions="gridOptions"
        :rowSelection="rowSelection"
        @grid-ready="onGridReady"
        @cell-clicked="onCellClicked"
        @selection-changed="onSelectionChanged"
      >
      </ag-grid-vue>
    </a-card>
  </div>
</template>
<script>
  import "ag-grid-community/dist/styles/ag-grid.css";
  import "ag-grid-community/dist/styles/ag-theme-alpine.css";
  import { AgGridVue } from "ag-grid-vue";
  import {searchvoice,getvoice,playvoice,playasset,savevoice} from "@/api/voiceapi.js";
  import AInput from 'ant-design-vue/lib/input/Input'
  export default {
    name: 'tester9',
    components:{
      AgGridVue,
      AInput,
    },
    data() {
      return {
        selectedAsset:'',
        rowSelection:'single',
        currlanguage:'select language',
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
        steps:0,
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

        speechmean:'',
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
    },

    methods: {

      handleMenuClick(Event){
        console.log('item select click', Event.key);
        this.currlanguage=Event.key;
      },
      handleButtonClick(){
        console.log('click');
      },
      get_voice(){
        let speechtext = this.form.getFieldValue('speechtext');
        let languagetype=this.currlanguage;
        console.log('get voice:',speechtext,languagetype);
        getvoice(JSON.stringify({speechtext:encodeURIComponent(speechtext),languagetype:languagetype})).then(res => {
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
        this.searchtable();
      },
      onCellClicked(){
        // console.log('onCellClicked');
      },
      onSelectionChanged() {
        const selectedRows = this.gridApi.getSelectedRows();
        this.selectedAsset=selectedRows[0].asset_path;
        console.log('onSelectionChanged'+selectedRows[0].asset_path);
      },
      rangechange(){
      },
      sliderchange(i){
        /*console.log('i:',i);*/
        this.$socket.emit('message',{'username':this.username,'msg':i});
      },
      timesliderchange(){
        console.log('curr steps:',this.steps);
      },
      websocketsent(){
        console.log('message send',{'username':this.username,'msg':'hahahahahha'})
//        this.$socket.emit('subscribe',{'username':this.username,'table':'Z_UI_ASN_GR'});
        this.socketdata=this.socketdata+'\n'+'hahahahahha';
        this.$socket.emit('message',{'username':this.username,'msg':'hahahahahha'});
         /*this.sockets.subscribe('response', (data) => {
             console.log('server sent response from onSwitchChange function');
             console.log(data,'if data change,can call refresh function locally');
         });
         this.sockets.subscribe('refreshdata', (data) => {
             console.log(data,'if data change,can call refresh function locally');
             this.renderChart(data)
         });*/
      },
      savevoice(){
        var that=this
//                debugger
        console.log('save voice');
        var speechtext = this.form.getFieldValue('speechtext');
        var languagetype=this.currlanguage;
        var steps=this.steps;
        var mean=this.speechmean;
        console.log(speechtext,mean,languagetype,steps);
        var param={speechtext:speechtext,mean:mean,languagetype:languagetype,steps:steps};
        savevoice(JSON.stringify(param))
          .then(res => {
            console.log('save function calling')
            console.log(res.res)
            that.gridApi.setRowData(res.res)
            return res.result
          }).catch(err => {
          console.log(err)
        })
      },
      playvoice(){
        var that=this
//                debugger
        console.log('play voice');

        var param={steps:this.steps};
        playvoice(JSON.stringify(param))
          .then(res => {
            console.log('search function calling')
            /*console.log(res.res)*/
            that.gridApi.setRowData(res.res)
            return res.result
          }).catch(err => {
          console.log(err)
        })

      },
      playasset(){
        var that=this
//                debugger
        console.log('play asset',this.selectedAsset);
        // that.
        var param={steps:this.steps,asset:this.selectedAsset};
        playasset(JSON.stringify(param))
          .then(res => {
            console.log('search function calling')
            /*console.log(res.res)*/
            // that.gridApi.setRowData(res.res)
            return res.result
          }).catch(err => {
          console.log(err)
        })

      },
      searchtable () {
        var that=this
//                debugger
        console.log('searchtable');
        // const value = this.queryParam
        this.gridApi.setColumnDefs(
          [{field: 'asset_id'},
          {field: 'text'},
          {field: 'asset_path'},
            {field: 'mean'},
            {field: 'language_type'},
            {field: 'steps'},
            {field: 'duration'},
        ])
//                    debugger;
        /*console.log(this.rowData)
        console.log('search.parameter', this.queryParam)*/
        let paramters = {"pageNum": 1, "pageSize": 100000};
        searchvoice(Object.assign(paramters, this.queryParam))
          .then(res => {
            console.log('search function calling')
            console.log(res.res)
            that.gridApi.setRowData(res.res)
            return res.result
          }).catch(err => {
          console.log(err)
        })
      },
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