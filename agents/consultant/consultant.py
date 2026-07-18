from pathlib import Path
import json
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


ANALYSIS_PROMPT = """
ROLE:
You are an expert Business Consultant.

TASK:
Analyze the business context.

CONSTRAINTS:
1. Summarize what the business sells.
2. Identify its target audience.
3. Identify its strongest offers.
4. Identify its brand voice.
5. Identify customer needs.
6. Identify trust signals.
7. Identify local or seasonal opportunities.
8. Clearly separate observed facts from assumptions.
9. Mention missing information whenever necessary.
10. Do not hallucinate information.

OUTPUT FORMAT:
Generate the response in markdown format.

INPUT:
"""


STRATEGY_PROMPT = """
ROLE:
You are an expert Marketing Strategist.

TASK:
Generate a content strategy based on the provided business analysis.

CONSTRAINTS:
1. Identify the primary content pillars.
2. Identify the target audience segments.
3. Identify the appropriate brand voice.
4. Identify the marketing opportunities.
5. Identify the posting goals.
6. Recommend suitable content directions.
7. Include any additional recommendations if necessary.

OUTPUT FORMAT:
Return ONLY valid JSON in the following format.

{
    "content_pillars": [],

    "target_audience": [],

    "brand_voice": [],

    "posting_goals": [],

    "marketing_opportunities": [],

    "recommended_content_directions": [],

    "additional_recommendations": []
}

IMPORTANT:
1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Do NOT add explanations outside the JSON.
5. Every field must always be present.

INPUT:
"""


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


def generate_analysis(source_pack):
    """
    Generates analysis.md using Gemini.
    """
    try:
        prompt = ANALYSIS_PROMPT + "\n\n" + source_pack

        analysis_text = generate_response(prompt)

        return analysis_text

    except Exception as error:
        raise RuntimeError(
            "Failed to generate analysis.md."
        ) from error


def save_analysis(business_name, analysis_text):
    """
    Saves analysis.md.
    """
    try:
        analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "analysis.md"
        )

        save_md(
            analysis_text,
            analysis_path,
        )

    except Exception as error:
        raise RuntimeError(
            "Failed to save analysis.md."
        ) from error
    

def generate_strategy(business_name):
    """
    Generates strategy.json using analysis.md.
    """

    try:
        analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "analysis.md"
        )

        analysis_text = read_md(analysis_path)

        prompt = STRATEGY_PROMPT + "\n\n" + analysis_text

        strategy_json = generate_response(prompt)

        return strategy_json

    except Exception as error:
        raise RuntimeError(
            "Failed to generate strategy.json."
        ) from error
    

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
    # Generate Analysis
    # ------------------------------------

    analysis_text = generate_analysis(source_pack)

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Business Analysis",
        status="SUCCESS",
        decision="Generate business analysis.",
        action="Called Gemini API.",
        observation="analysis.md generated successfully.",
    )

    # ------------------------------------
    # Save Analysis
    # ------------------------------------

    save_analysis(
        business_name,
        analysis_text,
    )

    log_execution_trace(
        business_name=business_name,
        layer="Consultant",
        step="Save Analysis",
        status="SUCCESS",
        decision="Save analysis output.",
        action="Saved analysis.md.",
        observation="analysis.md saved successfully.",
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