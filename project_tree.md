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
│   │   │   └── api.ts
│   │   └── page.tsx
│   ├── eslint.config.mjs
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
│   └── tsconfig.json
├── docker-compose.yml
├── generate_tree.py
└── server
    ├── .env
    ├── alembic
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    ├── alembic.ini
    └── app
        ├── core
        │   └── config.py
        ├── database
        │   ├── __init__.py
        │   ├── dependencies.py
        │   └── session.py
        ├── main.py
        ├── models
        │   ├── __init__.py
        │   ├── base.py
        │   └── user.py
        ├── repositories
        │   └── user.py
        ├── routes
        ├── schemas
        │   └── user.py
        └── services
            └── user.py
```
