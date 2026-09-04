# T2M Managed Test Project — Project Context

## Purpose & Scope
This project serves as a canonical reference implementation for T2M Multi-Agent Protocol compliance. It contains core utility functions and verified documentation for state reconstruction across independent agents.

## Architecture
- **Language**: Python 3
- **Test Framework**: `unittest`
- **Canonical Remote**: `https://github.com/t2mmanila-rgb/t2m-managed-test-project`

## Multi-Agent Protocol Rules
1. Every agent MUST read `PROJECT_STATUS.md` and `PROJECT_CONTEXT.md` before initiating changes.
2. Only verified, tested functionality may be marked as completed in `PROJECT_STATUS.md`.
3. State handoff occurs strictly through GitHub commit pushes, not conversation memory.
