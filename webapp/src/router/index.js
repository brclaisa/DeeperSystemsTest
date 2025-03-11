import { createRouter, createWebHistory } from 'vue-router'
import UserList from '../components/UserList.vue'
import AddUser from '../components/AddUser.vue'

const routes = [
  { path: '/', component: UserList },
  { path: '/add-user', component: AddUser },
  { path: '/edit-user/:id', name: 'edit-user', component: AddUser }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router