<template>
     <v-expansion-panels>
        <v-expansion-panel>
        <v-expansion-panel-header>{{number_sensor}}</v-expansion-panel-header>
        <v-expansion-panel-content>
                <Line></Line>
            </v-expansion-panel-content>
        </v-expansion-panel>
     </v-expansion-panels>
   
  
</template>

<script>
import Line from './Line';

export default {
    name:'Sensor',
    components:{
        Line
    },
    data(){
        return{
            number_sensor:''
        }
    },

}
</script>

<style>

</style>