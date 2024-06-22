const actions = {
  login({ commit }) {
    commit('SET_LOGIN')
  },
  logout({ commit }) {
    commit('SET_LOGOUT')
  },
  setForm({ commit }, form) {
    commit('SET_FORM', form)
  }
}

export default actions
