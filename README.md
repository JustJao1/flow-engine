# FlowEngine

Visual workflow editor for branching JSON transformations.

[Live demonstration](https://portfolio-suite-jv.vercel.app/flow) · [Developer portfolio](https://jv-software-portfolio.vercel.app/)

**Owner and maintainer:** João Victor da Silva ([JustJao1](https://github.com/JustJao1)).

## What it does

Configurable nodes, conditional branches, execution traces, saved flows and guided examples.

## Architecture

A dedicated HTML/CSS/JavaScript workspace backed by Python request handling and SQLite domain operations. The hosted sandbox reconstructs temporary state from a browser-local snapshot; it is not a persistent multi-user database. External server-side requests are limited to controlled examples.

## Run locally

Requires Python 3.11+.

```sh
python -m venv .venv
# Activate the environment, then:
python -m pip install -r requirements.txt
python run.py
```

Open http://127.0.0.1:8765/ in your browser. The local runner reproduces the bounded demo and binds to loopback only.

## Tests

```sh
python -m unittest discover -s tests -v
```

The tests cover core sandbox operations. Browser rendering and external dependencies need separate validation.

## Current status

Portfolio demonstration, not a production service. Online HTTP nodes use fixed sample endpoints. Execution is manual in the hosted demo; persistent scheduling is not provided.

See [ownership](OWNERSHIP.md) and [third-party notices](THIRD_PARTY_NOTICES.md).
