<template>
  <div>
    <nav class="bg-gray-800 p-4">
      <router-link to="/" class="text-white mr-4">User List</router-link>
      <router-link to="/add-user" class="text-white">Add User</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>