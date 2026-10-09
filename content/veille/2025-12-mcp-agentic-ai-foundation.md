Title: MCP confié à la nouvelle Agentic AI Foundation (Linux Foundation)
Date: 2025-12-09
Category: Veille
Tags: MCP, Anthropic, Linux Foundation, agents IA, standard ouvert
Slug: mcp-agentic-ai-foundation
Summary: Anthropic transfère le Model Context Protocol (MCP) à l'Agentic AI Foundation, créée sous l'égide de la Linux Foundation pour les standards des agents IA.
Source: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation

## Résumé

Le **Model Context Protocol (MCP)**, publié par Anthropic fin 2024, est un protocole ouvert qui standardise la façon dont une application d'IA se connecte à des **outils** et à des **sources de données** (fichiers, bases de données, applications métiers). En un an, il a été adopté par de nombreux éditeurs et outils de développement.

En décembre 2025, Anthropic a annoncé **confier MCP à l'Agentic AI Foundation (AAIF)**, une nouvelle fondation placée sous l'égide de la **Linux Foundation**, destinée à accueillir les projets open source liés aux agents IA.

## Comment fonctionne MCP (simplifié)

```text
[Application IA / agent]  <-- client MCP -->  [Serveur MCP]  -->  outil ou données
                                               (ex : agenda, base SQL, GitHub)
```

Un **serveur MCP** expose des *outils* (actions que l'agent peut appeler), des *ressources* (données à lire) et des *prompts*. Il suffit de développer un serveur MCP une fois pour que tous les agents compatibles puissent l'utiliser.

## Ce que ça change pour un développeur

- Pour rendre une application « utilisable par des agents », on peut lui ajouter un **serveur MCP** (des SDK officiels existent, notamment en Python, TypeScript et Java/Kotlin).
- La gouvernance neutre facilite l'adoption par les entreprises.
- La **sécurité** devient centrale : un agent qui peut agir doit avoir des droits limités (principe du moindre privilège).

## Mon avis

C'est le sujet qui m'a le plus marqué pendant mon stage : une plateforme d'orchestration d'agents pour PME repose précisément sur ce type de connecteurs.
