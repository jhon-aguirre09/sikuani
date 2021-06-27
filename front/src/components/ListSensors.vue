<template>
    <v-container class="mt-5">
        <Sensor v-for="i in 2" :key="i"></Sensor>
        
    </v-container>
  
</template>

<script>
import Sensor from './Features/Sensor';

export default {
    name:'ListSensors',
    components:{
    Sensor

    },
    data(){
        return{

        }
    }

}
</script>

<style>

</style>