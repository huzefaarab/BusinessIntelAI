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
9. Clearly specify the content type for every day. The "type" field must be exactly "Post" or "Video".
10. Ensure all strategic choices are specific to the business.
11. Do not hallucinate information. Make reasonable assumptions whenever necessary and clearly state them.

OUTPUT FORMAT:

Return ONLY valid JSON in the following format.


[
    {
        "day":1,
        "type":"Post | Video",
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


IMAGE_VIDEO_PROMPT = """
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
5. Generate EXACTLY FIVE complete image generation prompts.
6. Each image prompt must describe ONE scene of the video.
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

1. Generate EXACTLY FIVE complete standalone image prompts.
2. Each prompt must describe ONE different scene of the story.
3. Together, the five prompts must tell ONE continuous visual story from beginning to end.
4. Every prompt must already include:
    - the visual style
    - the lighting
    - the environment
    - the camera style
    - the color palette
    - the business branding
5. Every prompt must be fully self-contained.
6. Do NOT generate one base prompt with variations.
7. Maintain visual consistency across all five prompts while ensuring each scene is visually different.
8. The fifth prompt should naturally conclude the story.
9. The five prompts should feel like five consecutive cinematic scenes from the same premium short-form video.
10. Every image prompt must introduce a significant visual change from the previous one.

Examples of progression include:
- different actions
- different moments in time
- different camera compositions
- different viewpoints
- different interactions
- different environments within the same business

Do NOT generate five prompts that only show the same subject with minor appearance changes.

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
    "image_prompts":[

        "",
        "",
        "",
        "",
        ""

    ],

    "video_duration":"",

    "voiceover_script":"",

    "audio_direction":"",

    "caption":"",

    "hashtags":"",

    "cta":""

}


IMPORTANT:

1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Generate content for ONLY ONE VIDEO.
5. Every field must always be present.
6. Generate EXACTLY FIVE complete image prompts.
7. Every image prompt must be self-contained and ready to be sent directly to an image generation model without any additional text.


INPUT:

"""

WAN_VIDEO_PROMPT = """
ROLE:

You are an expert Social Media Video Creator.


TASK:

Generate ONE complete short-form cinematic
video creative using the provided content plan
item.


CONSTRAINTS:

1. Generate content for ONLY ONE video.
2. Generate a suitable caption.
3. Generate suitable hashtags.
4. Generate a suitable call-to-action.
5. Generate ONE highly detailed Wan 2.5 video prompt.
6. Generate ONE suitable voiceover script.
7. Ensure that all generated outputs align with:
    - the topic
    - the hook
    - the caption direction
    - the visual direction
    - the insight
    - the CTA.
8. Never generate content unrelated to the
provided content plan item.


IMPORTANT:

The generated video will later be generated
using Wan 2.5 Text-to-Video.

The generated video specifications are:

- Duration : DURATION seconds.


Keep these specifications in mind while
generating:
- the video prompt.
- the pacing of the scenes.
- the voiceover script.


WAN VIDEO PROMPT REQUIREMENTS:

1. Generate ONE highly detailed and visually
descriptive Wan 2.5 video prompt.

2. The generated prompt should naturally
describe:
    - the beginning of the video.
    - the progression of the video.
    - the conclusion of the video.

3. Clearly describe:
    - lighting.
    - environment.
    - subjects.
    - camera movements.
    - visual aesthetics.
    - business branding.
    - mood and atmosphere.

4. The generated video prompt should be suitable
for premium short-form cinematic social media
video content such as Instagram Reels.

5. Prefer realistic and visually engaging scene
descriptions.

6. Avoid excessive scene changes that are
unsuitable for the provided video duration.

7. Generate ONE cohesive visual story that can
comfortably fit within the provided duration.

8. The generated prompt should read naturally as
ONE continuous and cohesive Wan 2.5 video prompt
and must NOT be written as multiple independent
scenes or image descriptions.


VOICEOVER REQUIREMENTS:

1. Generate ONE suitable voiceover script.

2. Ensure that the generated voiceover naturally
complements the generated video prompt.

3. Ensure that the generated voiceover can be
comfortably narrated within the provided video
duration.

4. Ensure that the generated voiceover naturally
complements the pacing and progression of the
generated video.

5. Prefer warm, engaging and natural sounding
narration unless otherwise required.

6. The generated voiceover should naturally
complement the beginning, progression and
conclusion of the generated video.


OUTPUT FORMAT:

Return ONLY valid JSON.


{
    "wan_video_prompt":"",

    "voiceover_script":""

    "audio_direction":"",

}


IMPORTANT:

1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Generate content for ONLY ONE VIDEO.
5. Every field must always be present.


INPUT:
"""