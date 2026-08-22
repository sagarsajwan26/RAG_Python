# Project Tree: project

```text
project/
├── .gitignore
├── client
│   ├── .env.local
│   ├── .gitignore
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── README.md
│   ├── app
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   ├── lib
│   │   │   └── client.ts
│   │   └── page.tsx
│   ├── components
│   ├── eslint.config.mjs
│   ├── lib
│   │   └── client.ts
│   ├── next-env.d.ts
│   ├── next.config.ts
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.mjs
│   ├── public
│   │   ├── file.svg
│   │   ├── globe.svg
│   │   ├── next.svg
│   │   ├── vercel.svg
│   │   └── window.svg
│   ├── tsconfig.json
│   └── types
├── docker-compose.yml
├── generate_tree.py
└── server
    ├── .env
    ├── alembic
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       ├── 24b01039a4fa_add_refresh_token_model.py
    │       ├── 36c7e0953636_change_int_to_string_in_models.py
    │       ├── 656ed92886e2_add_models.py
    │       ├── a0adb0b049cc_add_user_tenant_and_tenant_member_models.py
    │       ├── a30f225ffaa0_update_user_model.py
    │       ├── d43e04aca92b_change_plurals_for_documents_and_chunks_.py
    │       └── dd1fae7a361b_update_refresh_token_model.py
    ├── alembic.ini
    ├── app
    │   ├── core
    │   │   ├── config.py
    │   │   ├── dependencies.py
    │   │   └── security.py
    │   ├── database
    │   │   ├── __init__.py
    │   │   ├── dependencies.py
    │   │   └── session.py
    │   ├── main.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── chunks.py
    │   │   ├── documents.py
    │   │   ├── refresh_token.py
    │   │   ├── tenant.py
    │   │   ├── tenant_member.py
    │   │   └── user.py
    │   ├── repositories
    │   │   ├── refresh_token.py
    │   │   └── user.py
    │   ├── routes
    │   │   └── api
    │   │       ├── __init__.py
    │   │       └── v1
    │   │           ├── __init__.py
    │   │           ├── auth.py
    │   │           ├── conversations.py
    │   │           ├── documents.py
    │   │           ├── router.py
    │   │           ├── tenants.py
    │   │           └── user.py
    │   ├── schemas
    │   │   ├── auth.py
    │   │   └── user.py
    │   └── services
    │       ├── auth.py
    │       └── user.py
    └── requirements.txt
```
