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

