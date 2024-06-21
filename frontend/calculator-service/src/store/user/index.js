import actions from '@/store/user/actions'
import mutations from '@/store/user/mutations'
import getters from '@/store/user/getters'

const userModule = {
  namespaced: true,
  state() {
    return {
      isLoggedIn: false
    }
  },
  getters,
  actions,
  mutations
}

export default userModule
