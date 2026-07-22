from pathlib import Path
import json

from utils.llm import (
    generate_response,
)

from utils.logger import (
    log_execution_trace,
)

from utils.filehandler import (
    read_json,
    save_json,
)

from utils.llm import (
    generate_response,
    generate_image,
    generate_voiceover,
)

from utils.video import (
    create_video,
)

from agents.creator.prompts import (
    PLAN_PROMPT,
    POST_PROMPT,
    VIDEO_PROMPT,
)


def generate_plan(business_name):
    """
    Generates plan.json using strategy.json.
    """

    try:

        strategy_path = (
            Path("data")
            / business_name
            / "strategy"
            / "strategy.json"
        )

        strategy_json = read_json(
            strategy_path,
        )

        prompt = (
            PLAN_PROMPT
            + "\n\n"
            + json.dumps(
                strategy_json,
                indent=4,
            )
        )

        plan_json = generate_response(
            prompt,
        )

        return plan_json

    except Exception as error:
        raise RuntimeError(
            "Failed to generate plan.json."
        ) from error


def save_plan(
    business_name,
    plan_json,
):
    """
    Saves plan.json.
    """

    try:

        plan_path = (
            Path("data")
            / business_name
            / "plan"
            / "plan.json"
        )

        plan_data = json.loads(
            plan_json,
        )

        save_json(
            plan_data,
            plan_path,
        )

    except Exception as error:
        raise RuntimeError(
            "Failed to save plan.json."
        ) from error


def generate_post(
    business_name,
    item,
    post_number
):
    """
    Generates one complete post.
    """

    try:

        prompt = (

            POST_PROMPT
            + "\n\n"
            + json.dumps(
                item,
                indent=4,
            )

        )

        post_json = generate_response(
            prompt,
        )

        post_data = json.loads(
            post_json,
        )

        # ------------------------------------
        # Create Posts Folder
        # ------------------------------------

        post_folder_path = (

            Path("data")
            / business_name
            / "content"
            / "posts"

        )

        post_folder_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        # ------------------------------------
        # Generate Post Image
        # ------------------------------------

        output_path = (

            post_folder_path
            / f"post_{post_number}.png"

        )

        generate_image(

            post_data["image_prompt"],
            output_path,

        )

        # ------------------------------------
        # Log Success
        # ------------------------------------

        log_execution_trace(

            business_name=business_name,
            layer="Creator",
            step=f"Generate Post {post_number}",
            status="SUCCESS",
            decision="Generate one static post.",
            action="Generated the post content and image.",
            observation=f"Post {post_number} generated successfully.",

        )

    except Exception as error:

        raise RuntimeError(
            f"Failed to generate Post {post_number}."
        ) from error   
    

def generate_video(
    business_name,
    item,
    video_number,
    
):
    """
    Generates one complete video.
    """

    try:

        prompt = (

            VIDEO_PROMPT
            + "\n\n"
            + json.dumps(
                item,
                indent=4,
            )

        )

        video_json = generate_response(
            prompt,
        )

        video_data = json.loads(
            video_json,
        )

        # --------------------------------
        # Create Video Folder
        # --------------------------------

        video_folder = (

            Path("data")
            / business_name
            / "content"
            / "videos"
            / f"video_{video_number}"

        )

        video_folder.mkdir(

            parents=True,
            exist_ok=True,

        )

        # --------------------------------
        # Generate Images
        # --------------------------------

        image_paths = []

        for image_number in range(1, 6):

            image_path = (

                video_folder
                / f"image_{image_number}.png"

            )

            pollinations_prompt = f"""

IMPORTANT:

This is Image {image_number} of 5.

This image is NOT independent.

It will later be combined with four other
visually consistent images to generate ONE
short-form cinematic video.

The generated video will use:
- zoom effects
- smooth transitions
- voiceover narration
- short-form cinematic storytelling.

Maintain:
- identical lighting.
- identical visual aesthetics.
- identical business branding.
- identical color palette.
- visual continuity across all five images.

This image must naturally progress the visual
story while remaining visually consistent with
the other generated images.

The final output should feel like five
consecutive scenes from the same premium
cinematic short-form video.


BASE IMAGE PROMPT:

{video_data["image_prompt"]}


IMAGE VARIATION:

{video_data["image_variations"][image_number - 1]}


"""

            generate_image(

                pollinations_prompt,
                image_path,

            )

            image_paths.append(
                image_path,
            )

        # --------------------------------
        # Generate Voiceover
        # --------------------------------

        voiceover_path = (

            video_folder
            / "voiceover.wav"

        )

        generate_voiceover(

            video_data[
                "voiceover_script"
            ],

            voiceover_path,

        )

        # --------------------------------
        # Generate Video
        # --------------------------------

        output_path = (

            video_folder
            / f"video_{video_number}.mp4"

        )

        create_video(

            image_paths=image_paths,

            audio_path=voiceover_path,

            output_path=output_path,

        )

        # --------------------------------
        # Execution Trace
        # --------------------------------

        log_execution_trace(

            business_name=business_name,

            layer="Creator",

            step=f'Generate Video {video_number}',

            status="SUCCESS",

            decision="Generate one complete video.",

            action=(
                "Generated the images, "
                "voiceover and mp4 video."
            ),

            observation=(
                f'Video {video_number} '
                "generated successfully "
                "with voiceover narration."
            ),

        )

        return output_path

    except Exception as error:

        raise RuntimeError(

            f'Failed to generate Video {video_number}.'

        ) from error

def run_creator_pipeline(
    business_name,
):
    """
    Runs the complete Creator pipeline.
    """

    # ------------------------------------
    # Generate Plan
    # ------------------------------------

    plan_json = generate_plan(
        business_name,
    )

    log_execution_trace(
        business_name=business_name,
        layer="Creator",
        step="Content Planning",
        status="SUCCESS",
        decision="Generate the 7-day content plan.",
        action="Called Gemini API.",
        observation="plan.json generated successfully.",
    )

    # ------------------------------------
    # Save Plan
    # ------------------------------------

    save_plan(
        business_name,
        plan_json,
    )

    log_execution_trace(
        business_name=business_name,
        layer="Creator",
        step="Save Plan",
        status="SUCCESS",
        decision="Save the generated content plan.",
        action="Saved plan.json.",
        observation="plan.json saved successfully.",
    )

    # ------------------------------------
    # Generate Static Posts
    # ------------------------------------

    plan_path = (
        Path("data")
        / business_name
        / "plan"
        / "plan.json"
    )

    plan = read_json(
        plan_path,
    )

    post_number = 1
    for item in plan:

        if item["type"] == "Post":

            generate_post(
                business_name,
                item,
                post_number,
            )
            post_number += 1

    # ------------------------------------
    # Video Generation
    # ------------------------------------

    # ------------------------------------
    # Generate Videos
    # ------------------------------------
    
    video_number = 1

    for item in plan:
    
        if item["type"] == "Video":
        
            generate_video(
            
                business_name,
                item,
                video_number,
    
            )
            video_number += 1
    
    
    return business_name