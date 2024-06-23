import { mount } from '@vue/test-utils';
import { describe, it, expect, beforeEach } from 'vitest';
import CalculatorKeyboard from '@/components/CalculatorKeyboard.vue';
import { SERVICE_BUTTONS } from '../../constants.js';

describe('CalculatorKeyboard.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(CalculatorKeyboard);
  });

  it('renders the correct number of rows and keys', () => {
    const rows = wrapper.findAll('.calculator_row');
    const keys = wrapper.findAll('.calculator_key');

    expect(rows.length).toBe(4);
    expect(keys.length).toBe(20);
  });

  it('assigns the correct classes to service keys', () => {
    SERVICE_BUTTONS.forEach((key) => {
      const keyWrappers = wrapper
        .findAll('.calculator_key')
        .filter((wrapKey) => wrapKey.text() === key);

      keyWrappers.forEach((keyWrapper) => {
        expect(keyWrapper.classes()).toContain('service_key');
        expect(keyWrapper.classes()).not.toContain('number_key');
      });
    });
  });

  it('assigns the correct classes to number keys', () => {
    const numberKeys = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.'];

    numberKeys.forEach((key) => {
      const keyWrappers = wrapper
        .findAll('.calculator_key')
        .filter((wrapKey) => wrapKey.text() === key);

      keyWrappers.forEach((keyWrapper) => {
        expect(keyWrapper.classes()).toContain('number_key');
        expect(keyWrapper.classes()).not.toContain('service_key');
      });
    });
  });

  it('emits "key-clicked" event with right parameteres when C key is clicked', async () => {
    const keys = wrapper.findAll('.calculator_key');

    await keys.at(0).trigger('click');

    expect(wrapper.emitted('key-clicked')).toBeTruthy();
    expect(wrapper.emitted('key-clicked')[0]).toEqual([{ key: 'C', isService: true }]);
  });

  it('emits "key-clicked" event with right parameters when key 7 is clicked', async () => {
    const keys = wrapper.findAll('.calculator_key');

    await keys.at(1).trigger('click');

    expect(wrapper.emitted('key-clicked')).toBeTruthy();
    expect(wrapper.emitted('key-clicked')[0]).toEqual([{ key: '7', isService: false }]);
  });
});
