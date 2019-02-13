<template >
    <div id='view-data'>
        <v-container bg fill-height grid-list-md text-xs-center>
            <v-layout row wrap align-center>
                <v-flex xs12 sm9 offset-sm2 align-center justify-center >
                    <v-card class="elevation-12" style="border-radius:25px;" height="800px">
                        <h2 style="margin-top:40px">Breakfast Details</h2>
                            <v-layout row style="margin-top:15px">
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp.caloric_intake "
                                        label="Calories"
                                        color="blue"
                                        disabled
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp.pre_meal_smbg"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                        disabled
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md>
                                    <v-text-field
                                        v-model="resp.post_meal_smbg"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                        disabled
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'
import {generateKeys, decrypt} from '../encryption.js'
export default {
  name: 'view-data',
    data () {
    return {
     resp:'',
     PublicKey: '',
     PrivateKey: '',
     E: ''
    }   
  }, methods: {
            async Getget() {
                let temp = generateKeys()
                this.E = temp[0]
                this.PublicKey = temp[1][0]
                this.PrivateKey = temp[1][1]
                let self = this
                let LunchTemp = ''
                let DinnerTemp = ''
                await axios.get(`http://127.0.0.1:5000/get_data/`+ new Date().toString()+ '/Breakfast/'+this.PublicKey+'/'+this.E)
                .then(function (response) {
                    self.resp = response.data
                    return self.resp
                })
                .catch(e => {
                    this.errors.push(e)
                })
                this.resp.caloric_intake = parseInt(decrypt(this.PrivateKey, this.E,this.resp.caloric_intake))
                this.resp.pre_meal_smbg = parseInt(decrypt(this.PrivateKey, this.E, this.resp.pre_meal_smbg))
                this.resp.post_meal_smbg = parseInt(decrypt(this.PrivateKey, this.E, this.resp.post_meal_smbg))
                
            }
        },
        beforeMount(){
            this.Getget()
        }          
}
</script>

<style>
    #view-data {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
    #content {
        margin: auto;
        width: 1024px;
        background-color: #FFFFFF;
        padding: 20px;
    }
</style>