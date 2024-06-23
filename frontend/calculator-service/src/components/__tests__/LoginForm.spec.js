import { mount } from '@vue/test-utils';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import LoginForm from '@/components/auth/login/LoginForm.vue';

globalThis.fetch = vi.fn();

function createFetchResponse(data) {
  return {
    json: () => new Promise((resolve) => resolve(data)),
    ok: true,
  };
};

describe('Login Form', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = mount(LoginForm);
    globalThis.fetch.mockReset();
  });

  it('throws an error when authorization failes', async () => {
    fetch.mockRejectedValueOnce(new Error('Unauthorized'));

    await expect(() => wrapper.vm.loginUser()).rejects.toThrowError();
  });

  it('throws an error when response has no access token', async () => {
    const data = {
            ok: false,
            status: 401    
    };
    fetch.mockResolvedValueOnce(createFetchResponse(data));

    await expect(wrapper.vm.loginUser()).rejects.toThrowError();
  });

});
