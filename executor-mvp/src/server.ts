import "dotenv/config";
import { app } from "./app.js";

const PORT = Number(process.env.PORT || 3000);

app.listen(PORT, () => {
  console.log(`Executor MVP listening on http://localhost:${PORT}`);
  console.log(`UI: http://localhost:${PORT}/`);
});
