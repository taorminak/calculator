<template>
  <div class="profile_container">
    <div>You successfully logged in.</div>
  <button @click="handleLogout" class="main_button">Log Out</button>
  <button @click="showHistory" class="main_button">See the history of calculations</button>
  <div id="no-history-message">{{ noHistoryMessage }}</div>
  <table v-if="calculations.length > 0">
      <thead>
        <tr>
          <th>Operand 1</th>
          <th>Operand 2</th>
          <th>Result</th>
          <th>Operation</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(calculation, index) in calculations" :key="index">
          <td>{{ calculation[0] }}</td>
          <td>{{ calculation[1] }}</td>
          <td>{{ calculation[2] }}</td>
          <td>{{ calculation[3] }}</td>
        </tr>
      </tbody>
    </table>
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
      },
      noHistoryMessage: "",
      calculations: []
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
    },
    async showHistory() {
      try {
        const response = await fetch('http://localhost:8000/calculator/history', {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
          }
        });
        
        if (!response.ok) {
          throw new Error('Failed to fetch calculation history');
        }

        const data = await response.json();
        console.log('Calculation history:', data);
        this.calculations = data;
        
        
      } catch (error) {
        console.error('Error fetching calculation history:', error.message);
        this.noHistoryMessage = 'Failed to see history of calculations. Check if you have authorization to perform this action.';
      }
    },
  }
}
</script>

<style scoped>
.profile_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
table {
  width: 100%;
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid black;
  padding: 8px;
  color: rgb(80, 181, 249);
  background-color: rgb(16, 16, 16);
}

td {
  text-align: center; 
}

th {
  background-color: rgb(16, 16, 16);
}
</style>
