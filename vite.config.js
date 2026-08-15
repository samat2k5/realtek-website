import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    {
      name: 'dev-html-rewrite',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (req.url === '/about' || req.url === '/about/') req.url = '/about/index.html';
          if (req.url === '/products' || req.url === '/products/') req.url = '/products/index.html';
          if (req.url === '/projects' || req.url === '/projects/') req.url = '/projects/index.html';
          if (req.url === '/projects/changi-airport' || req.url === '/projects/changi-airport/') req.url = '/projects/changi-airport/index.html';
          if (req.url === '/safety-quality' || req.url === '/safety-quality/') req.url = '/safety-quality/index.html';
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
        products: resolve(__dirname, 'products/index.html'),
        projects: resolve(__dirname, 'projects/index.html'),
        changiAirport: resolve(__dirname, 'projects/changi-airport/index.html'),
        safetyQuality: resolve(__dirname, 'safety-quality/index.html'),
        privacy: resolve(__dirname, 'privacy/index.html'),
        terms: resolve(__dirname, 'terms/index.html'),
      },
    },
  },
});
