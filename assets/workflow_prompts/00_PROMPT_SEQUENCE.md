# Coherent prompt sequence — PyMeasure workflow prompts v6

This package renumbers the workflow into one chronological sequence. Use the prompts in the order below.

| Step | File | Purpose | Recommended model | Hardware access |
|---:|---|---|---|---|
| 01 | `prompts/01_prepare_assets_workspace_prompt.md` | Create local planning workspace | `qwen3-coder-next:cloud` or `kimi-k2.6:cloud` | No |
| 02 | `prompts/02_optimize_programming_guide_for_llm_prompt.md` | Optimize Programming Guide for LLM retrieval | `kimi-k2.6:cloud` or `qwen3.6:latest` | No |
| 03 | `prompts/03_optimize_operator_manual_for_llm_prompt.md` | Optimize Operation/Operator Manual for safety and test policy | `kimi-k2.6:cloud` or `qwen3.6:latest` | No |
| 04 | `prompts/04_optimize_service_manual_for_llm_prompt.md` | Optimize Service Manual for service-risk planning | `kimi-k2.6:cloud` or `qwen3.6:latest` | No |
| 05 | `prompts/05_extract_commands_txt_prompt.md` | Extract all commands from Programming Guide to `commands.txt` | `kimi-k2.6:cloud` or `qwen3.6:latest` | No |
| 06 | `prompts/06_verify_manual_artifacts_quality_gate_prompt.md` | Verify manual artifacts and `commands.txt` | `kimi-k2.6:cloud` or `deepseek-v4-pro:cloud` | No |
| 07 | `prompts/07_create_command_coverage_prompt.md` | Create `command_coverage.md` | `kimi-k2.6:cloud` or `deepseek-v4-pro:cloud` | No |
| 08 | `prompts/08_verify_command_coverage_quality_gate_prompt.md` | Verify command coverage completeness and safety classification | `deepseek-v4-pro:cloud` | No |
| 09 | `prompts/09_architecture_and_batches_prompt.md` | Create architecture and batch plan | `deepseek-v4-pro:cloud` | No |
| 10 | `prompts/10_verify_architecture_before_code_quality_gate_prompt.md` | Verify architecture before implementation | `deepseek-v4-pro:cloud` | No |
| 11 | `prompts/11_implementation_batch_01_skeleton_common_status_prompt.md` | Implement batch 1: skeleton/common/status | `qwen3-coder-next:cloud` | No |
| 12 | `prompts/12_verify_implementation_batch_01_quality_gate_prompt.md` | Verify batch 1 implementation | `qwen3-coder-next:cloud` | No |
| 13 | `prompts/13_implementation_batch_template_prompt.md` | Implement one selected subsystem batch | `qwen3-coder-next:cloud` | No |
| 14 | `prompts/14_verify_each_implementation_batch_quality_gate_prompt.md` | Verify each subsystem batch after step 13 | `qwen3-coder-next:cloud` | No |
| 15 | `prompts/15_hardware_execution_decision_gate_prompt.md` | Decide whether hardware tests may run | `qwen3-coder-next:cloud` | Yes, operator decision |
| 16 | `prompts/16_safe_hardware_tests_prompt.md` | Add/refine safe hardware tests | `qwen3-coder-next:cloud` | Yes |
| 17 | `prompts/17_docs_and_final_cleanup_prompt.md` | Documentation and final cleanup | `qwen3-coder-next:cloud` or `deepseek-v4-pro:cloud` | No |
| 18 | `prompts/18_final_pr_audit_quality_gate_prompt.md` | Final PR audit | `deepseek-v4-pro:cloud` or `qwen3-coder-next:cloud` | No |

## Loop rule

Repeat steps **13 → 14** for every implementation batch until the selected scope is complete.

## Hardware rule

The first mandatory physical-device stage is **step 15**. Earlier prompts may contain a VISA address as metadata or as a command-line placeholder, but cloud models cannot access local GPIB/USB/LAN/RS-232 instruments directly.

## Human-in-the-loop rule

Human input should be required only when a report says `HUMAN_REQUIRED: yes`, especially for missing files, ambiguous OCR/manual content, architecture ambiguity, VISA address, physical wiring, unsafe test decisions, or final PR approval.
