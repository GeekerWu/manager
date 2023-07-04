<template>
  <div id="parent">
    <div>
      <a-button
        type="primary"
        style="margin-left: 8px"
        icon="download"
        @click="release2">release</a-button>
      <a-button
        type="primary"
        style="margin-left: 8px"
        icon="append"
        @click="addel">append</a-button>
    </div>
    <div>
      <iframe id="iframe-scene">
      </iframe>
    </div>

  </div>




</template>

<script>
  //    import Unity from 'vue-unity-webgl';
  import router from '../../router'

  //    import Vue from 'vue';
  export default {
    name: 'tester2',
    /* components: {
         Unity
     },*/
    data() {
      return {
        iframe: null,
      }
    },
    mounted(){
      this.iframe = document.getElementById("iframe-scene");

//            iframe.setAttribute("src", "UnityWebGL页面地址");
      this.iframe.setAttribute("src", "http://localhost:8000/static/index.html");
//            this.iframe.setAttribute("src", "https://www.baidu.com");
      this.iframe.setAttribute("style", "display:block;");
      this.iframe.setAttribute("frameborder", "0");
      this.iframe.style.height="500px";
      this.iframe.style.width="100%";
      this.iframe.style.border = 'none';
    },
    methods:{
      /*onready(){
          created
      },*/

      addel(){
        let parent = document.getElementById("parent");
        var x = document.createElement("DIV");//创建一个<DIV>节点
        var ifr = document.createElement('<iframe name="iframe-scene"></iframe>');
        x.appendChild(ifr);
        parent.append(x);
      },

      release2(){
        let iframe = document.getElementById("iframe-scene");
        iframe.src="about:blank";

        if(iframe){
          try {
            iframe.contentWindow.document.write('');
            iframe.contentWindow.document.clear();
            iframe.contentWindow.close();
            console.log('iframe released!')
          } catch (error) {
            console.log(error)
          }
        }

        iframe.parentElement.removeChild(iframe);
      }
    }
  }
  /*router.beforeEach((to, from, next) => {
      console.log('router leave');
      console.log(from);
      this.release2;
      setTimeout(() => {
          next();
      }, 300);
  })*/


  //        ,
  //    new Vue({
  //        components: { Unity }
  //    })
</script>