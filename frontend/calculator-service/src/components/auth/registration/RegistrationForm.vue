<template>
  <div class="form">
    <component :is="currentForm">
      <template v-if="currentForm === 'registration'">
        <h2>Sign Up</h2>
        <form @submit.prevent="register">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
          <label for="confirmPassword">Confirm password:</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
          <label for="role">Role:</label>
          <select id="role" v-model="role" required>
            <option value="scientist">Scientist</option>
            <option value="student">Student</option>
          </select>
          <button class="registration_button" type="submit">Register</button>
        </form>
        <p>
          Already registered?
          <button class="toggle_button" @click="toggleForm('login')">Login</button>
        </p>
      </template>

      <template v-else-if="currentForm === 'login'">
        <h2>Login</h2>
        <form @submit.prevent="login">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
          <button class="registration_button" type="submit">Login</button>
        </form>
        <p>
          Not registered yet?
          <button class="toggle_button" @click="toggleForm('registration')">Sign Up</button>
        </p>
      </template>
    </component>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentForm: 'registration',
      username: '',
      password: '',
      role: 'student'
    }
  },
  methods: {
    register() {
      const userData = {
        username: this.username,
        password: this.password,
        role: this.role
      }
    },
    login() {
      const userData = {
        username: this.username,
        password: this.password
      }
    },
    toggleForm(form) {
      this.currentForm = form
    }
  }
}
</script>

<style scoped>
.form {
  background-color: rgb(16, 16, 16);
  display: flex;
  flex-direction: column;
  padding: 25px;
  border-radius: 2%;
  background-color: rgb(16, 16, 16);
  color: rgba(178, 218, 255, 1);
  font-size: 1.2em;
}

form {
  display: flex;
  flex-direction: column;
}

h2 {
  margin-bottom: 10px;
}

label {
  margin-bottom: 5px;
}
input,
select {
  margin-bottom: 10px;
  height: 1.5rem;
}

.toggle_button {
  border: none;
  background: transparent;
  color: rgba(41, 168, 255, 1);
  cursor: pointer;
  font-size: 1em;
  transition: all 0.2s ease-in-out;
}

.toggle_button:hover {
  color: rgb(31, 137, 208);
}

.registration_button {
  margin: auto;
  margin-bottom: 10px;
  margin-top: 10px;
  height: 2rem;
  width: 50%;
  cursor: pointer;
  background-color: rgb(130, 202, 250);
  border-radius: 5px;
  transition: all 0.3s ease-in-out;
}

.registration_button:hover {
  background-color: rgb(81, 82, 91);
  color: rgb(80, 181, 249);
}

.registration_button:active {
  background-color: rgb(98, 99, 110);
  color: rgb(130, 202, 250);
}
</style>
