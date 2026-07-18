from agents.consultant.consultant import (
    run_consultant_pipeline,
)

from agents.creator.creator import (
    run_creator_pipeline,
)

from agents.reviewer.reviewer import (
    review_content,
)


SOURCE_FILE_PATH = (
    "source_files/ken's bakery.md"
)


def run_pipeline():
    """
    Runs the complete BusinessIntelAI
    pipeline.
    """

    print(
        "\n===== CONSULTANT =====\n"
    )

    business_name = (

        run_consultant_pipeline(
            SOURCE_FILE_PATH,
        )

    )


    print(
        "\n===== CREATOR =====\n"
    )

    run_creator_pipeline(

        business_name,

    )


    print(
        "\n===== REVIEWER =====\n"
    )

    review_content(

        business_name,

    )


    print(

        "\n===== PIPELINE COMPLETED SUCCESSFULLY =====\n"

    )


if __name__ == "__main__":

    run_pipeline()