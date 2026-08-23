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
    │       ├── 151276388eee_add_document_storage_path.py
    │       ├── 1574707e3088_update_document_tenant_ownership.py
    │       ├── 1a6a80db146c_create_documents_table.py
    │       ├── 24b01039a4fa_add_refresh_token_model.py
    │       ├── 36c7e0953636_change_int_to_string_in_models.py
    │       ├── 4350739915f4_add_unique_constraint_to_tenant_.py
    │       ├── 656ed92886e2_add_models.py
    │       ├── a0adb0b049cc_add_user_tenant_and_tenant_member_models.py
    │       ├── a30f225ffaa0_update_user_model.py
    │       ├── aba3a163568a_create_documents_table.py
    │       ├── b876b4de0f24_change_vector_from_1536_to_768.py
    │       ├── d43e04aca92b_change_plurals_for_documents_and_chunks_.py
    │       ├── d77c73fe1fe4_create_documents_table_with_env_upgrade.py
    │       └── dd1fae7a361b_update_refresh_token_model.py
    ├── alembic.ini
    ├── app
    │   ├── core
    │   │   ├── authorization.py
    │   │   ├── config.py
    │   │   ├── dependencies.py
    │   │   ├── permission.py
    │   │   ├── security.py
    │   │   └── tenant.py
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
    │   │   ├── chunk.py
    │   │   ├── document.py
    │   │   ├── refresh_token.py
    │   │   ├── tenant.py
    │   │   ├── tenant_member.py
    │   │   └── user.py
    │   ├── routes
    │   │   └── api
    │   │       ├── __init__.py
    │   │       └── v1
    │   │           ├── __init__.py
    │   │           ├── auth.py
    │   │           ├── conversations.py
    │   │           ├── document.py
    │   │           ├── router.py
    │   │           ├── search.py
    │   │           ├── tenants.py
    │   │           └── user.py
    │   ├── schemas
    │   │   ├── auth.py
    │   │   ├── document.py
    │   │   ├── search.py
    │   │   ├── tenant.py
    │   │   └── user.py
    │   └── services
    │       ├── auth.py
    │       ├── chunkers.py
    │       ├── document.py
    │       ├── document_parser.py
    │       ├── embedding.py
    │       ├── file_storage.py
    │       ├── retrieval.py
    │       ├── storage.py
    │       ├── tenant.py
    │       └── user.py
    ├── requirements.txt
    ├── storage
    │   └── documents
    │       └── 3
    │           ├── 01bdebe6-defe-4422-a4e0-77f098e0cae9.pdf
    │           ├── 58243850-a805-411d-839a-631676850814.pdf
    │           ├── 60220287-d49c-4109-a6ef-ec5f64d39826.pdf
    │           └── cd0edc01-1e2e-448a-b64a-93af8153b4a6.pdf
    └── test_embedding.py
```
