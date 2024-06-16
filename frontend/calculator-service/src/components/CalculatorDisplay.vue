<template>
  <div class="calculator_display">
    {{ displayValue }}
  </div>
</template>

<script>
export default {
  name: 'CalculatorDisplay',
  props: ['displayValue']
}
</script>

<style scoped>
.calculator_display {
  font-size: 2em;
  text-align: right;
  background-color: white;
  border: 1px solid #ccc;
  margin: 10px;
  width: 100%;
  min-height: 50px;
}
</style>
