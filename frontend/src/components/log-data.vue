<template>
    <v-container bg fill-height grid-list-md text-xs-center>
        <v-layout row wrap align-center>
            <v-flex xs12 sm9 offset-sm2 align-center justify-center >
                <v-card class="elevation-12" style="border-radius:25px;" height="800px">
                    <v-container>
                    <h1>Hello Meredith</h1>
                        <form>
                            <v-layout row style="margin-top:15px">
                                <v-flex md4>
                                    <datepicker v-on:selected="getDate" :value='new Date()'></datepicker>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:40px">Breakfast</h2>
                            <v-layout row style="margin-top:15px">
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[0].Calories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[0].BloodSugar.pre"
                                        :rules="bloodSugarRules"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md>
                                    <v-text-field
                                        v-model="resp[0].BloodSugar.post"
                                        :rules="bloodSugarRules"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:140px">Lunch</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[1].Calories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[1].BloodSugar.pre"
                                        :rules="bloodSugarRules"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[1].BloodSugar.post"
                                        :rules="bloodSugarRules"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:140px">Dinner</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[2].Calories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[2].BloodSugar.pre"
                                        :rules="bloodSugarRules"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="resp[2].BloodSugar.post"
                                        :rules="bloodSugarRules"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                             <v-layout row xs12>
                            <v-flex>
                                <v-btn flat block color="blue" @click="postPost()">
                                Submit
                                </v-btn>
                            </v-flex>
                        </v-layout>
                        </form>
                    </v-container>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import axios from 'axios'
import Datepicker from 'vuejs-datepicker'
import {encrypt} from '../encryption.js'
export default {
  name: 'LogData',
  data: () => ({
    resp: [{
        Mealtype: 'Breakfast',
        Calories: '',
        BloodSugar: {
            pre: '',
            post: ''
        }, 
        Date: new Date().toString(),
        name: 'Meredith'
    },{
        Mealtype: 'Lunch',
        Calories: '',
        BloodSugar: {
            pre: '',
            post: ''
        }, 
        Date: new Date().toString(),
        name: 'Meredith'
    },{
        Mealtype: 'Dinner',
        Calories: '',
        BloodSugar: {
            pre: '',
            post: ''
        }, 
        Date: new Date().toString(),
        name: 'Meredith'
    }],
    calorieMask: '#####',
    valid: false,
    key: '',
    eval: '',
    key_resp: '',
    bloodSugarRules: [
      v => /^[0-9]{2,3}$/.test(v) || 'Must be a valid blood sugar level'
    ]
  }),
  methods: {
    postPost() {
        this.resp[0].BloodSugar.pre = encrypt(this.key, this.eval, this.resp[0].BloodSugar.pre)
        this.resp[0].BloodSugar.post = encrypt(this.key, this.eval, this.resp[0].BloodSugar.post)
        this.resp[0].calories = encrypt(this.key, this.eval, this.resp[0].Calories)
        axios.put(`http://127.0.0.1:5000/new_data`, {
        body: this.resp
        })
        .then(response => {})
        .catch(e => {
        this.errors.push(e)
        })
    }, 
    getDate(date){
        this.resp[0].date = date.toString()
        this.resp[1].date = date.toString()
        this.resp[2].date = date.toString()
    },
    async GetKey() {
        var self = this
        await axios.get(`http://127.0.0.1:5000/get_key`)
        .then(function (response) {
        self.key_resp = response.data
        return self.key_resp
        })
        .catch(e => {
            console.log('err')
            this.errors.push(e)
        })
        this.key_resp = this.key_resp.split(' ')
        this.key = parseInt(this.key_resp[0])
        this.eval = parseInt(this.key_resp[1])
        console.log(this.key)
        console.log(this.eval)
    }    
  },
  components: {
    Datepicker
  },beforeMount(){
    this.GetKey()
  }      
}
</script>
<style>
.example {
  background: #7e7b7b;
  border: 1px solid #ddd;
  padding: 0em 1em 1em;
  margin-bottom: 2em;
}
</style>
