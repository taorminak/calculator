<template>
  <div class="calculator">
    <CalculatorDisplay :displayValue="displayValue" />
    <CalculatorKeyboard @key-clicked="handleKeyClick" />
  </div>
</template>

<script>
import { OPERATORS, ENDPOINTS } from '@/constants'
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
        this.resetDisplayValue()
        this.resultDisplayed = false
      }
      if (this.operator == '') {
        this.firstOperand += key
      } else {
        if (this.secondOperand == '') {
          this.resetDisplayValue()
        }
        this.secondOperand += key
      }
      this.displayValue += key
    },
    handleServiceKey(key) {
      switch (key) {
        case 'C':
          this.resetCalculationValues()
          this.resetDisplayValue()
          break
        case '=':
          this.calculateResult()
          break
        default:
          if (OPERATORS.includes(key)) {
            this.operator = key
            if (this.firstOperand && this.secondOperand) {
              this.calculateResult()
            }
          }
          break
      }
    },
    resetCalculationValues() {
      this.firstOperand = ''
      this.secondOperand = ''
      this.operator = ''
    },
    resetDisplayValue() {
      this.displayValue = ''
    },
    async calculateResult() {
      if (this.firstOperand === '' || this.secondOperand === '' || this.operator === '') return

      const endpoint = ENDPOINTS[this.operator]
      if (!endpoint) {
        console.error('Unsupported operator')
        return
      }

      const requestBody = {
        operand1: parseFloat(this.firstOperand),
        operand2: parseFloat(this.secondOperand)
      }

      try {
        const data = await this.fetchCalculationResult(endpoint, requestBody)
        this.displayValue = String(data.result)
        this.firstOperand = String(data.result)
        this.secondOperand = ''
        this.operator = ''
        this.resultDisplayed = true
      } catch (error) {
        console.error('Error calculating result:', error)
      }
    },
    async fetchCalculationResult(endpoint, requestBody) {
      try {
        const response = await fetch(`http://localhost:8000/calculator/${endpoint}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        })

        if (!response.ok) {
          throw new Error('Failed to fetch response')
        }

        const data = await response.json()
        return data
      } catch (error) {
        throw error
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
