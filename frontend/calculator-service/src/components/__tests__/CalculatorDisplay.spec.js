import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import CalculatorDisplay from '@/components/CalculatorDisplay.vue'

describe('CalculatorDisplay', () => {
    const displayValues = [
        '12345', 
        "6.789",
        "-27645765870.36",
        "0.00",
    ];
  it.each(displayValues)('renders display value correctly', (value) => {
    const wrapper = mount(CalculatorDisplay, {
      props: { displayValue: value }
    })

    expect(wrapper.text()).toContain(value)
  })
})