const mutations = {
  SET_LOGIN(state) {
    state.isLoggedIn = true;
  },
  SET_LOGOUT(state) {
    state.isLoggedIn = false;
  },
  SET_FORM(state, form) {
    state.currentForm = form;
  }
};

export default mutations;
