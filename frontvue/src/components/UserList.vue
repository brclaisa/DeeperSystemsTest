<template>
    <v-container>
      <v-row>
        <v-col>
          <h1 class="text-2xl font-bold mb-4">User List</h1>
          <v-list>
            <v-list-item v-for="user in users" :key="user.user">
              <v-list-item-content>
                <v-list-item-title>{{ user.user }}</v-list-item-title>
                <v-list-item-subtitle>{{ user.user_timezone }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        users: []
      }
    },
    created() {
      this.fetchUsers()
    },
    methods: {
      async fetchUsers() {
        try {
          const response = await axios.get('http://localhost:5000/api/users')
          this.users = response.data.users
        } catch (error) {
          console.error('Error fetching users:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Adicione estilos específicos do componente aqui, se necessário */
  </style>