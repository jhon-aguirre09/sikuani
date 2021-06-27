<template>
    <v-col>
        
        <div id="circle" class="circle mt-3 d-flex justify-center align-center " :class='{"blue":this.status == true,"red":this.status==false}'>
            <img src="../assets/death-star.svg" class="justify-center"   width="70%" height="70%" alt="death star">
        </div>
  </v-col>
</template>

<script>
export default {
    name:'StatusCircle',
    props:{
        state:Boolean
        },
    data(){
        return{
            'status':null,
        }
    },
    watch:{
        "state":function(data){
            this.status = data
        }
    }

}
</script>

<style>
    #circle{
        border-radius: 50%;
        width:300px;
        height:300px ;
        transition: background-color 1.5s;
    }
    .blue{
        background-color: blue;
    }
    .red{
        background-color: red;
    }
</style>