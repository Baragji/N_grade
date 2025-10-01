import Ajv2020 from "ajv/dist/2020";
import addFormats from "ajv-formats";
import schema from "../../contracts/executor-output.schema.json" with { type: "json" };
import type { ExecutorOutput } from "./types.js";

const ajv = new Ajv2020({ allErrors: true, strict: true });
(addFormats as unknown as (ajv: any) => void)(ajv);
const validate = ajv.compile(schema as any);

export function validateExecutorOutput(data: unknown): { ok: true; value: ExecutorOutput } | { ok: false; errors: string } {
  const ok = validate(data);
  if (ok) return { ok: true, value: data as ExecutorOutput };
  const msg = (validate.errors || []).map((e: any) => `${e.instancePath} ${e.message}`).join("; ");
  return { ok: false, errors: msg || "Invalid schema" };
}
