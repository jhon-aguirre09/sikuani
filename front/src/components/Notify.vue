<template>
<div>
    
  <v-col >
      <v-row>
          <h1>Action</h1>
      </v-row>
      <v-row>
          <v-alert 
          dense
          outlined 
          :type="AlertType" >{{MessageType}}</v-alert>
      </v-row>
  </v-col>
  <v-col >
      <v-row>
          <h1>Sensores</h1>
      </v-row>
      <v-row>
          <div type="info">
              <p v-for="(sensor,i) in data_sensores" :key="i">{{sensor}}</p>
          </div>
      </v-row>
  </v-col>
  <v-col >
      <v-row>
          <h1>Timestamp</h1>
      </v-row>
      <v-row>
          <v-alert 
          dense
          outlined 
          type="info">
                {{text_time}}
          </v-alert>
      </v-row>
  </v-col>
  </div>
</template>

<script>
export default {
name:'Notify',
props:{
    action:Number,
    sensores:Array,
    timestamp:String
},
data(){
    return{
        num_action:3,
        text_time:''    ,
        data_sensores:[],
        alert:['warning','info','error'],
        alert2:[
            {type:'warning',value:`Alerta envio de tropas a sensore ` }, /*Posicion 0 - Nave enemiga detecta */
            {type:'info',value:`Averia en los sensores enviand equipo de mantenimiento`}, /*Posicion 1 - Reparacion de Nave*/
            {type:'error',value:`Bomba detectada, Disparando cañón plasmodium ribosómico a sennsor `}, /*Posicion 2 - Reparacion de Nave*/
            {type:'success',value:`Todo en marcha y en funcionamiento`} /*Posicion 3 - Reparacion de Nave*/
            ]

        
    }
},
watch:{
       "action":function(data){
           this.num_action= data
       },
       "timestamp":function(data){
           this.text_time=data
       },
       "sensores":function(data){
           this.data_sensores = data;
       }  
    },

computed:{
        AlertType:function(){
            let action = this.num_action;
            return String(this.alert2[action].type)
        },
        MessageType:function(){
            let action = this.num_action;
            return String(this.alert2[action].value)
        }
    }
}
</script>

<style>

</style>