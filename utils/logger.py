import json
from datetime import datetime
from pathlib import Path


def _get_timestamp():
    """Returns the current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _write_jsonl(file_path, data):
    """Appends a JSON object to a .jsonl file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(json.dumps(data) + "\n")


def log_execution_trace(
    business_name,
    layer,
    step,
    status,
    decision,
    action,
    observation,
    error=None,
):
    """
    Logs execution traces for every step of the pipeline.
    """

    log_data = {
        "timestamp": _get_timestamp(),
        "business_name": business_name,
        "layer": layer,
        "step": step,
        "status": status,
        "decision": decision,
        "action": action,
        "observation": observation,
        "error": error,
    }

    file_path = (
        Path("data")
        / business_name
        / "logs"
        / "execution_trace.jsonl"
    )

    _write_jsonl(file_path, log_data)


def log_spend(
    business_name,
    layer,
    model,
    input_tokens,
    output_tokens,
    total_tokens,
    cost_inr,
    budget_limit=100,
    status="WITHIN LIMIT",
):
    """
    Logs token usage and spending information for every LLM call.
    """

    spend_data = {
        "timestamp": _get_timestamp(),
        "business_name": business_name,
        "layer": layer,
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "cost_inr": cost_inr,
        "budget_limit": budget_limit,
        "status": status,
    }

    file_path = (
        Path("data")
        / business_name
        / "logs"
        / "spend_logs.jsonl"
    )

    _write_jsonl(file_path, spend_data)


def log_human_checkpoint(
    business_name,
    step,
    status,
    observation,
):
    """
    Logs human approval checkpoints.
    """

    checkpoint_data = {
        "timestamp": _get_timestamp(),
        "business_name": business_name,
        "layer": "Human Checkpoint",
        "step": step,
        "status": status,
        "decision": "Awaiting human decision.",
        "action": "Pipeline execution paused.",
        "observation": observation,
        "error": None,
    }

    file_path = (
        Path("data")
        / business_name
        / "logs"
        / "execution_trace.jsonl"
    )

    _write_jsonl(file_path, checkpoint_data)