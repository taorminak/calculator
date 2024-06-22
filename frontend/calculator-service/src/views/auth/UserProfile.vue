<template>
  <div>You successfully logged in.</div>
  <button @click="handleLogout" class="logout-button">Log Out</button>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data() {
    return {
      formData: {
        username: '',
        password: '',
        confirmPassword: '',
        role: 'student'
      }
    }
  },
  computed: {
    ...mapGetters('user', ['isLoggedIn', 'currentForm'])
  },
  methods: {
    ...mapActions('user', ['logout', 'setForm']),
    handleLogout() {
      this.logout()
      this.setForm('Login')
      this.$router.push('/login')
    }
  }
}
</script>

<style lang=""></style>
