// Dados gerais do site. Edite aqui para mudar em todas as páginas.

export const site = {
  name: 'Dra. Mariana Rossi',
  fullName: 'Mariana Rossi Oliveira',
  role: 'Médica',
  crm: 'CRM-SP 163730',
  city: 'Ribeirão Preto',
  region: 'Ribeirão Preto e região',
  description:
    'Artigos escritos pela Dra. Mariana Rossi, médica em Ribeirão Preto, para entender sintomas, exames e cuidados com clareza e sem alarmismo.',

  // Endereço do formulário da newsletter (Buttondown, Brevo, Mailchimp...).
  // Enquanto estiver vazio, o formulário avisa que as inscrições abrem em breve.
  newsletterAction: '',
};

// Temas dos artigos. Para criar um tema novo, acrescente aqui
// e em src/content.config.ts.
export const topics = [
  'Urgência ou consulta?',
  'Exames e resultados',
  'Medicamentos',
  'Prevenção',
  'Saúde da família',
] as const;

// Versões do topo da home para teste A/B.
// A versão A aparece por padrão; ?v=b ou ?v=c no endereço mostra as outras.
export const heroVariants = {
  a: {
    title: 'Medicina explicada com clareza, para você decidir com mais segurança.',
    sub: 'Sou médica de pronto atendimento em Ribeirão Preto. Aqui transformo as dúvidas que ouço todos os dias em artigos simples e baseados em evidências, para você entender sintomas, exames e cuidados antes de se preocupar.',
    cta: 'Ler os artigos',
  },
  b: {
    title: 'As explicações do plantão, agora por escrito.',
    sub: 'Febre, resultados de exames, quando ir ao pronto atendimento: respostas diretas de uma médica que ouve essas perguntas toda semana.',
    cta: 'Começar pelos artigos',
  },
  c: {
    title: 'Entenda o que está acontecendo, sem jargão e sem alarmismo.',
    sub: 'Artigos escritos por uma médica para você saber o que observar em casa, o que perguntar na consulta e quando procurar atendimento.',
    cta: 'Ver o que já expliquei',
  },
};

/** Monta um link interno respeitando o caminho base do site. */
export function url(path = '/'): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return base + path;
}

export function readingMinutes(text: string): number {
  const words = text.trim().split(/\s+/).length;
  return Math.max(1, Math.round(words / 200));
}

export function formatDate(d: Date): string {
  return d.toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric', timeZone: 'UTC' });
}
