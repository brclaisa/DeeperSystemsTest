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
          <th class="py-2">Created At</th>
          <th class="py-2">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td class="border px-4 py-2">{{ user.user }}</td>
          <td class="border px-4 py-2">
            <span v-if="user.is_user_admin" class="mr-2">admin</span>
            <span v-if="user.is_user_manager" class="mr-2">manager</span>
            <span v-if="user.is_user_tester" class="mr-2">tester</span>
          </td>
          <td class="border px-4 py-2">{{ user.user_timezone }}</td>
          <td class="border px-4 py-2">{{ user.is_user_active }}</td>
          <td class="border px-4 py-2">{{ user.created_at }}</td>
          <td class="border px-4 py-2">
            <router-link :to="{ name: 'edit-user', params: { id: user.id } }" class="bg-blue-500 text-white px-4 py-2 mr-2">Edit</router-link>
            <button class="bg-red-500 text-white px-4 py-2" @click="confirmDeleteUser(user)">Delete</button>
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
    confirmDeleteUser(user) {
      if (confirm(`Are you sure you want to delete user ${user.user}?`)) {
        this.deleteUser(user)
      }
    },
    async deleteUser(user) {
      try {
        await axios.delete(`http://localhost:5000/api/users/${user.id}`)
        this.users = this.users.filter(u => u.id !== user.id)
        alert('User deleted successfully')
      } catch (error) {
        console.error('Error deleting user:', error)
        alert('Failed to delete user')
      }
    }
  }
}
</script>