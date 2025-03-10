<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>My Vue App</v-toolbar-title>
      <v-spacer></v-spacer>
      <router-link to="/" class="v-btn v-btn--text">User List</router-link>
      <router-link to="/add-user" class="v-btn v-btn--text">Add User</router-link>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* Adicione estilos globais aqui, se necessário */
</style>