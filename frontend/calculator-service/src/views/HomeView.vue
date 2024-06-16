<script setup>
import Calculator from '../components/Calculator.vue'
</script>

<template>
  <main class="main">
    <h1>Calculator</h1>
    <Calculator />
  </main>
</template>

<style scoped>
.main {
  display: flex;
  padding: 10px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
