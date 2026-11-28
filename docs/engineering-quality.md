# FlowEngine — engineering quality / engenharia

Owner and maintainer: João Victor da Silva (JustJao1).

EN: Visual JSON workflow orchestration.
PT: Orquestração visual de fluxos JSON.

## Architecture
```mermaid
flowchart LR
 UI[HTML / CSS / JavaScript] --> API[Python workspace API]
 API --> Core[Domain operations]
 Core --> DB[(Temporary SQLite)]
 API --> UI
```
Browser snapshots are reconstructed per request. This is a bounded portfolio sandbox, not a shared production database.

## Decision record / decisões
ADR-001: Validate graph connections and reject cycles before execution; controlled endpoints avoid external network access.
ADR-002: Use loopback-only local access; the Docker port is published to the host loopback and no real credentials are included.

## Run / Executar
Python 3.11: pip install -r requirements.txt; python run.py.
Docker: docker compose up --build --wait; open http://127.0.0.1:8765/. Stop with docker compose down. Base image patch versions and any dependency ranges can change on rebuild; use lockfiles and digests for byte-identical production builds. Do not expose the demo publicly from this container.

## Verification
Run python -m unittest discover -s tests -v. The [CI workflow](https://github.com/JustJao1/flow-engine/actions/workflows/engineering-quality.yml) publishes actual test logs and branch coverage, and checks the container health. Coverage is not a claim of complete end-to-end testing.

## Technical demo (EN)
Build a set → condition → output flow, run both branches and inspect the trace; try an invalid cycle.

## Demonstração (PT)
Monte um fluxo set → condition → output, execute os dois ramos e confira o trace; tente um ciclo inválido.

## Limitations
Manual sandbox executions, not a persistent scheduler. HTTP nodes use controlled samples.

## AI-assisted review
Inspect diffs, validate input and authorization boundaries, run tests, and inspect CI output before merging. Do not share secrets or customer data. This is a proposed ongoing review procedure, not evidence about every historical change.
