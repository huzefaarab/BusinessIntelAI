from pathlib import Path
import json
import traceback
from utils.llm import generate_response

from utils.logger import (
    log_execution_trace,
)

from utils.filehandler import (
    read_md,
    save_json,
    save_md,
    create_business_folders,
    extract_business_name,
)

from agents.consultant.prompts import (
    BUSINESS_ANALYSIS_PROMPT,
    STRATEGY_PROMPT,
)

from agents.consultant.market_analytics import (
    run_market_analysis_pipeline,
)

def load_source_pack(source_file_path):
    """
    Loads the uploaded source pack.
    """
    try:
        return read_md(source_file_path)

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Source file was not found: {source_file_path}"
        ) from error


def generate_business_analysis(source_pack):
    """
    Generates business_analysis.md using Gemini.
    """
    try:
        prompt = BUSINESS_ANALYSIS_PROMPT + "\n\n" + source_pack

        analysis_text = generate_response(prompt)

        return analysis_text

    # except Exception as error:
    #     raise RuntimeError(
    #         "Failed to generate analysis.md."
    #     ) from error
    except Exception:

        traceback.print_exc()

        raise


def save_business_analysis(business_name, business_analysis_text):
    """
    Saves business_analysis.md.
    """
    try:
        analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "business_analysis"
            / "business_analysis.md"
        )

        save_md(
            business_analysis_text,
            analysis_path,
        )

    except Exception as error:
        raise RuntimeError(
            "Failed to save analysis.md."
        ) from error
    

def generate_strategy(
    business_name,
):
    """
    Generates strategy.json using
    business_analysis.md and
    market_analysis.md.
    """

    try:

        business_analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "business_analysis"
            / "business_analysis.md"
        )

        market_analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "market_analysis.md"
        )

        business_analysis = read_md(
            business_analysis_path,
        )

        market_analysis = read_md(
            market_analysis_path,
        )

        prompt = (
            STRATEGY_PROMPT
            + "\n\nBUSINESS ANALYSIS:\n\n"
            + business_analysis
            + "\n\nMARKET ANALYSIS:\n\n"
            + market_analysis
        )

        strategy_json = generate_response(
            prompt,
        )

        return strategy_json

    except Exception:

        traceback.print_exc()

        raise

def save_strategy(business_name, strategy_json):
    """
    Saves strategy.json.
    """

    try:
        strategy_path = (
            Path("data")
            / business_name
            / "strategy"
            / "strategy.json"
        )

        strategy_data = json.loads(strategy_json)

        save_json(
            strategy_data,
            strategy_path,
        )

    except Exception as error:
        raise RuntimeError(
            "Failed to save strategy.json."
        ) from error
    

def run_consultant_pipeline(source_file_path):
    """
    Runs the complete Consultant pipeline.

    """

    # ------------------------------------
    # Load Source Pack
    # ------------------------------------

    source_pack = load_source_pack(source_file_path)

    try:
        business_name = extract_business_name(source_pack)

    except Exception as error:
        raise ValueError(
            "Failed to extract the business name from the source pack."
    ) from error

    create_business_folders(business_name)

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Source Pack Loading",
        status="SUCCESS",
        decision="Load source pack.",
        action="Successfully loaded source file.",
        observation="Source pack loaded successfully.",
    )

    # ------------------------------------
    # Generate Business Analysis
    # ------------------------------------

    business_analysis_text = generate_business_analysis(source_pack)

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Business Analysis",
        status="SUCCESS",
        decision="Generate business analysis.",
        action="Called Gemini API.",
        observation="business_analysis.md generated successfully.",
    )

    # ------------------------------------
    # Save Business Analysis
    # ------------------------------------

    save_business_analysis(
        business_name,
        business_analysis_text,
    )

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Save Business Analysis",
        status="SUCCESS",
        decision="Save analysis output.",
        action="Saved business_analysis.md.",
        observation="business_analysis.md saved successfully.",
    )

    # ------------------------------------
    # Market Analysis
    # ------------------------------------

    run_market_analysis_pipeline(
        business_name,
    )       

    
    # ------------------------------------
    # Generate Strategy
    # ------------------------------------

    strategy_json = generate_strategy(
     business_name,
     )

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Content Strategy",
        status="SUCCESS",
        decision="Generate content strategy.",
        action="Called Gemini API.",
        observation="strategy.json generated successfully.",
        )

    # ------------------------------------
    # Save Strategy
    # ------------------------------------

    save_strategy(
        business_name,
        strategy_json,
    )

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Save Strategy",
        status="SUCCESS",
        decision="Save strategy output.",
        action="Saved strategy.json.",
        observation="strategy.json saved successfully.",
   )
    return business_name