<template >
    <div id='view-data'>
        <div id='content'>
            <canvas ref='chart'></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'
export default {
  name: 'view-data',
    data () {
    return {
     resp:''
    }   
  },
  mounted() {
    var chart = this.$refs.chart
    var ctx = chart.getContext("2d")
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Calories, Pre Meal, Post Meal'],
            datasets: [{
                label: 'Blood Glucose',
                data: [this.resp.caloric_intake, this.resp.pre_meal_smbg, this.resp.post_meal_smbg],
                borderColor: [
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
},      methods: {
            Getget() {
                var self = this
                axios.get(`http://127.0.0.1:5000/get_data/`+ new Date().toString()+ '/Breakfast')
                .then((response) => {
                self.resp = response.data
                })
                .catch(e => {
                    this.errors.push(e)
                })
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