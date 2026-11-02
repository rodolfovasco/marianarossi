// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Enquanto o site estiver no endereço do GitHub Pages:
//   SITE_URL = https://rodolfovasco.github.io   BASE_PATH = /marianarossi
// Quando o domínio próprio estiver ativo, mude para:
//   SITE_URL = https://www.marianarossi.com.br  BASE_PATH = /
// (veja o README, seção "Usar o domínio próprio")
const SITE_URL = process.env.SITE_URL ?? 'https://rodolfovasco.github.io';
const BASE_PATH = process.env.BASE_PATH ?? '/marianarossi';

export default defineConfig({
  site: SITE_URL,
  base: BASE_PATH,
  trailingSlash: 'always',
  integrations: [sitemap()],
});
