import { describe, it, expect, beforeAll, afterAll } from "vitest";
import request from "supertest";
import { app } from "../src/app.js";
import http from "node:http";

let server: http.Server;
const PORT = 0; // ephemeral

beforeAll(async () => {
  await new Promise<void>((resolve) => {
    server = app.listen(PORT, () => resolve());
  });
});

afterAll(async () => {
  await new Promise<void>((resolve, reject) => {
    server.close((err) => (err ? reject(err) : resolve()));
  });
});

describe("server smoke", () => {
  it("GET /healthz returns ok", async () => {
    const res = await request(server).get("/healthz");
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ status: "ok" });
  });

  it("POST /api/execute requires prompt", async () => {
    const res = await request(server).post("/api/execute").send({ prompt: "" });
    expect(res.status).toBe(400);
    expect(res.body).toEqual({ error: "prompt required" });
  });
});
