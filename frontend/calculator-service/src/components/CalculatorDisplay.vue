<template>
  <div class="calculator_display">
    {{ displayValue }}
  </div>
</template>

<script>
export default {
  name: 'CalculatorDisplay',
  props: {
    displayValue: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.calculator_display {
  font-size: 2em;
  text-align: right;
  background-color: rgb(16, 16, 16);
  color: rgb(216, 221, 245);
  border: none;
  margin: 20px;
  width: 100%;
  min-height: 100px;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: right;
}
</style>
