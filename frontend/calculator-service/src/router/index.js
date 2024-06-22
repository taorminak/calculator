import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '../store'

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
      component: () => import('@/views/auth/UserProfile.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const allowedRoutes = ['login', 'register', 'profile']
  const formName = allowedRoutes.includes(to.name) ? capitalizeFirstLetter(to.name) : 'Login'
  store.dispatch('user/setForm', formName)

  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('token')
    if (!token) {
      next('/login')
    } else {
      next()
    }
  } else {
    next()
  }
})

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}

export default router
