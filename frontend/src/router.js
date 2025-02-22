import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'
import  HOmepage from './views/Home.vue'
import Services from './views/Services.vue'
import Contact from './views/Contact.vue'
import Login from './pages/Login.vue'
const routes = [
  {
    path: '/',
    name: 'House',
    component: () => import('@/pages/Home.vue'),
  },
//   {
// path:'/login',
// name:'Login',
// component:Login
//   },
  { path: '/', component: HOmepage },
  { path: '/services', component: Services },
  { path: '/contact', component: Contact },
  {
    path: '/account/login',
    component: () => import('@/pages/Login.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
