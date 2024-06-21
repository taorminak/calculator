const mutations = {
  SET_LOGIN(state) {
    state.isLoggedIn = true
  },
  SET_LOGOUT(state) {
    state.isLoggedIn = false
  }
}

export default mutations
