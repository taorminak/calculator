/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  root: true,
  env: {
    browser: true,
    es2021: true,
    jest: true 
  },
  extends: [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-prettier/skip-formatting'
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  rules: {
    "semi": ["error", "always"],
    "max-len": [
      "warn",
      { "code": 120, "ignorePattern": "^import\\s.+\\sfrom\\s.+;$" }
    ],
    "no-multiple-empty-lines": ["error", { "max": 1, "maxEOF": 1 }],
    "quotes": [
      "error",
      "single",
      { "allowTemplateLiterals": true, "avoidEscape": true }
    ],
    "import/extensions": "off",
    "import/prefer-default-export": "off",
    "max-lines-per-function": ["warn", 40]
  },
}
