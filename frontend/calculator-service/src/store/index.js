import { createStore } from 'vuex'
import userModule from '@/store/user/index.js'

const store = createStore({
  modules: {
    user: userModule
  }
})

export default store
