import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const artigos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/artigos' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    topic: z.enum(['Urgência ou consulta?', 'Exames e resultados', 'Medicamentos', 'Prevenção', 'Saúde da família']),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    summary: z.array(z.string()).default([]),
    alerts: z.array(z.string()).default([]),
    alertsTitle: z.string().default('Procure atendimento no mesmo dia se houver'),
    references: z.array(z.object({ label: z.string(), url: z.string().optional() })).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { artigos };
