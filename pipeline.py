import sys

from agents.consultant.consultant import (
    run_consultant_pipeline,
)

from agents.creator.creator import (
    run_creator_pipeline,
)

from agents.reviewer.reviewer import (
    review_content,
)



def run_pipeline(
    source_file_path,
    generation_mode="free",
):
    """
    Runs the complete BusinessIntelAI
    pipeline.
    """

    print(
        "\n===== CONSULTANT =====\n"
    )

    business_name = (

        run_consultant_pipeline(
            source_file_path,
        )

    )


    print(
        "\n===== CREATOR =====\n"
    )

    run_creator_pipeline(

    business_name=business_name,
    generation_mode=generation_mode,

   )


    print(
        "\n===== REVIEWER =====\n"
    )

    review_content(

        business_name,
        generation_mode,

    )


    print(

        "\n===== PIPELINE COMPLETED SUCCESSFULLY =====\n"

    )

    return business_name


if __name__ == "__main__":

    if len(sys.argv) < 2:

        sys.exit(
            "Usage: python pipeline.py <source_file.md> [free|premium]"
        )

    run_pipeline(
        source_file_path=sys.argv[1],
        generation_mode=(
            sys.argv[2].lower()
            if len(sys.argv) > 2
            else "free"
        ),
    )