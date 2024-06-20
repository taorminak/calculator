<template>
  <div class="registration">
    <RegistrationForm />
  </div>
</template>

<script setup>
import RegistrationForm from '../components/auth/registration/RegistrationForm.vue'
</script>

<style scoped>
.registration {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin-top: 30px;
}
</style>
