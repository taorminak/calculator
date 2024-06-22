<template>
  <div class="form">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="formData.username" autocomplete="username" required />
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="formData.password" autocomplete="new-password" required />
      <button class="registration_button" type="submit">Login</button>
    </form>
    <p>
      Not registered yet?
      <button class="toggle_button" @click="toggleForm('Register')">Sign Up</button>
    </p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data() {
    return {
      formData: {
        username: '',
        password: ''
      }
    }
  },
  computed: {
    ...mapGetters('user', ['isLoggedIn', 'currentForm'])
  },
  methods: {
    ...mapActions('user', ['login', 'logout', 'setForm']),
    async loginUser() {
      const userData = {
        username: this.formData.username,
        password: this.formData.password
      }

      try {
        const response = await fetch('http://localhost:8000/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        })

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`)
        }

        const data = await response.json()
        console.log('User authenthificated:', data)

        //this.$router.push('/')
        if (data.access_token) {
          this.login()
          this.setForm('Profile')
          this.$router.push('/profile')
        } else {
          throw new Error('Authentication failed')
        }
      } catch (error) {
        console.error('Error authentificating user:', error)
      }
    },
    toggleForm(form) {
      this.setForm(form)
      this.$router.push(`/${form.toLowerCase()}`)
      this.formData.username = ''
      this.formData.password = ''
    }
  }
}
</script>
