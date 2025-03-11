<template>
  <div class="container mx-auto">
    <h1 class="text-2xl font-bold mb-4">{{ isEditMode ? 'Edit User' : 'Add User' }}</h1>
    <form @submit.prevent="submitForm" class="space-y-4">
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
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">
        {{ isEditMode ? 'Update User' : 'Add User' }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default {
  setup() {
    const user = ref({
      username: '',
      password: '',
      user_timezone: '',
      is_user_admin: false,
      is_user_manager: false,
      is_user_tester: false
    })
    const isEditMode = ref(false)
    const route = useRoute()
    const router = useRouter()

    onMounted(async () => {
      const userId = route.params.id
      if (userId) {
        isEditMode.value = true
        try {
          const response = await axios.get(`http://localhost:5000/api/users/${userId}`)
          Object.assign(user.value, response.data)
        } catch (error) {
          console.error('Error fetching user:', error)
        }
      }
    })

    const submitForm = async () => {
      try {
        if (isEditMode.value) {
          await axios.put(`http://localhost:5000/api/users/${route.params.id}`, user.value)
          alert('User updated successfully')
        } else {
          await axios.post('http://localhost:5000/api/users', user.value)
          alert('User added successfully')
        }
        router.push('/')
      } catch (error) {
        console.error('Error submitting form:', error)
      }
    }

    return {
      user,
      isEditMode,
      submitForm
    }
  }
}
</script>