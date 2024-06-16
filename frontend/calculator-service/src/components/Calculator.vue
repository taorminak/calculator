<template>
  <div class="calculator">
    <CalculatorDisplay :displayValue="displayValue" />
    <CalculatorKeyboard @key-clicked="handleKeyClick" />
  </div>
</template>

<script>
import CalculatorDisplay from './CalculatorDisplay.vue'
import CalculatorKeyboard from './CalculatorKeyboard.vue'

export default {
  name: 'Calculator',
  components: {
    CalculatorDisplay,
    CalculatorKeyboard
  },
  data() {
    return {
      displayValue: ''
    }
  },
  methods: {
    handleKeyClick({ key, isService }) {
      console.log(key)
      if (isService) {
        this.handleServiceKey(key)
      } else {
        this.updateDisplay(key)
      }
      console.log('Key clicked:', key)
    },
    updateDisplay(key) {
      console.log(this.displayValue)
      if (this.displayValue === '0' && key !== '.') {
        this.displayValue = key
      } else {
        this.displayValue += key
      }
    },
    clearDisplay() {
      this.displayValue = '0'
    },
    calculateResult() {
      console.log('Was calculated')
    },
    handleServiceKey(key) {
      if (key === 'C') {
        this.clearDisplay()
      }
      console.log(key)
    }
  }
}
</script>

<style scoped>
.calculator {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 10px;
}
</style>
