<template>
  <v-form v-model="valid">
    <v-container bg fill-height grid-list-md text-xs-center>
      <v-layout row wrap align-center>
        <v-flex xs12 sm8 offset-sm2 align-center justify-center>
            <v-card class="elevation-12" style="border-radius:25px;">
                <v-toolbar color="blue">
                    <v-toolbar-title class="white--text">Sign In</v-toolbar-title>
                </v-toolbar>
                <v-container>
                    <form>
                        <v-layout row>
                            <v-flex xs12>
                                <v-text-field
                                    v-model="email"
                                    :rules="emailRules"
                                    label="E-mail"
                                    color="blue"
                                    required
                                ></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout row>
                            <v-flex xs12>
                                <v-text-field
                                    v-model="password"
                                    :rules="passRules"
                                    :type="show1 ? 'text' : 'password'"
                                    name="input-10-1"
                                    label="Password"
                                    color="blue"
                                    @click:append="show1 = !show1"
                                ></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout row xs12>
                            <v-flex>
                                <v-btn flat block color="blue" @click.prevent="validateBeforeSubmit">
                                Sign In
                                </v-btn>
                            </v-flex>
                        </v-layout>
                    </form>
                </v-container>
            </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>
<script>
// import {generateKeys} from '../encryption.js'
// console.log(generateKeys())
export default {
  name: 'Login',
  data: () => ({
    valid: false,
    password: '',
    passRules: [
      v => !!v || 'Password is required',
      v => v.length >= 8 || 'Password must be more than 8 characters'
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+/.test(v) || 'E-mail must be valid'
    ]
  })
}
</script>
