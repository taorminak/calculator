import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/auth/login/LoginForm.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/components/auth/registration/RegistrationForm.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('@/views/auth/UserProfile.vue')
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})

export default router
