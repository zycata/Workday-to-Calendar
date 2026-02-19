import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  server: {
    port: 5100,
    strictPort: true, // This prevents Vite from jumping to 5101 if 5100 is busy
  },
  plugins: [react()],
})
