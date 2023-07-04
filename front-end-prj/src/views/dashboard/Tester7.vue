<template>
  <div>
    <div >
      hahah
    </div>
  <!--  <button @click="test()">
      test
    </button>-->
    <button @click="websocketsent()">
      websocket
    </button>
    <button @click="searchtable()">
      searchtable
    </button>
    <p>
      {{ this.socketdata}}
    </p>
      <ag-grid-vue
        style="width: 94%; height: 200px"
        class="ag-theme-alpine"
        :columnDefs="columnDef"
        :rowData="rowData"
        :gridOptions="gridOptions"
        @grid-ready="onGridReady"
      >
      </ag-grid-vue>

  </div>
</template>

<script>
  import "ag-grid-community/dist/styles/ag-grid.css";
  import "ag-grid-community/dist/styles/ag-theme-alpine.css";
  import { AgGridVue } from "ag-grid-vue";
  import {search} from "@/api/tableapi.js";
  export default {
    name: 'tester7',
    components:{
      AgGridVue
    },

    data() {
      return {
        socketdata:'',//websocket 数据定义
        rowData:null,//展示数据定义
        columnDef:null,//字段定义
        gridApi: null,
        columnApi: null,
        gridOptions:'',//aggriud 功能定义
        queryParam: {}, // 查询参数
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
      onGridReady(params){
        //ongrid ready
        this.gridApi = params.api;
        this.columnApi = params.columnApi;
      },
      test(){

        console.log(this.columnDef)

        this.gridApi.setColumnDefs([{field: 'animation_name'},
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
          [{field: 'animation_name'},
          {field: 'channel'},
          {field: 'channel_name'},
          {field: 'channel_value'},
          {field: 'time_stamp'},
        ])

//                    debugger;
        /*console.log(this.rowData)
        console.log('search.parameter', this.queryParam)*/
        let paramters = {"pageNum": 1, "pageSize": 100000};
        search(Object.assign(paramters, this.queryParam))
          .then(res => {
            console.log('search function calling')
            console.log(res.res)
            /*that.rowData = res.res*/
            that.gridApi.setRowData(res.res)



            /*that.searchLoading = false;*/
//                            that.$refs.table.clearSelected();
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
