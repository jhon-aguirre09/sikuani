<template>
  <v-app>
    <v-app-bar app color="dark" dark>
        <v-col  >
          <v-row justify="center">
          <h3 class="h3">La defensa de la Estrella V1.0</h3>
            </v-row>
        </v-col>
      <!-- <v-toolbar-title>La Defensa de la Estrella V1.0</v-toolbar-title> -->
    </v-app-bar>

    <v-main>
      <v-row>   
          <StatusCircle></StatusCircle>
        
          <Notify class="mt-2"></Notify>
          <ListSensors></ListSensors>
        
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from "./components/HelloWorld";
import  StatusCircle from "./components/StatusCircle";
import  Notify from "./components/Notify";
import ListSensors from "./components/ListSensors";



export default {
  name: "App",

  components: {
    StatusCircle,
    Notify,
    ListSensors,
    
  },
  created () {
    this.$vuetify.theme.dark = true
  },
  data: () => ({
    data:{
      "repair":{
        status:null,
        values:[],
        timestamps:''
      },
      "attack":{
        status:null,
        values:[],
        timestamps:''
      },
      "bomb":{

      }
    }
  }),
  watch:{

  }
};
</script>
