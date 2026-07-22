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
Create the first-week content strategy for the business based on the provided business analysis.

CONSTRAINTS:
1. Define the week's primary marketing objective.
2. Identify the target audience for this week's content.
3. Define three to five content pillars for the week.
4. Identify the key marketing messages that should be communicated.
5. Define the appropriate tone of communication.
6. Suggest suitable calls-to-action for the week's content.
7. Recommend an appropriate mix of content formats for the week.
8. Clearly explain the reasoning behind the proposed strategy.
9. Ensure all strategic choices are specific to the business.
10. Do not hallucinate information. Make reasonable assumptions whenever necessary and clearly state them.

OUTPUT FORMAT:
Return ONLY valid JSON in the following format.

{
    "week_objective":"",

    "target_audience":[],

    "content_pillars":[],

    "key_messages":[],

    "tone":[],

    "calls_to_action":[],

    "format_mix":[],

    "strategy_reasoning":""
}


IMPORTANT:
1. Return ONLY valid JSON.
2. Never wrap the JSON inside ```json.
3. Do NOT return Markdown.
4. Do NOT add explanations outside the JSON.
5. Every field must always be present.
6. The strategy must be suitable ONLY for the first week's content plan.

INPUT:
"""
