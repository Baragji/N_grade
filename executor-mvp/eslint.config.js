import js from "@eslint/js";
import globals from "globals";

export default [
  js.configs.recommended,
  {
    languageOptions: { ecmaVersion: 2022, sourceType: "module" },
    rules: {
      "no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
      "no-undef": "error",
      "no-console": "off"
    }
  }
  ,
  // Ignore generated output and build artifacts
  {
    ignores: [
      "output/**",
      "**/dist/**",
      "**/*.cjs"
    ]
  },
  {
    files: ["public/**/*.js"],
    languageOptions: { globals: globals.browser }
  }
];