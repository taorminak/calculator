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
      displayValue: '',
      firstOperand: '',
      secondOperand: '',
      operator: '',
      resultDisplayed: false
    }
  },
  methods: {
    handleKeyClick({ key, isService }) {
      if (isService === true) {
        this.handleServiceKey(key)
      } else {
        this.updateDisplay(key)
      }
    },
    updateDisplay(key) {
      if (this.resultDisplayed) {
        this.displayValue = ''
        this.resultDisplayed = false
      }
      if (this.operator == '') {
        this.firstOperand += key
      } else {
        if (this.secondOperand == '') {
          this.displayValue = ''
        }
        this.secondOperand += key
      }
      this.displayValue += key
    },
    clearDisplay() {
      this.displayValue = ''
      this.firstOperand = ''
      this.secondOperand = ''
      this.operator = ''
    },
    async calculateResult() {
      if (this.firstOperand === '' || this.secondOperand === '' || this.operator === '') return
      let endpoint
      if (this.operator === '+') {
        endpoint = 'add'
      } else if (this.operator === '-') {
        endpoint = 'subtract'
      } else {
        console.error('Unsupported operator')
        return
      }

      const requestBody = {
        operand1: parseFloat(this.firstOperand),
        operand2: parseFloat(this.secondOperand)
      }

      try {
        const response = await fetch(`http://localhost:8000/calculator/${endpoint}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        })

        const data = await response.json()
        this.displayValue = data.result
        this.firstOperand = data.result
        this.secondOperand = ''
        this.operator = ''
        this.resultDisplayed = true
      } catch (error) {
        console.error('Error:', error)
      }
    },
    handleServiceKey(key) {
      if (key === 'C') {
        this.clearDisplay()
      } else if (['+', '-', '*', '/'].includes(key)) {
        this.operator = key
        if (this.firstOperand !== '' && this.secondOperand !== '') {
          this.calculateResult()
        }
      } else if (key === '=') {
        this.calculateResult()
      }
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
