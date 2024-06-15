<template>
    <div class="calculator">
      <div v-for="(row, index) in rows" :key="index" class="calculator_row">
        
        <div v-for="key in row" :key="key" class="calculator_key" @click="handleKeyClick(key)">
          {{ key }}
        </div>
  
      </div>
    </div>
  </template>
  
  <script>
  const ROWS = ['789/', '456*', '123-', '0.+=']
  
  export default {
    name: 'Calculator',
    data() {
      return {
        rows: ROWS
      }
    },
    methods: {
      handleKeyClick(key) {
        console.log('Key clicked:', key)
      },
    }
  }
  </script>
  
  <style scoped>
  .calculator {
    display: flex;
    padding: 10px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
  }
  
  .calculator_row {
    display: flex;
    justify-content: center;
    margin: 10px 0;
  }
  
  .calculator_key {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    background-color: white;
    color: black;
    font-family: system-ui, sans-serif;
    font-size: 16px;
    margin: 0 5px;
    cursor: pointer;
    border-radius: 10%;
    transition: all 0.3s ease-in-out;
  }
  
  .calculator_key:hover {
    background-color: #aba9a9;
    color: white;
  }
  
  .calculator_key:active {
    border-radius: 30%;
    background-color: #8e8d8d;
    color: white;
  }
  </style>