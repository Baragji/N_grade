Here’s the single, decisive path forward—and I’ve already packaged the MVP so you can run it now.

# What you get (today)

* A tiny **Executor Agent** you run locally.
* Simple web UI: type a build prompt → click → it calls an LLM → validates a strict JSON contract → **writes files** into `./output/<project>`, browsable in the UI.
* Node.js + TypeScript server with **Ajv** schema validation and **path sandboxing** (no `../` etc.).
* Pluggable LLM provider (OpenAI or Anthropic) via `.env`.
* Minimal roadmap doc to keep us pointed in one direction.

# Download

[Download the MVP as a zip](sandbox:/mnt/data/executor-mvp.zip)

# Run it

1. Unzip, then in the project root:

```
cp .env.example .env
# Set LLM_PROVIDER=openai (or anthropic), set your API key, optionally model
pnpm i   # or: npm i
pnpm dev # or: npm run dev
```

2. Open [http://localhost:3000](http://localhost:3000)
3. Use this prompt to get your first win:

```
Make a minimal Node+TypeScript Hello World HTTP server exposing GET / returning "Hello World". Include README.md with run steps. Output must follow the provided JSON schema.
```

It will write files to `./output/<project>` and give you a link to open the generated project.

# Why this path (and not 10 others)?

* You wanted: **docs for clarity**, **one agent**, **hello world**, **see output in repo**. This delivers exactly that.
* No glue nightmare, no orchestration detour. We’ll add features incrementally after this win.
* **Strict JSON contract** means reliability (no stray prose) and aligns with your SSOT “no mocks, strict contracts” rule.

# What’s inside (high level)

* `src/server.ts` — Express server, `/api/execute` endpoint, serves UI and `/output`.
* `src/executor/systemPrompt.md` — the Executor system prompt (JSON-only, minimal runnable output).
* `contracts/executor-output.schema.json` — JSON schema gate (Ajv).
* `src/llm/providers/{openai,anthropic}.ts` — provider switches via env.
* `public/{index.html,script.js,styles.css}` — dead simple UI.
* `ROADMAP.md` — Phase 0→3 next steps.
* `docker/` — Dockerfile + compose for local container run.

# Next 3 steps (after your first Hello World)

1. **Checksums in `_executor_meta.json`** per file (guard against partial writes).
2. **Retry/repair pass** if the model ever returns non-JSON (still enforced by schema).
3. **Tiny CI**: supertest for `/api/execute` + schema, artifact upload of meta.

If you want me to extend this into a Next.js UI with history/diffs, or add a guarded “run npm install & test inside generated project” tool, I’ll ship that next.
