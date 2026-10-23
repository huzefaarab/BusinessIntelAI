from pathlib import Path
import json

from utils.filehandler import (
    read_json,
    read_md,
    save_json,
    save_md,
)

from utils.llm import generate_response

from utils.logger import (
    log_execution_trace,
)

from utils.websearch import (
    web_search,
)

from agents.consultant.prompts import (
    MARKET_ANALYSIS_PROMPT,
    MARKET_RESEARCH_QUERY_PROMPT,
)


def load_business_analysis(
    business_name,
):
    """
    Loads business_analysis.md.
    """

    try:

        analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "business_analysis"
            / "business_analysis.md"
        )

        return read_md(
            analysis_path,
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to load business_analysis.md."
        ) from error


def load_research_queries(
    business_name,
):
    """
    Loads research_queries.json.
    """

    try:

        queries_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "research_queries.json"
        )

        return read_json(
            queries_path,
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to load research_queries.json."
        ) from error


def load_search_results(
    business_name,
):
    """
    Loads search_results.json.
    """

    try:

        results_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "search_results.json"
        )

        return read_json(
            results_path,
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to load search_results.json."
        ) from error


def generate_research_queries(
    business_name,
    business_analysis,
):
    """
    Generates categorized research
    queries from the business analysis.
    """

    try:

        prompt = (
            MARKET_RESEARCH_QUERY_PROMPT
            + "\n\n"
            + business_analysis
        )

        response = generate_response(
            prompt,
        )

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Research Query Generation",
            status="SUCCESS",
            decision="Generate market research queries.",
            action="Called Gemini API.",
            observation="research_queries.json generated successfully.",
        )

        return json.loads(
            response,
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to generate research queries."
        ) from error


def save_research_queries(
    business_name,
    research_queries,
):
    """
    Saves research_queries.json.
    """

    try:

        queries_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "research_queries.json"
        )

        save_json(
            research_queries,
            queries_path,
        )

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Save Research Queries",
            status="SUCCESS",
            decision="Save research queries.",
            action="Saved research_queries.json.",
            observation="research_queries.json saved successfully.",
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to save research_queries.json."
        ) from error


def execute_web_searches(
    business_name,
    research_queries,
):
    """
    Executes web searches for every
    generated research query.
    """

    try:

        search_results = {}

        for category, queries in research_queries.items():

            category_results = []

            for query in queries:

                results = web_search(
                    query=query,
                    max_results=5,
                )

                category_results.append(
                    {
                        "query": query,
                        "results": results,
                    }
                )

            search_results[category] = category_results

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Web Search",
            status="SUCCESS",
            decision="Execute market research queries.",
            action="Executed DuckDuckGo web searches.",
            observation="search_results.json generated successfully.",
        )

        return search_results

    except Exception as error:

        raise RuntimeError(
            "Failed to execute web searches."
        ) from error


def save_search_results(
    business_name,
    search_results,
):
    """
    Saves search_results.json.
    """

    try:

        results_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "search_results.json"
        )

        save_json(
            search_results,
            results_path,
        )

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Save Search Results",
            status="SUCCESS",
            decision="Save search results.",
            action="Saved search_results.json.",
            observation="search_results.json saved successfully.",
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to save search_results.json."
        ) from error


def generate_market_analysis(
    business_name,
    business_analysis,
    search_results,
):
    """
    Generates market_analysis.md.
    """

    try:

        prompt = (
            MARKET_ANALYSIS_PROMPT
            + "\n\nBUSINESS ANALYSIS:\n\n"
            + business_analysis
            + "\n\nSEARCH RESULTS:\n\n"
            + json.dumps(
            search_results,
            indent=4,
        )
)

        market_analysis = generate_response(
            prompt,
        )

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Market Analysis Generation",
            status="SUCCESS",
            decision="Generate market analysis.",
            action="Called Gemini API.",
            observation="market_analysis.md generated successfully.",
        )

        return market_analysis

    except Exception as error:

        raise RuntimeError(
            "Failed to generate market_analysis.md."
        ) from error


def save_market_analysis(
    business_name,
    market_analysis,
):
    """
    Saves market_analysis.md.
    """

    try:

        analysis_path = (
            Path("data")
            / business_name
            / "analysis"
            / "market_analysis"
            / "market_analysis.md"
        )

        save_md(
            market_analysis,
            analysis_path,
        )

        log_execution_trace(
            business_name=business_name,
            layer="Market Analysis",
            step="Save Market Analysis",
            status="SUCCESS",
            decision="Save market analysis.",
            action="Saved market_analysis.md.",
            observation="market_analysis.md saved successfully.",
        )

    except Exception as error:

        raise RuntimeError(
            "Failed to save market_analysis.md."
        ) from error


def run_market_analysis_pipeline(
    business_name,
):
    """
    Executes the complete market
    research pipeline.
    """

    # ------------------------------------
    # Load Business Analysis
    # ------------------------------------

    business_analysis = load_business_analysis(
        business_name,
    )

    # ------------------------------------
    # Generate Research Queries
    # ------------------------------------

    research_queries = generate_research_queries(
        business_name,
        business_analysis,
    )

    # ------------------------------------
    # Save Research Queries
    # ------------------------------------

    save_research_queries(
        business_name,
        research_queries,
    )

    # ------------------------------------
    # Load Research Queries
    # ------------------------------------

    research_queries = load_research_queries(
        business_name,
    )

    # ------------------------------------
    # Execute Web Searches
    # ------------------------------------

    search_results = execute_web_searches(
        business_name,
        research_queries,
    )

    # ------------------------------------
    # Save Search Results
    # ------------------------------------

    save_search_results(
        business_name,
        search_results,
    )

    # ------------------------------------
    # Load Search Results
    # ------------------------------------

    search_results = load_search_results(
        business_name,
    )

    # ------------------------------------
    # Generate Market Analysis
    # ------------------------------------

    market_analysis = generate_market_analysis(
        business_name,
        business_analysis,
        search_results,
    )

    # ------------------------------------
    # Save Market Analysis
    # ------------------------------------

    save_market_analysis(
        business_name,
        market_analysis,
    )

    return market_analysis