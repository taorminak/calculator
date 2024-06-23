<template>
  <div class="calculator_keyboard">
    <div v-for="(row, index) in rows" :key="index" class="calculator_row">
      <div
        v-for="key in row"
        :key="key"
        :class="[
          'calculator_key',
          `calculator-${key}`,
          isServiceKey(key) ? 'service_key' : 'number_key'
        ]"
        @click="handleKeyClick(key)"
      >
        {{ key }}
      </div>
    </div>
  </div>
</template>

<script>
import { ROWS, SERVICE_BUTTONS } from '../constants'

export default {
  name: 'CalculatorKeyboard',
  data() {
    return {
      rows: ROWS
    }
  },
  methods: {
    handleKeyClick(key) {
      const isService = this.isServiceKey(key)

      this.$emit('key-clicked', { key, isService })
    },
    isServiceKey(key) {
      return SERVICE_BUTTONS.includes(key)
    }
  }
}
</script>

<style scoped>
.calculator_keyboard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
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
  width: 60px;
  height: 60px;
  background-color: rgba(48, 49, 54, 1);
  color: rgba(41, 168, 255, 1);
  font-family: system-ui, sans-serif;
  font-size: 16px;
  margin: 0 5px;
  cursor: pointer;
  border-radius: 10%;
  transition: all 0.3s ease-in-out;
}

.calculator_key:hover {
  background-color: rgb(81, 82, 91);
  color: rgb(80, 181, 249);
}

.calculator_key:active {
  border-radius: 20%;
  background-color: rgb(98, 99, 110);
  color: rgb(130, 202, 250);
}

.service_key {
  background-color: rgba(0, 93, 178, 1);
  color: rgba(178, 218, 255, 1);
}

.calculator-C {
  background-color: rgb(178, 0, 33);
  color: rgb(243, 200, 208);
}
</style>
