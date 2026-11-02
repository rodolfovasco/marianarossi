# Site da Dra. Mariana Rossi

Site em [Astro](https://astro.build), publicado no GitHub Pages. Cada alteração enviada para a branch `main` é publicada sozinha em cerca de 1 a 2 minutos (aba **Actions** mostra o andamento).

- Endereço atual: https://rodolfovasco.github.io/marianarossi/
- Futuro: https://www.marianarossi.com.br (veja "Usar o domínio próprio")

---

## Como publicar um artigo novo (pelo navegador, sem instalar nada)

1. No GitHub, abra a pasta `src/content/artigos/`.
2. Clique em **Add file → Create new file**.
3. Dê um nome curto, sem acentos e com hífens, terminando em `.md`. Esse nome vira o endereço do artigo.
   Ex.: `dor-de-garganta.md` → `/artigos/dor-de-garganta/`
4. Cole o modelo abaixo, preencha e clique em **Commit changes**.

```markdown
---
title: "Título do artigo"
description: "Uma ou duas frases que resumem o artigo (aparecem no Google e no WhatsApp)."
topic: "Urgência ou consulta?"
date: 2026-11-15
summary:
  - "Ponto principal 1"
  - "Ponto principal 2"
alerts:
  - "Sinal de alerta 1"
  - "Sinal de alerta 2"
references:
  - label: "Nome da fonte, ano."
    url: "https://link-da-fonte"
draft: false
---

Primeiro parágrafo do texto.

## Um intertítulo

Mais texto. **Negrito** com dois asteriscos.

- Item de lista
- Outro item

1. Passo numerado
2. Outro passo
```

### Campos

| Campo | Obrigatório | O que é |
| --- | --- | --- |
| `title` | sim | Título do artigo, entre aspas |
| `description` | sim | Resumo curto (até ~160 caracteres) |
| `topic` | sim | Um destes, escrito igual: `Urgência ou consulta?`, `Exames e resultados`, `Medicamentos`, `Prevenção`, `Saúde da família` |
| `date` | sim | Data de publicação no formato `AAAA-MM-DD` |
| `updated` | não | Data da última revisão, se o texto for atualizado |
| `summary` | não | Itens da caixa "Resumo em 30 segundos" |
| `alerts` | não | Itens da caixa escura "Procure atendimento no mesmo dia se houver" |
| `references` | não | Fontes consultadas; `url` é opcional |
| `draft` | não | `true` deixa o artigo fora do ar e aparece só como "Em breve" na home |

O tempo de leitura é calculado automaticamente. O artigo mais recente vira o destaque da home.

**Dica:** para guardar uma ideia sem publicar, use `draft: true`. Os rascunhos já criados (hemograma, antibiótico, calor, check-up, pronto atendimento) estão na mesma pasta: é só escrever o texto e trocar para `draft: false`.

**Importante:** todo artigo deve ser revisado pela Dra. Mariana antes de ir ao ar.

---

## Outras edições comuns

- **Textos da home** (hero, sobre, formação, dúvidas): `src/pages/index.astro`
- **Nome, CRM, cidade e newsletter**: `src/lib/site.ts`
- **Cores e fontes**: `src/styles/global.css` (variáveis no topo)
- **Foto**: `src/assets/mariana.jpg` (rosto do autor: `src/assets/avatar.jpg`)

## Newsletter

O formulário já está pronto, mas precisa de um serviço para guardar os e-mails (por exemplo, Buttondown, Brevo ou Mailchimp). Crie a conta, copie o endereço de envio do formulário (form action) e cole em `newsletterAction` no arquivo `src/lib/site.ts`. Enquanto estiver vazio, o site avisa que as inscrições abrem em breve.

## Teste A/B do topo da home

A versão A aparece por padrão. Para ver as outras: `.../marianarossi/?v=b` e `.../marianarossi/?v=c`. Os textos ficam em `src/lib/site.ts`.

## Usar o domínio próprio

Depois de registrar `marianarossi.com.br`:

1. No GitHub: **Settings → Pages → Custom domain** → `www.marianarossi.com.br` → Save. Marque **Enforce HTTPS** quando liberar.
2. No Registro.br, no DNS do domínio, crie:
   - `www` do tipo **CNAME** apontando para `rodolfovasco.github.io`
   - Para o domínio sem www, quatro registros **A**: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
3. Em `.github/workflows/deploy.yml`, acrescente ao passo `withastro/action` as variáveis do domínio:

```yaml
      - uses: withastro/action@v4
        env:
          SITE_URL: https://www.marianarossi.com.br
          BASE_PATH: /
```

4. Crie o arquivo `public/CNAME` contendo só `www.marianarossi.com.br`.

## Rodar no computador (opcional)

```bash
npm install
npm run dev     # abre em http://localhost:4321/marianarossi/
```
