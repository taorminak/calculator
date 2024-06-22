<template>
  <div class="form">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <label for="username">Username:</label>
      <input
        type="text"
        id="username"
        v-model="formData.username"
        autocomplete="username"
        required
      />
      <label for="password">Password:</label>
      <input
        type="password"
        id="password"
        v-model="formData.password"
        autocomplete="new-password"
        required
      />
      <label for="confirmPassword">Confirm password:</label>
      <input
        type="password"
        id="confirmPassword"
        v-model="formData.confirmPassword"
        autocomplete="new-password"
        required
      />
      <label for="role">Role:</label>
      <select id="role" v-model="formData.role" required>
        <option value="scientist">Scientist</option>
        <option value="student">Student</option>
      </select>
      <button class="main_button" type="submit">Register</button>
    </form>
    <p>
      Already registered?
      <button class="toggle_button" @click="toggleForm('Login')">Login</button>
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
    ...mapActions('user', ['login', 'logout', 'setForm']),
    async register() {
      if (this.password !== this.confirmPassword) {
        alert('Passwords do not match!')
        return
      }

      const userData = {
        username: this.formData.username,
        password: this.formData.password,
        role: this.formData.role
      }

      try {
        const response = await fetch('http://localhost:8000/users/create', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        })

        console.log(response)
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`)
        }

        const data = await response.json()
        console.log('User created:', data)

        this.login()
        this.$router.push('/profile')
      } catch (error) {
        console.error('Error creating user:', error)
      }
    },

    toggleForm(form) {
      this.setForm(form)
      this.$router.push(`/${form.toLowerCase()}`)
      this.username = ''
      this.password = ''
      this.confirmPassword = ''
      this.role = 'student'
    }
  }
}
</script>

<style></style>
