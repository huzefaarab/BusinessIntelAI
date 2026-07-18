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

PLAN_PROMPT = """
ROLE:
You are an expert Content Strategist.

TASK:
Create the complete 7-day content plan for the business based on the provided first-week content strategy.

CONSTRAINTS:
1. Generate exactly 7 content items.
2. Generate exactly 5 Posts.
3. Generate exactly 2 Videos.
4. Every content item must align with the week's objective.
5. Every content item must align with the target audience.
6. Every content item must align with the week's content pillars.
7. Every content item must align with the business tone and key marketing messages.
8. Include suitable calls-to-action.
9. Clearly specify the content type for every day.
10. Ensure all strategic choices are specific to the business.
11. Do not hallucinate information. Make reasonable assumptions whenever necessary and clearly state them.

OUTPUT FORMAT:

Return ONLY valid JSON in the following format.


[
    {
        "day":1,
        "type":"",
        "topic":"",
        "hook":"",
        "caption_direction":"",
        "visual_direction":"",
        "cta":"",
        "insight":""
    }
]


IMPORTANT:
1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Generate exactly 7 content items.
5. Generate exactly 5 Posts.
6. Generate exactly 2 Videos.
7. Every field must always be present.

INPUT:
"""

POST_PROMPT = """
ROLE:

You are an expert Social Media Content Creator.


TASK:

Generate ONE complete static post creative
using the provided content plan item.


CONSTRAINTS:

1. Generate content for ONLY ONE post.
2. Generate a suitable caption.
3. Generate suitable hashtags.
4. Generate a suitable call-to-action.
5. Generate a detailed image generation prompt.
6. Ensure the generated image prompt aligns
with the provided visual direction.
7. Ensure the caption aligns with the provided
topic, hook, caption direction and insight.
8. Ensure the content remains visually
consistent with the business.
9. Never generate content unrelated to the
provided content plan item.


OUTPUT FORMAT:

Return ONLY valid JSON.


{

    "caption":"",

    "hashtags":[

        "#.....",
        "#....."

    ],

    "cta":"",

    "image_prompt":""

}


IMPORTANT:

1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Generate content for ONLY ONE POST.
5. Every field must always be present.


INPUT:

"""


VIDEO_PROMPT = """
ROLE:

You are an expert Social Media Video Creator.


TASK:

Generate ONE complete short-form cinematic video
creative using the provided content plan item.


CONSTRAINTS:

1. Generate content for ONLY ONE video.
2. Generate a suitable caption.
3. Generate suitable hashtags.
4. Generate a suitable call-to-action.
5. Generate ONE detailed base image generation prompt.
6. Generate FIVE image variations that collectively tell ONE progressing visual story.
7. Generate a suitable voiceover script.
8. Generate suitable audio directions.
9. Suggest the appropriate video duration.
10. Ensure the generated content aligns with the provided topic, hook, caption direction, visual direction and insight.
11. Never generate content unrelated to the provided content plan item.


IMPORTANT:

The generated outputs will NOT be used independently.

They will collectively be used for generating
ONE short-form cinematic video.

The generated video will later use:
- 5 visually consistent images.
- Zoom effects.
- Smooth transitions.
- Voiceover narration.
- Short-form visual storytelling.


IMAGE REQUIREMENTS:

1. The five generated images must tell ONE progressing visual story.
2. The images must NOT feel independent.
3. Every image should naturally transition into the next image.
4. Maintain visual consistency across:
    - lighting
    - visual aesthetics
    - environment
    - business branding
    - color palette.
5. The fifth image should naturally conclude the visual story.
6. The five generated images should feel like five consecutive scenes from the same premium cinematic short-form video.
7. The generated base image prompt and image variations should collectively ensure visual continuity across all five images.


VOICEOVER REQUIREMENTS:

1. Generate a suitable voiceover script that will be narrated alongside the generated short-form video.
2. The generated voiceover must complement:
    - the visual progression
    - the business tone
    - the pacing of the generated video.
3. The voiceover should naturally complement the beginning, progression and conclusion of the visual story.
4. Keep the video duration in mind while generating the voiceover script.
5. Ensure that the generated voiceover feels like it belongs to the generated short-form video.
6. Prefer warm, engaging and natural sounding narration unless otherwise required.


VIDEO REQUIREMENTS:

1. The generated video will later use:
    - zoom effects
    - smooth transitions
    - voiceover narration.
2. Keep this in mind while generating every output.
3. Ensure that all generated outputs complement each other and belong to the same short-form video.


OUTPUT FORMAT:

Return ONLY valid JSON.


{

    "caption":"",

    "hashtags":[

        "#.....",
        "#....."

    ],

    "cta":"",

    "image_prompt":"",

    "image_variations":[

        "",
        "",
        "",
        "",
        ""

    ],

    "voiceover_script":"",

    "audio_direction":"",

    "video_duration":""

}


IMPORTANT:

1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Generate content for ONLY ONE VIDEO.
5. Every field must always be present.
6. Generate EXACTLY FIVE image variations.


INPUT:

"""



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
            / f'post_{item["day"]}.png'

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
            step=f'Generate Post {item["day"]}',
            status="SUCCESS",
            decision="Generate one static post.",
            action="Generated the post content and image.",
            observation=f'Post {item["day"]} generated successfully.',

        )

    except Exception as error:

        raise RuntimeError(
            f'Failed to generate Post {item["day"]}.'
        ) from error   
    

def generate_video(
    business_name,
    item,
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
            / f'video_{item["day"]}'

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
            / f'video_{item["day"]}.mp4'

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

            step=f'Generate Video {item["day"]}',

            status="SUCCESS",

            decision="Generate one complete video.",

            action=(
                "Generated the images, "
                "voiceover and mp4 video."
            ),

            observation=(
                f'Video {item["day"]} '
                "generated successfully "
                "with voiceover narration."
            ),

        )

        return output_path

    except Exception as error:

        raise RuntimeError(

            f'Failed to generate Video {item["day"]}.'

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

    for item in plan:

        if item["type"] == "Post":

            generate_post(
                business_name,
                item,
            )

    # ------------------------------------
    # Video Generation
    # ------------------------------------

    # ------------------------------------
    # Generate Videos
    # ------------------------------------
    
    for item in plan:
    
        if item["type"] == "Video":
        
            generate_video(
            
                business_name,
                item,
    
            )
    
    
    return business_name