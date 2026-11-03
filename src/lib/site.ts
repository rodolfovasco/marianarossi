// Dados gerais do site. Edite aqui para mudar em todas as páginas.

export const site = {
  name: 'Dra. Mariana Rossi',
  nickname: 'Tia Mari',
  fullName: 'Mariana Rossi Oliveira',
  role: 'Pediatra',
  crm: 'CRM-SP 163730',
  rqe: 'RQE 118511',
  city: 'Ribeirão Preto',
  region: 'Ribeirão Preto e região',
  description:
    'Dicas da Tia Mari: a pediatra Dra. Mariana Rossi explica o que observar em casa, o que fazer e quando procurar atendimento, sem susto e com base em evidência.',

  // Endereço do formulário de inscrição do Brevo (lista "Dicas da Tia Mari").
  // Campos esperados pelo Brevo: NOME, EMAIL e TEMA.
  // Se ficar vazio, o formulário avisa que as inscrições abrem em breve.
  newsletterAction: 'https://a7fd5610.sibforms.com/serve/MUIFALKfVgYJV4jjns8qJxKrrRZIJPZTlCIoeeS7AsbKX5fKD224S8d6bJPVtQJoPH3R-G2FJkGYNC2TxVJwc8_uVKXDDdtlDx7DDMxuh4zxqpag28QQtxLwAeP8VyJJfnDiCw_wwBY5NWfPpY9Y4jA3D08hMbjQSrCRzabikVvZo0hQ7ic825Zf45qlG4RDOXE1Ay3MEGA28LJblg==',

  // Google Tag Manager
  gtmId: 'GTM-K88KVQ2N',
};

// Temas dos artigos e a cor de cada um. Para criar um tema novo,
// acrescente aqui e em src/content.config.ts.
export const topics = [
  'Urgência ou consulta?',
  'Exames e resultados',
  'Medicamentos',
  'Prevenção',
  'Saúde da família',
] as const;

export const topicColor: Record<string, string> = {
  'Urgência ou consulta?': 't-morango',
  'Exames e resultados': 't-ceu',
  'Medicamentos': 't-uva',
  'Prevenção': 't-menta',
  'Saúde da família': 't-sol',
};

// Versões do topo da home para teste A/B.
// A versão A aparece por padrão; ?v=b ou ?v=c no endereço mostra as outras.
export const heroVariants = {
  a: {
    title: 'Pediatria sem susto.',
    sub: 'Oi, eu sou a Tia Mari, pediatra de plantão em Ribeirão Preto. Aqui eu explico o que observar em casa, o que fazer e quando correr pro atendimento, do jeitinho que explico no plantão.',
    cta: 'Ver as dicas',
  },
  b: {
    title: 'O que eu explico no plantão, agora pra você ler com calma.',
    sub: 'Febre, tosse, vômito, manchinhas: respostas diretas de uma pediatra que ouve essas perguntas toda semana.',
    cta: 'Começar pelas dicas',
  },
  c: {
    title: 'Febre, tosse, manchinha? Respira: a Tia Mari explica.',
    sub: 'Dicas escritas por uma pediatra para você saber o que observar, o que perguntar e quando procurar atendimento.',
    cta: 'Quero as dicas',
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
