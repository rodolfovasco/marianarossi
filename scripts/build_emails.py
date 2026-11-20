"""Gera os e-mails HTML das Dicas da Tia Mari (automação Brevo).

Uso: python3 scripts/build_emails.py  -> grava emails/NN-slug.html
Cada e-mail segue o mesmo molde (cabeçalho, faixa colorida com Bento, resumo,
caixa roxa, botão para o artigo, alerta, assinatura, rodapé).
"""
from pathlib import Path

SITE = "https://www.marianarossi.com.br"
UTM = "utm_source=brevo&utm_medium=email&utm_campaign=boas-vindas"

COLORS = {
    "morango": dict(c="#D63A63", d="#A82748", l="#FFE3EA", btn="#D63A63", btnd="#A82748"),
    "menta": dict(c="#0B8577", d="#08665B", l="#DDF7F3", btn="#0B8577", btnd="#08665B"),
    "sol": dict(c="#8A5A00", d="#8A5A00", l="#FFF4D1", btn="#7C5CE0", btnd="#5B3FC0", border="#FFC845"),
}

EMAILS = [
    dict(
        file="04-queda-de-bebe.html", slug="queda-de-bebe-quando-e-perigoso", utm="queda", color="morango",
        topic="Urgência ou consulta?",
        subject="A Sapeca da Queda aprontou? O que observar depois do tombo",
        title="A Sapeca da Queda: quando o tombo é perigoso",
        tagline="Ela adora um segundinho de distração. Bora deixar a casa à prova de tombo?",
        preheader="A altura da queda e o comportamento depois dizem muito. E um checklist para a casa.",
        intro=[
            "Conheça a <strong>Sapeca da Queda</strong>. Ela espera um segundinho de distração para fazer o bebê rolar do trocador, escorregar do sofá ou escapar do colo. O coração dispara, e a pergunta é sempre a mesma: <strong>\"será que foi grave?\"</strong>",
            "A boa notícia é que a maioria das quedas é de pouca altura e não deixa consequência. Mas alguns sinais pedem atendimento, e dá para deixar a casa bem mais difícil para essa sapeca.",
        ],
        summary=[
            "Antes dos 2 anos, queda de mais de 90 cm (como do colo de um adulto em pé) merece avaliação médica, mesmo que o bebê pareça bem.",
            "As primeiras 24 a 48 horas são as mais importantes: fique por perto e observe o comportamento.",
            "Ele pode dormir. Não precisa acordar de hora em hora, mas ao acordar deve agir como sempre.",
            "Nunca deixe o bebê sozinho em lugar alto, nem por um segundinho. Bebê-conforto vai no chão.",
        ],
        box=("Importante", "Nunca sacuda o bebê, nem para \"ver se ele está bem\". Se bater o nervoso, deixe-o num lugar seguro e peça ajuda."),
        cta_lead="No artigo completo tem a tabela de alturas que preocupam e o checklist anti-Sapeca, com quedas e outros acidentes da casa.",
        alert="Procure atendimento imediatamente se houver perda de consciência (mesmo rápida), três ou mais vômitos, sonolência excessiva, convulsão, sangue ou líquido saindo do nariz ou do ouvido, choro inconsolável ou moleira estufada. Em emergência, ligue 192.",
        closing="Na dúvida, procure o pediatra. O seu \"tem alguma coisa estranha\" merece ser ouvido.",
    ),
    dict(
        file="05-tosse.html", slug="tosse-que-nao-passa", utm="tosse", color="morango",
        topic="Urgência ou consulta?",
        subject="A tosse do seu filho já vai fazer mesversário? 🤧",
        title="A Malvada da Tosse: por que ela demora tanto",
        tagline="Ela chega de mansinho, vai ficando... e quando você vê, já está comemorando mesversário!",
        preheader="Tosse depois de resfriado pode durar semanas. Veja o que ajuda e quando se preocupar.",
        intro=[
            "Toda família conhece a <strong>Malvada da Tosse</strong>. O nariz melhora, a febre vai embora... e ela fica. Uma semana, duas, três. Quando você percebe, a tosse já está quase fazendo <strong>mesversário</strong>.",
            "Na maioria das vezes, isso é normal. A tosse é a faxineira do pulmão: ela limpa o catarro. O segredo é deixar a criança confortável e saber quando ela merece consulta.",
        ],
        summary=[
            "Depois de um resfriado, a tosse costuma durar até 10 dias, mas pode passar de 3 semanas.",
            "Quem vai à creche ou à escola pode ter de 8 a 12 resfriados por ano. Parece uma tosse só, mas são várias.",
            "Lavagem nasal com soro e bastante líquido ajudam. Mel, só depois de 1 ano.",
            "Tosse que passa de 4 semanas, ou em bebê com menos de 6 meses, merece consulta.",
        ],
        box=("Importante", "Xarope para tosse não é indicado para crianças pequenas, e mel é proibido antes de 1 ano por risco de botulismo."),
        cta_lead="No artigo completo, explico o que ajuda em casa, o que evitar e todos os sinais que pedem atendimento.",
        alert="Procure atendimento no mesmo dia se houver respiração rápida ou cansada, lábios arroxeados, chiado no peito, tosse que começou depois de um engasgo, crises de tosse com guincho ou vômito, ou criança muito molinha. Em emergência, ligue 192.",
        closing="Tosse incomoda, mas quase sempre vai embora sozinha. Se ficar em dúvida, o pediatra é o melhor caminho.",
    ),
    dict(
        file="06-dentes.html", slug="primeiros-dentes-e-higiene", utm="dentes", color="menta",
        topic="Prevenção",
        subject="Nasceu o primeiro dentinho? A Fadinha do Dente tem um recado 🦷",
        title="A Fadinha do Dente: primeiros dentinhos",
        tagline="Nasceu o primeiro dentinho? A Fadinha já está de escovinha na mão!",
        preheader="Quando escovar, quanta pasta usar e quando ir ao odontopediatra.",
        intro=[
            "Um belo dia aparece uma pontinha branca na gengiva, e pronto: a <strong>Fadinha do Dente</strong> chegou à sua casa. Junto com ela vêm a baba, as mãozinhas na boca e um monte de dúvidas.",
            "Separei o essencial para você cuidar desse sorriso desde o primeiro dente.",
        ],
        summary=[
            "O primeiro dente costuma aparecer por volta dos 6 meses, mas cada bebê tem seu tempo.",
            "Do primeiro dente em diante: escovar 2 vezes por dia, com escova macia e pasta com flúor.",
            "Pasta: um grão de arroz cru enquanto não sabe cuspir; depois, um grão de ervilha.",
            "Primeira consulta no odontopediatra: quando nascer o primeiro dente ou antes do primeiro aniversário.",
        ],
        box=("Importante", "Nascer dente não costuma dar febre alta, diarreia forte ou prostração. Se aparecerem, procure o pediatra. E nada de colar de âmbar."),
        cta_lead="No artigo completo tem o passo a passo da escovação, como aliviar o incômodo da gengiva e os inimigos do sorriso.",
        alert="Procure o pediatra ou o odontopediatra se notar manchas brancas, amareladas ou escuras nos dentes, gengiva com pus ou sangramento frequente, nenhum dente até 1 ano ou trauma com dente amolecido ou quebrado.",
        closing="Escovar junto pode virar um momento gostoso do dia. Cante, conte até dez, faça careta no espelho.",
    ),
    dict(
        file="07-telas.html", slug="tempo-de-tela-criancas", utm="telas", color="sol",
        topic="Saúde da família",
        subject="A Lilypad está roubando a cena na sua casa? 📱🐸",
        title="A Lilypad da Telinha: quanto tempo de tela é demais",
        tagline="A Lilypad quer roubar a cena, mas o brinquedo favorito do seu filho ainda é você!",
        preheader="O tempo de tela recomendado para cada idade e como trazer as brincadeiras de volta.",
        intro=[
            "Em <strong>Toy Story 5</strong>, a vilã não é um brinquedo malvado: é a <strong>Lilypad</strong>, um tablet em formato de sapinho que chega à casa da Bonnie e rouba a atenção que antes era dos brinquedos.",
            "Em muitas casas, a Lilypad da vida real já roubou a cena: na mesa do jantar, no carro e na hora de dormir. Dá para virar esse jogo.",
        ],
        summary=[
            "Menores de 2 anos: nada de telas (videochamada rápida com a família, com um adulto junto, é a exceção).",
            "De 2 a 5 anos: no máximo 1 hora por dia, com supervisão.",
            "De 6 a 10 anos: de 1 a 2 horas por dia, também com supervisão.",
            "Em qualquer idade: sem telas nas refeições e desligadas de 1 a 2 horas antes de dormir.",
        ],
        box=("Dica da Tia Mari", "Deixe brinquedos simples à vista e reserve 15 minutinhos por dia de brincadeira junto, sem celular por perto."),
        cta_lead="No artigo completo tem as regras da casa contra a Lilypad e ideias para trazer os brinquedos de volta para a cena.",
        alert="Converse com o pediatra se notar atraso na fala, crises intensas toda vez que a tela é desligada, sono ruim que não melhora ou perda de interesse por brincar e estar com outras crianças.",
        closing="Não é preciso declarar guerra à tecnologia. O objetivo é que a Lilypad seja só mais um brinquedo na caixa.",
    ),
    dict(
        file="08-sol.html", slug="protecao-solar-criancas", utm="sol", color="sol",
        topic="Prevenção",
        subject="O Raio Sapeca está solto lá fora! ☀️ Boné e protetor a postos",
        title="O Senhor Ardidinho: proteção solar no verão",
        tagline="O Raio Sapeca está solto lá fora! Precisamos de boné e protetor para vencer essa batalha.",
        preheader="Bebês, protetor, horários e o que fazer se a pele queimar.",
        intro=[
            "O verão chegou e, com ele, o <strong>Senhor Ardidinho</strong>. Ele vem montado no Raio Sapeca, o raio ultravioleta, e deixa a pele vermelha, quente e dolorida.",
            "Os estragos do sol se acumulam ao longo da vida, e boa parte dessa conta é feita na infância. Mas dá para vencer essa batalha com o equipamento certo.",
        ],
        summary=[
            "Menores de 6 meses: nada de sol direto e nada de protetor. A proteção é sombra, roupa e chapéu.",
            "A partir dos 6 meses: protetor infantil FPS 30 ou mais, de 15 a 30 minutos antes de sair.",
            "Reaplique a cada 2 horas e sempre depois de entrar na água ou suar muito.",
            "Evite o sol entre 10h e 16h. Se a sombra da criança está menor que ela, é hora de abrigo.",
        ],
        box=("Kit anti-Ardidinho", "Protetor, boné ou chapéu de aba larga, roupa com proteção UV, óculos de sol com proteção ultravioleta, guarda-sol e muita água."),
        cta_lead="No artigo completo, explico como proteger os bebês, a regra da sombra e o que fazer se o Ardidinho ganhar uma rodada.",
        alert="Procure atendimento se, depois do sol, houver queimadura em bebê menor de 1 ano, bolhas grandes ou espalhadas, febre, vômitos, criança muito sonolenta ou sinais de desidratação.",
        closing="Em dia nublado o Raio Sapeca continua solto, viu? O protetor também vai.",
    ),
    dict(
        file="09-introducao-alimentar.html", slug="introducao-alimentar", utm="safari", color="sol",
        topic="Saúde da família",
        subject="Do leitinho pro pratinho! Bem-vindo ao Safari das Comidinhas 🥕",
        title="O Safari das Comidinhas: introdução alimentar",
        tagline="Do leitinho pro pratinho! Essa aventura pode ser mais divertida do que assustadora.",
        preheader="Quando começar, como oferecer e o que fica de fora até os 2 anos.",
        intro=[
            "Chegou a hora de trocar o <strong>leitinho</strong> pelo <strong>pratinho</strong>! A introdução alimentar é um verdadeiro safári: cada refeição é uma expedição por cores, cheiros, texturas e sabores.",
            "E, como todo safári, tem bicho que encanta e bicho que assusta (geralmente o brócolis). Respira: essa aventura pode ser muito mais divertida do que assustadora.",
        ],
        summary=[
            "Começa aos 6 meses. Até lá, só leite materno (ou a fórmula orientada pelo pediatra).",
            "Comida amassada com o garfo, nada de liquidificador. E o mesmo cardápio da família, com pouco sal.",
            "Até os 2 anos: nada de açúcar e ultraprocessados. Mel é proibido antes de 1 ano.",
            "Careta não é recusa. Pode ser preciso oferecer o mesmo alimento muitas vezes.",
        ],
        box=("Ânsia ou engasgo?", "Ânsia (careta, tosse, comida para fora) é normal no começo. Engasgo de verdade é silencioso: a criança não chora, não tosse e não respira. Aí, ligue 192."),
        cta_lead="No artigo completo tem o mapa do safári, os alimentos que ficam de fora até os 2 anos e dicas para explorar sem medo.",
        alert="Procure atendimento imediatamente em caso de engasgo sem conseguir respirar, inchaço nos lábios ou olhos depois de um alimento novo, manchas pelo corpo com falta de ar ou vômitos repetidos. Em emergência, ligue 192.",
        closing="Suja, faz careta, joga no chão... e aprende. Aproveite essa fase!",
    ),
]

BULLET = '<tr><td valign="top" style="padding:0 10px {pb}px 0; color:{c}; font-weight:800;">&#9829;</td><td style="padding:0 0 {pb}px; font-weight:700;">{t}</td></tr>'


def render(e):
    k = COLORS[e["color"]]
    border = k.get("border", k["c"])
    art = f'{SITE}/artigos/{e["slug"]}/?{UTM}&utm_content={e["utm"]}'
    home = lambda s: f'{SITE}/?{UTM}&utm_content={e["utm"]}-{s}'
    bullets = "\n".join(
        BULLET.format(c=k["c"] if e["color"] != "sol" else "#E0A12A", t=t, pb=0 if i == len(e["summary"]) - 1 else 10)
        for i, t in enumerate(e["summary"]))
    intro = "\n".join(
        f'<p style="margin:0{" 0 16px" if i < len(e["intro"]) - 1 else ""};">{p}</p>' for i, p in enumerate(e["intro"]))
    return f'''<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="x-apple-disable-message-reformatting">
  <meta name="color-scheme" content="light">
  <meta name="supported-color-schemes" content="light">
  <title>{e["subject"]}</title>
  <!--[if mso]>
  <noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
  <style>td,th,div,p,a,h1,h2,h3{{font-family:Arial,sans-serif!important;}}</style>
  <![endif]-->
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {{ margin: 0; padding: 0; width: 100% !important; background: #FFF4D1; }}
    img {{ border: 0; outline: none; text-decoration: none; display: block; }}
    a {{ color: #1478BC; }}
    @media only screen and (max-width: 620px) {{
      .container {{ width: 100% !important; }}
      .px {{ padding-left: 22px !important; padding-right: 22px !important; }}
      .h1 {{ font-size: 30px !important; line-height: 34px !important; }}
      .hero-img {{ width: 110px !important; height: auto !important; }}
      .stack {{ display: block !important; width: 100% !important; box-sizing: border-box !important; }}
    }}
  </style>
</head>
<body style="margin:0; padding:0; background:#FFF4D1;">
  <!-- Pré-cabeçalho -->
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#FFF4D1;">
    {e["preheader"]}&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;&#8199;&#847;
  </div>

  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFF4D1;">
    <tr>
      <td align="center" style="padding:28px 12px;">

        <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px;">
          <tr>
            <td align="center" style="padding:0 0 14px; font-family:'Nunito',Arial,sans-serif; font-size:12px; color:#6E6378;">
              Não está vendo direito? <a href="{{{{ mirror }}}}" style="color:#6E6378; text-decoration:underline;">Abrir no navegador</a>
            </td>
          </tr>
        </table>

        <table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px; background:#FFFFFF; border:3px solid #3B2F45; border-radius:28px; border-collapse:separate; overflow:hidden;">

          <!-- Cabeçalho -->
          <tr>
            <td class="px" style="padding:22px 36px; border-bottom:2px solid #EDE6EE;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="padding-right:10px;" valign="middle">
                    <a href="{home('logo')}" style="text-decoration:none;">
                      <img src="{SITE}/email/logo.png" width="40" height="40" alt="" style="width:40px; height:40px; border-radius:12px;">
                    </a>
                  </td>
                  <td valign="middle" style="font-family:'Fredoka','Nunito',Arial,sans-serif; line-height:1.1;">
                    <a href="{home('logo')}" style="text-decoration:none;">
                      <span style="font-size:22px; font-weight:700; color:#D63A63;">Tia Mari</span><br>
                      <span style="font-family:'Nunito',Arial,sans-serif; font-size:12px; font-weight:700; color:#6E6378;">Dra. Mariana Rossi · Pediatra</span>
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Destaque -->
          <tr>
            <td style="background:{k["l"]}; border-bottom:3px solid {border};">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td class="px stack" valign="middle" style="padding:30px 10px 30px 36px;">
                    <span style="display:inline-block; background:#FFFFFF; color:{k["c"]}; font-family:'Nunito',Arial,sans-serif; font-weight:800; font-size:12px; padding:5px 12px; border-radius:999px;">Dicas da Tia Mari · {e["topic"]}</span>
                    <h1 class="h1" style="margin:14px 0 0; font-family:'Fredoka','Nunito',Arial,sans-serif; font-weight:700; font-size:34px; line-height:38px; color:#3B2F45;">{e["title"]}</h1>
                    <p style="margin:14px 0 0; display:inline-block; background:#FFFFFF; border:2px solid #3B2F45; border-radius:16px; padding:8px 14px; font-family:'Fredoka','Nunito',Arial,sans-serif; font-weight:600; font-size:16px; line-height:22px; color:{k["d"]};">{e["tagline"]}</p>
                  </td>
                  <td class="stack" valign="bottom" align="center" width="150" style="padding:20px 26px 0 0;">
                    <img class="hero-img" src="{SITE}/email/bento.png" width="130" alt="Bento, o ursinho da Tia Mari" style="width:130px; height:auto;">
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Texto -->
          <tr>
            <td class="px" style="padding:32px 36px 8px; font-family:'Nunito',Arial,sans-serif; font-size:17px; line-height:27px; color:#3B2F45;">
              <p style="margin:0 0 16px; font-weight:700;">Oi, {{{{ contact.FIRSTNAME }}}}!</p>
              {intro}
            </td>
          </tr>

          <!-- Resumo -->
          <tr>
            <td class="px" style="padding:22px 36px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFF4D1; border:3px solid #FFC845; border-radius:22px; border-collapse:separate;">
                <tr>
                  <td style="padding:22px 24px; font-family:'Nunito',Arial,sans-serif; font-size:16px; line-height:24px; color:#3B2F45;">
                    <p style="margin:0 0 12px; font-family:'Fredoka','Nunito',Arial,sans-serif; font-weight:600; font-size:18px; color:#8A5A00;">Resumo da Tia Mari</p>
                    <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                      {bullets}
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Caixa roxa -->
          <tr>
            <td class="px" style="padding:0 36px 8px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#EEE8FF; border-radius:22px; border-collapse:separate;">
                <tr>
                  <td style="padding:18px 22px; font-family:'Nunito',Arial,sans-serif; font-size:16px; line-height:24px; color:#3B2F45;">
                    <span style="font-family:'Fredoka','Nunito',Arial,sans-serif; font-weight:600; font-size:17px; color:#5B3FC0;">{e["box"][0]}</span><br>
                    {e["box"][1]}
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Chamada para o artigo -->
          <tr>
            <td class="px" style="padding:26px 36px 8px; font-family:'Nunito',Arial,sans-serif; font-size:17px; line-height:27px; color:#3B2F45;">
              <p style="margin:0;">{e["cta_lead"]}</p>
            </td>
          </tr>
          <tr>
            <td class="px" align="left" style="padding:22px 36px 30px;">
              <!--[if mso]>
              <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{art}" style="height:54px;v-text-anchor:middle;width:260px;" arcsize="30%" stroke="f" fillcolor="{k["btn"]}">
                <w:anchorlock/><center style="color:#ffffff;font-family:Arial,sans-serif;font-size:18px;font-weight:bold;">Ler o artigo completo</center>
              </v:roundrect>
              <![endif]-->
              <!--[if !mso]><!-->
              <a href="{art}"
                 style="display:inline-block; background:{k["btn"]}; color:#FFFFFF; font-family:'Fredoka','Nunito',Arial,sans-serif; font-weight:600; font-size:19px; line-height:24px; text-decoration:none; padding:15px 28px; border-radius:16px; border-bottom:4px solid {k["btnd"]};">
                Ler o artigo completo &rarr;
              </a>
              <!--<![endif]-->
            </td>
          </tr>

          <!-- Alerta -->
          <tr>
            <td class="px" style="padding:0 36px 26px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#FFE3EA; border:3px solid #D63A63; border-radius:22px; border-collapse:separate;">
                <tr>
                  <td style="padding:18px 22px; font-family:'Nunito',Arial,sans-serif; font-size:15px; line-height:23px; color:#A82748; font-weight:700;">
                    {e["alert"]}
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Convite + assinatura -->
          <tr>
            <td class="px" style="padding:0 36px 32px; font-family:'Nunito',Arial,sans-serif; font-size:17px; line-height:27px; color:#3B2F45;">
              <p style="margin:0 0 22px;">{e["closing"]} Se quiser que eu explique outro tema por aqui, é só responder esta mensagem.</p>
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="background:#EEE8FF; border-radius:22px; border-collapse:separate;" width="100%">
                <tr>
                  <td width="96" valign="middle" style="padding:16px 0 16px 18px;">
                    <img src="{SITE}/email/mariana.png" width="72" height="72" alt="Dra. Mariana Rossi" style="width:72px; height:72px; border-radius:50%; border:3px solid #FFFFFF;">
                  </td>
                  <td valign="middle" style="padding:16px 18px 16px 6px; font-family:'Nunito',Arial,sans-serif; line-height:20px;">
                    <span style="font-size:15px; color:#6E6378;">Com carinho,</span><br>
                    <span style="font-family:'Fredoka','Nunito',Arial,sans-serif; font-size:20px; font-weight:700; color:#7C5CE0;">Tia Mari</span><br>
                    <span style="font-size:13px; font-weight:700; color:#3B2F45;">Dra. Mariana Rossi Oliveira · Pediatra<br>CRM-SP 163730 · RQE 118511</span>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Rodapé -->
          <tr>
            <td class="px" style="background:#3B2F45; padding:24px 36px; font-family:'Nunito',Arial,sans-serif; font-size:13px; line-height:20px; color:#E9E1EC;" align="center">
              <p style="margin:0 0 8px;">Este e-mail é informativo e não substitui consulta médica. Em emergências, ligue 192.</p>
              <p style="margin:0 0 8px;">
                <a href="{home('rodape')}" style="color:#FFFFFF; font-weight:700;">marianarossi.com.br</a>
                &nbsp;·&nbsp;
                <a href="{SITE}/privacidade/" style="color:#FFFFFF;">Privacidade</a>
              </p>
              <p style="margin:0;">Você recebeu este e-mail porque se inscreveu nas Dicas da Tia Mari. <a href="{{{{ unsubscribe }}}}" style="color:#FFFFFF; text-decoration:underline;">Cancelar inscrição</a></p>
            </td>
          </tr>
        </table>

      </td>
    </tr>
  </table>
</body>
</html>
'''


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "emails"
    for e in EMAILS:
        (out / e["file"]).write_text(render(e), encoding="utf-8")
        print(f'{e["file"]}  |  Assunto: {e["subject"]}')
