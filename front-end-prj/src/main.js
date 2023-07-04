// ie polyfill
import '@babel/polyfill'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/'
import { VueAxios } from './utils/request'

// mock
// import './mock'

import bootstrap from './core/bootstrap'
import './core/use'
import './permission' // permission control
import './utils/filter' // global filter
import * as echarts from 'echarts'//echarts
Vue.prototype.$echarts = echarts

import '../node_modules/ag-grid-community/dist/styles/ag-grid.css';
import '../node_modules/ag-grid-community/dist/styles/ag-theme-balham.css';
import "ag-grid-vue";




//wuqi add 20220328
import nipplejs from 'nipplejs'
// web socket wuqi 20191129
import VueSocketio from 'vue-socket.io'

//support video js
import Video from 'video.js'
import 'video.js/dist/video-js.css'
Vue.prototype.$video = Video



Vue.config.productionTip = false

// mount axios Vue.$http and this.$http
Vue.use(VueAxios)

// web socket wuqi 20191129
Vue.use(new VueSocketio({
    debug: false,
     // connection: 'http://10.0.0.88:2222/test',//flask 地址
    connection: 'http://localhost:2222/test',//flask 地址
    // options: { reconnection: false}
    // options: { reconnection: false,path:'/test',transports: ['websocket', 'polling', 'flashsocket'] }// jango地址+端口，由后端提供
}))


new Vue({
  router,
  store,
  created: bootstrap,
  render: h => h(App)
}).$mount('#app')
