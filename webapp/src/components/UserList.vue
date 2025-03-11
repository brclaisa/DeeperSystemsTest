<template>
    <div class="container mx-auto">
      <h1 class="text-2xl font-bold mb-4">User List</h1>
      <table class="min-w-full bg-white">
        <thead>
          <tr>
            <th class="py-2">Username</th>
            <th class="py-2">Roles</th>
            <th class="py-2">Timezone</th>
            <th class="py-2">Is Active?</th>
            <th class="py-2">Last Updated At</th>
            <th class="py-2">Created At</th>
            <th class="py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.user">
            <td class="border px-4 py-2">{{ user.user }}</td>
            <td class="border px-4 py-2">
              <span v-for="role in user.roles" :key="role">{{ role }}</span>
            </td>
            <td class="border px-4 py-2">{{ user.user_timezone }}</td>
            <td class="border px-4 py-2">{{ user.is_user_active }}</td>
            <td class="border px-4 py-2">{{ user.updated_at }}</td>
            <td class="border px-4 py-2">{{ user.created_at }}</td>
            <td class="border px-4 py-2">
              <button class="bg-blue-500 text-white px-4 py-2 mr-2" @click="editUser(user)">Edit</button>
              <button class="bg-red-500 text-white px-4 py-2" @click="deleteUser(user)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
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
      },
      editUser(user) {
        console.log('Edit user:', user)
      },
      deleteUser(user) {
        console.log('Delete user:', user)
      }
    }
  }
  </script>
  
  <style scoped>
  
  </style>