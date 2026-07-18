# BusinessIntelAI

BusinessIntelAI is an autonomous multi-agent AI system that generates a complete first-week marketing content package for a business. The system performs business-context analysis, creates a content strategy, generates a seven-day content plan, produces social media assets, and reviews the generated outputs before human approval.

## Pipeline

```
                Source Pack
                     ↓
              Consultant Agent
                     ↓
                analysis.md
                     ↓
               strategy.json
                     ↓
                Creator Agent
                     ↓
                  plan.json
                     ↓
            5 Posts + 2 Videos
                     ↓
                Reviewer Agent
                     ↓
                 review.json
```

The complete workflow can be executed using:

```bash
python pipeline.py
```

## Architecture

- **Consultant Agent** – Performs business-context analysis and generates the first-week content strategy.
- **Creator Agent** – Generates the seven-day content plan and creates the required content assets.
- **Reviewer Agent** – Reviews the generated outputs for business and strategy alignment before human approval.

The modular architecture allows each agent to operate independently while collaborating as part of the complete workflow.

## Technologies Used

- Python
- Google Gemini API
- Pollinations AI
- Piper TTS
- MoviePy

Pollinations AI was used for image generation, Piper TTS for voiceover generation and MoviePy for generating short-form cinematic videos from the generated assets. These technologies were selected to provide an autonomous and cost-efficient end-to-end content generation pipeline.

Commercial alternatives such as premium image generation APIs, text-to-speech services and video generation models can be integrated in future versions with minimal architectural changes.

## Generated Outputs

The system automatically generates:

- Business Analysis (`analysis.md`)
- First-Week Content Strategy (`strategy.json`)
- Seven-Day Content Plan (`plan.json`)
- Five Post Creatives
- Two Short-Form Videos
- Reviewer Outputs (`review.json`)
- Execution Traces (`execution_trace.json`)
- Spend Logs (`spend_log.json`)

## Future Improvements

Future versions may include:

- Interactive user interfaces.
- Extended prompt modularization across all agents.
- Additional reviewer capabilities.
- Alternative content generation workflows.
- Support for additional content formats and generation services.

---

### Author

**Huzefa Arab**

MIT World Peace University  
ECE (Artificial Intelligence & Machine Learning)