<template>
  <div>
    <div >
      hahah
    </div>

    <button @click="sent()">
      hahah
    </button>

    <p>
      {{ this.socketdata}}
    </p>

  </div>
</template>

<script>

  export default {
    name: 'tester4',


    data() {
      return {
        socketdata:'',
      }
    },
    mounted(){
      this.sockets.subscribe('response', (data) => {
//                console.log('server sent refresh data from mounted');
                this.socketdata=this.socketdata+'\n'+JSON.stringify(data);
//                console.log(data);
            });
    },

    methods: {
      sent(){
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
