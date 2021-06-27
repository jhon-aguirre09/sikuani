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
          :type="this.alert[0]" >{{text_action}}</v-alert>
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
          <h1>Tiemstamp</h1>
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
    sensones:Array,
    tiemstamp:String
},
data(){
    return{
        num_action:undefined,
        text_time:'',
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
       "tiemstamp":function(data){
           this.text_time=data
       },
       "sensonres":function(data){
           this.data_sensonres = data;
       }  
    },

computed:{
        AlertType:function(value){
            return String(this.alert2[value].type)
        }
    }
}
</script>

<style>

</style>