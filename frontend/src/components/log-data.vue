<template>
    <v-container bg fill-height grid-list-md text-xs-center>
        <v-layout row wrap align-center>
            <v-flex xs12 sm9 offset-sm2 align-center justify-center >
                <v-card class="elevation-12" style="border-radius:25px;" height="800px">
                    <v-container>
                    <h1>Hello INSERT NAME HERE</h1>
                        <form>
                            <h2 style="margin-top:40px">Breakfast</h2>
                            <v-layout row style="margin-top:15px">
                                <v-flex md4>
                                    <v-text-field
                                        v-model="bCalories"
                                        :rules="calorieRules"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preBreakfastBloodSugar"
                                        :rules="bloodSugar"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md>
                                    <v-text-field
                                        v-model="postBreakfastBloodSugar"
                                        :rules="bloodSugar"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:100px">Lunch</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="lCalories"
                                        :rules="calorieRules"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preLunchBloodSugar"
                                        :rules="bloodSugar"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="postLunchBloodSugar"
                                        :rules="bloodSugar"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                            </v-layout>
                            <h2 style="margin-top:100px">Dinner</h2>
                            <v-layout row>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="dCalories"
                                        :rules="calorieRules"
                                        label="Calories"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="preDinnerBloodSugar"
                                        :rules="bloodSugar"
                                        label="Pre-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
                                </v-flex>
                                <v-flex md4>
                                    <v-text-field
                                        v-model="postDinnerBloodSugar"
                                        :rules="bloodSugar"
                                        label="Post-Meal Blood Sugar"
                                        color="blue"
                                    ></v-text-field>
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
    name: 'Login',
    data: () => ({
      valid: false,
      password: '',
      passRules: [
        v => !!v || 'Password is required',
        v => v.length >= 8 || 'Password must be more than 8 characters'
      ]
    })
  }
</script>