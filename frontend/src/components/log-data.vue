<template>
    <v-container bg fill-height grid-list-md text-xs-center>
        <v-layout row wrap align-center>
            <v-flex xs12 sm9 offset-sm2 align-center justify-center >
                <v-card class="elevation-12" style="border-radius:25px;" height="800px">
                    <v-container>
                    <h1>Hello {{name}}</h1>
                        <form>
                            <h2 style="margin-top:40px">Breakfast</h2>
                            <v-layout row style="margin-top:15px">
                                <v-flex md4>
                                    <v-text-field
                                        v-model="bCalories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preBreakfastBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md>
                                    <v-text-field
                                        v-model="postBreakfastBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:140px">Lunch</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="lCalories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preLunchBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="postLunchBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:140px">Dinner</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="dCalories"
                                        :mask="calorieMask"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preDinnerBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="postDinnerBloodSugar"
                                        :rules="bloodSugarRules"
                                        :mask="bloodSugarMask"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                             <v-layout row xs12>
                            <v-flex>
                                <v-btn flat block color="blue" @click.prevent="validateBeforeSubmit">
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
export default {
  name: 'Log Data',
  data: () => ({
    name: 'Meredith',
    calorieMask: '#####',
    valid: false,
    bloodSugarRules: [
      v => /^[0-9]{2,3}$/.test(v) || 'Must be a valid blood sugar level'
    ]
  })
//   mounted () {
//     axios
//       .post('INSERT_ENDPOINT_HERE')
//       .then(response => (this.data = response))
//   }
}
</script>
