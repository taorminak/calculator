const actions = {
  login({ commit }) {
    commit('SET_LOGIN')
  },
  logout({ commit }) {
    commit('SET_LOGOUT')
  }
}

export default actions
