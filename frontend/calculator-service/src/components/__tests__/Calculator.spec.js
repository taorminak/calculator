import { mount } from '@vue/test-utils'
import { describe, it, expect, beforeEach, vi } from 'vitest'
import Calculator from '@/components/Calculator.vue'
import { nextTick } from 'vue'

global.fetch = vi.fn()

function createFetchResponse(data) {
  return {
    json: () => Promise.resolve(data),
    ok: true
  }
}

describe('Calculator', () => {
  let wrapper

  beforeEach(() => {
    wrapper = mount(Calculator)
    global.fetch.mockReset()
  })

  it('resets calculation and display values correctly on C key press', () => {
    wrapper.setData({
      firstOperand: '10',
      secondOperand: '5',
      operator: '+',
      displayValue: '15',
      resultDisplayed: true
    })

    wrapper.vm.handleServiceKey('C')

    expect(wrapper.vm.firstOperand).toBe('')
    expect(wrapper.vm.secondOperand).toBe('')
    expect(wrapper.vm.operator).toBe('')
    expect(wrapper.vm.displayValue).toBe('')
    expect(wrapper.vm.resultDisplayed).toBe(false)
  })

  it('assigns the value of pressed number keys to the first operand when the operator is empty', () => {
    wrapper.vm.operator = ''

    wrapper.vm.handleKeyClick({ key: '1', isService: false })
    wrapper.vm.handleKeyClick({ key: '8', isService: false })
    wrapper.vm.handleKeyClick({ key: '.', isService: false })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })

    expect(wrapper.vm.firstOperand).toBe('18.2')
  })

  it('assigns the negative value to the operand when the operator is empty', () => {
    wrapper.vm.operator = ''

    wrapper.vm.handleKeyClick({ key: '-', isService: true })
    wrapper.vm.handleKeyClick({ key: '7', isService: false })
    wrapper.vm.handleKeyClick({ key: '.', isService: false })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })

    expect(wrapper.vm.firstOperand).toBe('-7.2')
  })

  it('updates display value correctly when pressing numeric keys', () => {
    wrapper.vm.handleKeyClick({ key: '1', isService: false })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })
    wrapper.vm.handleKeyClick({ key: '.', isService: false })
    wrapper.vm.handleKeyClick({ key: '3', isService: false })

    expect(wrapper.vm.displayValue).toBe('12.3')
  })

  const operandValues = ['1', '8', '0', '2']
  it.each(operandValues)(
    'assigns the value of pressed number key to the second operand when the operator is present',
    (operand) => {
      wrapper.vm.operator = '+'

      wrapper.vm.handleKeyClick({ key: operand, isService: false })

      expect(wrapper.vm.secondOperand).toBe(operand)
    }
  )

  it('assigns the values to the operands and operator', () => {
    wrapper.vm.handleKeyClick({ key: '-', isService: true })
    wrapper.vm.handleKeyClick({ key: '3', isService: false })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })
    wrapper.vm.handleKeyClick({ key: '+', isService: true })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })

    expect(wrapper.vm.firstOperand).toBe('-32')
    expect(wrapper.vm.secondOperand).toBe('2')
    expect(wrapper.vm.operator).toBe('+')
  })

  it('calculates result correctly for valid operands and operator', async () => {
    wrapper.setData({
      firstOperand: '1.2',
      secondOperand: '5',
      operator: '+'
    })

    const response = { result: 6.2 }
    fetch.mockResolvedValue(createFetchResponse(response))

    await wrapper.vm.calculateResult()

    expect(wrapper.vm.displayValue).toBe('6.2')
    expect(wrapper.vm.resultDisplayed).toBe(true)
  })

  it('resets second operand to empty strings after calculation', async () => {
    wrapper.setData({
      firstOperand: '3',
      secondOperand: '5',
      operator: '+'
    })

    const response = { result: 8.0 }
    fetch.mockResolvedValue(createFetchResponse(response))

    await wrapper.vm.calculateResult()
    await nextTick()

    expect(wrapper.vm.secondOperand).toBe('')
  })

  it('resets first operand to the result of calculation', async () => {
    wrapper.vm.operator = '+'
    wrapper.vm.firstOperand = '1.5'
    wrapper.vm.secondOperand = '1.4'
    const response = { result: 2.9 }
    fetch.mockResolvedValue(createFetchResponse(response))

    await wrapper.vm.calculateResult()
    await nextTick()

    expect(wrapper.vm.firstOperand).toBe('2.9')
  })

  it('calculates the result and updates values after the second operator is applied', async () => {
    wrapper.vm.handleKeyClick({ key: '-', isService: true })
    wrapper.vm.handleKeyClick({ key: '3', isService: false })
    wrapper.vm.handleKeyClick({ key: '+', isService: true })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })
    wrapper.vm.handleKeyClick({ key: '-', isService: true })

    const response = { result: -1 }
    fetch.mockResolvedValue(createFetchResponse(response))

    await wrapper.vm.calculateResult()

    expect(wrapper.vm.firstOperand).toBe('-1')
    expect(wrapper.vm.secondOperand).toBe('')
    expect(wrapper.vm.displayValue).toBe('-1')
  })

  it('calculates the result and updates values after the third operator is applied', async () => {
    wrapper.vm.handleKeyClick({ key: '1', isService: false })
    wrapper.vm.handleKeyClick({ key: '+', isService: true })
    wrapper.vm.handleKeyClick({ key: '2', isService: false })
    wrapper.vm.handleKeyClick({ key: '-', isService: true })

    const response1 = { result: 3 }
    const response2 = { result: -2 }

    fetch.mockResolvedValue(createFetchResponse(response1))
    await wrapper.vm.calculateResult()
    await nextTick()

    wrapper.vm.handleKeyClick({ key: '5', isService: false })
    wrapper.vm.handleKeyClick({ key: '+', isService: true })

    fetch.mockResolvedValue(createFetchResponse(response2))
    await wrapper.vm.calculateResult()
    await nextTick()

    expect(wrapper.vm.firstOperand).toBe('-2')
    expect(wrapper.vm.secondOperand).toBe('')
    expect(wrapper.vm.operator).toBe('+')
    expect(wrapper.vm.displayValue).toBe('-2')
  })

  it('should handle unsupported operator', async () => {
    wrapper.setData({
      firstOperand: '1',
      secondOperand: '5',
      operator: '#'
    })

    await expect(() => wrapper.vm.calculateResult()).rejects.toThrowError('Unsupported operator')
  })
})
