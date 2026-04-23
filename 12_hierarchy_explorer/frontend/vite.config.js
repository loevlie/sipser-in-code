import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/regex": "http://localhost:8000",
      "/cfg": "http://localhost:8000",
      "/tm": "http://localhost:8000",
      "/health": "http://localhost:8000",
    },
  },
});
