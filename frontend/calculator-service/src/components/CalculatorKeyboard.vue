<template>
  <div class="calculator_keyboard">
    <div v-for="(row, index) in rows" :key="index" class="calculator_row">
      <div
        v-for="key in row"
        :key="key"
        :class="['calculator_key', isServiceKey(key) ? 'service_key' : 'number_key']"
        @click="handleKeyClick(key)"
      >
        {{ key }}
      </div>
    </div>
  </div>
</template>
<script>
const ROWS = ['C789/', '456*', '123-', '0.+=']
export default {
  name: 'CalculatorKeyboard',
  data() {
    return {
      rows: ROWS
    }
  },
  methods: {
    handleKeyClick(key) {
const keys = this.$el.querySelectorAll('.calculator_key')
     console.log(keys)

      const isService = this.isServiceKey(key)
    
      this.$emit('key-clicked', { key, isService })
    },
    isServiceKey(key) {
      return ['+', '-', '*', '=', 'C', '/'].includes(key)
    }
  }
}
</script>
<style>
.calculator_keyboard {
  display: flex;
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
