# Model selection and hardware access policy

## Recommended models

| Workflow area | Recommended model | Notes |
|---|---|---|
| Large manual analysis, Markdown optimization, command extraction | `kimi-k2.6:cloud` or `qwen3.6:latest` | Prefer long-context/fact-retrieval models. |
| Architecture, class design, safety policy, batch planning | `deepseek-v4-pro:cloud` | Prefer strongest reasoning. |
| Driver code, tests, documentation, cleanup | `qwen3-coder-next:cloud` | Prefer coding-specialized model. |
| Visual diagrams, screenshots, OCR-sensitive figures | `qwen3-vl:235b-cloud` | Use only when diagrams/images must be interpreted. |

## Hardware access

- Steps 01–14: no physical device is required.
- Step 15: physical device access and operator decision are required.
- Step 16: physical device access is required if tests are executed.
- Steps 17–18: no physical device is required unless the operator chooses to re-run safe hardware tests before PR.

A VISA address is meaningful only on the computer or local runner connected to the instrument. It may be inserted into generated local test commands, but a remote cloud model cannot communicate with a local instrument by seeing the address.
