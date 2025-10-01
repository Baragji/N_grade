import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    environment: "node",
    include: ["tests/**/*.test.ts"],
    exclude: ["output/**", "dist/**", "node_modules/**"],
    coverage: {
      reporter: ["text", "lcov"],
      provider: "v8",
      reportsDirectory: "coverage"
    }
  }
});
