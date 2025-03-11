<template>
    <div class="container mx-auto">
      <h1 class="text-2xl font-bold mb-4">Add User</h1>
      <form @submit.prevent="addUser" class="space-y-4">
        <div>
          <label class="block text-gray-700">Username</label>
          <input v-model="user.username" class="border rounded w-full py-2 px-3" type="text" required>
        </div>
        <div>
          <label class="block text-gray-700">Password</label>
          <input v-model="user.password" class="border rounded w-full py-2 px-3" type="password" required>
        </div>
        <div>
          <label class="block text-gray-700">Timezone</label>
          <input v-model="user.user_timezone" class="border rounded w-full py-2 px-3" type="text" required>
        </div>
        <div>
          <label class="block text-gray-700">Admin</label>
          <input v-model="user.is_user_admin" class="mr-2 leading-tight" type="checkbox">
        </div>
        <div>
          <label class="block text-gray-700">Manager</label>
          <input v-model="user.is_user_manager" class="mr-2 leading-tight" type="checkbox">
        </div>
        <div>
          <label class="block text-gray-700">Tester</label>
          <input v-model="user.is_user_tester" class="mr-2 leading-tight" type="checkbox">
        </div>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">Add User</button>
      </form>
    </div>
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
  </style>