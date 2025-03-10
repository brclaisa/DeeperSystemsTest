<template>
    <v-container>
      <v-row>
        <v-col>
          <h1 class="text-2xl font-bold mb-4">Add User</h1>
          <v-form @submit.prevent="addUser">
            <v-text-field v-model="user.username" label="Username" required></v-text-field>
            <v-text-field v-model="user.password" label="Password" type="password" required></v-text-field>
            <v-text-field v-model="user.user_timezone" label="Timezone" required></v-text-field>
            <v-checkbox v-model="user.is_user_admin" label="Admin"></v-checkbox>
            <v-checkbox v-model="user.is_user_manager" label="Manager"></v-checkbox>
            <v-checkbox v-model="user.is_user_tester" label="Tester"></v-checkbox>
            <v-btn type="submit" color="primary">Add User</v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        user: {
          username: '',
          password: '',
          user_timezone: '',
          is_user_admin: false,
          is_user_manager: false,
          is_user_tester: false
        }
      }
    },
    methods: {
      async addUser() {
        try {
          await axios.post('http://localhost:5000/api/users', this.user)
          alert('User added successfully')
          this.user = {
            username: '',
            password: '',
            user_timezone: '',
            is_user_admin: false,
            is_user_manager: false,
            is_user_tester: false
          }
        } catch (error) {
          console.error('Error adding user:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Adicione estilos específicos do componente aqui, se necessário */
  </style>