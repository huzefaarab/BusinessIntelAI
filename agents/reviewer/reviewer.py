from pathlib import Path

import json

from .prompts import (
    REVIEW_PROMPT,
)

from utils.filehandler import (
    read_json,
    read_md,
)

from utils.llm import (
    generate_response,
)

def review_posts(
    business_name,
):
    """
    Reviews all generated posts.
    """

    issues = []

    posts_path = (

        Path("data")
        / business_name
        / "content"
        / "posts"

    )

    if not posts_path.exists():

        issues.append(
            "Posts folder is missing."
        )

        return issues


    image_count = (

        len(
            list(
                posts_path.glob("*.png")
            )
        )

        +

        len(
            list(
                posts_path.glob("*.jpg")
            )
        )

        +

        len(
            list(
                posts_path.glob("*.jpeg")
            )
        )

    )


    if image_count == 0:

        issues.append(
            "No post images were generated."
        )


    return issues




def review_videos(
    business_name,
):
    """
    Reviews all generated videos.
    """

    issues = []

    videos_path = (

        Path("data")
        / business_name
        / "content"
        / "videos"

    )

    if not videos_path.exists():

        issues.append(
            "Videos folder is missing."
        )

        return issues


    video_folders = sorted(

        videos_path.glob(
            "video_*"
        )

    )


    if len(video_folders) == 0:

        issues.append(
            "No videos were generated."
        )

        return issues


    for folder in video_folders:


        image_count = (

            len(
                list(
                    folder.glob(
                        "*.png"
                    )
                )
            )

            +

            len(
                list(
                    folder.glob(
                        "*.jpg"
                    )
                )
            )

            +

            len(
                list(
                    folder.glob(
                        "*.jpeg"
                    )
                )
            )

        )


        if image_count != 5:

            issues.append(

                f"{folder.name} is missing one or more images."

            )


        if not (

            folder
            / "voiceover.wav"

        ).exists():

            issues.append(

                f"{folder.name} is missing its voiceover."

            )


        if not (

            folder
            / f"{folder.name}.mp4"

        ).exists():

            issues.append(

                f"{folder.name} is missing its mp4 file."

            )


    return issues


def create_creator_outputs(
    issues,
):
    """
    Creates a summary of the Creator outputs.
    """

    if not issues:

        return (

            "All post and video assets were "
            "generated successfully. No "
            "generation issues were found."

        )


    output = (

        "The following generation issues "
        "were found:\n\n"

    )


    for issue in issues:

        output += f"- {issue}\n"


    return output


def create_review_prompt(

    business_name,

    analysis,

    strategy,

    plan,

    creator_outputs,

):
    """
    Creates the reviewer prompt.
    """

    prompt = f"""

{REVIEW_PROMPT}


BUSINESS NAME
-------------

{business_name}


ANALYSIS
--------

{analysis}


STRATEGY
--------

{strategy}


PLAN
----

{plan}


CREATOR OUTPUTS
---------------

{creator_outputs}


Review the generated outputs and return ONLY valid JSON.

"""


    return prompt





def save_review(
    business_name,
    review,
):
    """
    Saves review.json.
    """

    review_path = (

        Path("data")
        / business_name
        / "reviews"

    )

    review_path.mkdir(

        parents=True,

        exist_ok=True,

    )


    with open(

        review_path / "review.json",

        "w",

        encoding="utf-8",

    ) as file:

        json.dump(

            review,

            file,

            indent=4,

            ensure_ascii=False,

        )




def review_content(
    business_name,
):
    """
    Main Reviewer pipeline.
    """

    issues = []

    analysis = read_md(

        Path("data")
        / business_name
        / "analysis"
        / "analysis.md"

    )

    strategy = read_json(

        Path("data")
        / business_name
        / "strategy"
        / "strategy.json"

    )

    plan = read_json(

        Path("data")
        / business_name
        / "plan"
        / "plan.json"

    )


    post_issues = review_posts(
        business_name,
    )

    video_issues = review_videos(
        business_name,
    )


    issues.extend(
        post_issues,
    )

    issues.extend(
        video_issues,
    )


    creator_outputs = create_creator_outputs(
        issues,
    )


    prompt = create_review_prompt(

        business_name,

        analysis,

        strategy,

        plan,

        creator_outputs,

    )


    review = generate_response(

        prompt,

    )


    review = json.loads(

        review,

    )


    if issues:

        review["status"] = (

            "NEEDS_REVISION"

        )

        review["issues"].extend(

            issues,

        )


    save_review(

        business_name,

        review,

    )


    return review