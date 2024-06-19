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
          this.operator = ''
          break
        case '-':
          if (this.firstOperand === '') {
            this.firstOperand = '-'
            this.displayValue = '-'
          } else {
            this.assignOperator(key)
          }
          break
        default:
          this.assignOperator(key)
          break
      }
    },
    assignOperator(key) {
      if (this.firstOperand) {
        if (OPERATORS.includes(key)) {
          if (this.firstOperand && this.secondOperand) {
            this.calculateResult()
          }
          this.operator = key
        }
      }
    },
    resetCalculationValues() {
      this.firstOperand = ''
      this.secondOperand = ''
      this.operator = ''
      this.resultDisplayed = false
    },
    resetDisplayValue() {
      this.displayValue = ''
    },
    async calculateResult() {
      if (this.firstOperand === '' || this.secondOperand === '' || this.operator === '') return

      const endpoint = ENDPOINTS[this.operator]
      if (!endpoint) {
        throw new Error('Unsupported operator')
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

        this.resultDisplayed = true
      } catch (e) {
        console.error(e)
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

        if (!response || !response.ok) {
          throw new Error('Failed to fetch calculation result')
        }

        const data = await response.json()
        return data
      } catch (e) {
        throw e
      }
    }
  }
}
</script>

<style scoped>
.calculator {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 25px;
  border-radius: 5%;
  background-color: rgb(16, 16, 16);
}
</style>
