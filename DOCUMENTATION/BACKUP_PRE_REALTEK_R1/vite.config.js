import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    {
      name: 'dev-html-rewrite',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url === '/about' || req.url === '/about/') req.url = '/about/index.html';
          if (req.url === '/ezy-saas' || req.url === '/ezy-saas/') req.url = '/ezy-saas/index.html';
          if (req.url === '/ezyhr' || req.url === '/ezyhr/') req.url = '/ezyhr/index.html';
          if (req.url === '/privacy' || req.url === '/privacy/') req.url = '/privacy/index.html';
          if (req.url === '/terms' || req.url === '/terms/') req.url = '/terms/index.html';
          next();
        });
      },
    },
  ],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about/index.html'),
        ezySaas: resolve(__dirname, 'ezy-saas/index.html'),
        ezyHr: resolve(__dirname, 'ezyhr/index.html'),
        privacy: resolve(__dirname, 'privacy/index.html'),
        terms: resolve(__dirname, 'terms/index.html'),
      },
    },
  },
});
