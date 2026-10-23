import streamlit as st
from pathlib import Path

from pipeline import run_pipeline



st.title("Business Intel AI")

st.write(
    "AI Powered Marketing Intelligence Platform"
)

st.header("Upload Source Pack")


uploaded_file = st.file_uploader(
    "Choose a Markdown file",
    type=["md"],
)



if uploaded_file is not None:

    source_path = Path("source_files") / uploaded_file.name

    source_path.parent.mkdir(parents=True, exist_ok=True)

    with open(source_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.info(f"Selected File : {uploaded_file.name}")

    

    st.subheader("Content Generation Mode")

    generation_mode = st.radio(
        "Choose Content Generation Mode",
        ["Free", "Premium"],
        horizontal=True,
        ).lower()

    
    if st.button("RUN PIPELINE"):
        

        with st.spinner("Running BusinessIntelAI Pipeline..."):

            st.session_state["business_name"] = run_pipeline(
                source_file_path=source_path,
                generation_mode=generation_mode,
            )

        st.session_state["source_file_name"] = uploaded_file.name

        st.success("Pipeline executed successfully!")


    # Results are rendered outside the button block so they
    # survive the rerun triggered by clicking a download button.

    if st.session_state.get("source_file_name") == uploaded_file.name:

        base_path = Path("data") / st.session_state["business_name"]

        st.divider()

        st.subheader("Business Analysis")

        business_analysis_path = base_path / "analysis" /"business_analysis"/ "business_analysis.md"

        if business_analysis_path.exists():

            with open(business_analysis_path, "rb") as file:

                st.download_button(
                label="Download business_analysis.md",
                data=file,
                file_name="business_analysis.md",
            )

        else:

            st.warning(
            "business_analysis.md was not generated."
            )

        st.divider()

        st.subheader("Market Analysis")

        market_analysis_path = base_path / "analysis" /"market_analysis"/ "market_analysis.md"

        if market_analysis_path.exists():

            with open(market_analysis_path, "rb") as file:

                st.download_button(
                label="Download market_analysis.md",
                data=file,
                file_name="market_analysis.md",
            )

        else:

            st.warning(
            "market_analysis.md was not generated."
            )

        st.divider()

        st.subheader("Content Strategy")

        strategy_path = base_path / "strategy" / "strategy.json"

        if strategy_path.exists():

            with open(strategy_path, "rb") as file:

                st.download_button(
                label="Download strategy.json",
                data=file,
                file_name="strategy.json",
            )

        else:

            st.warning(
            "strategy.json was not generated."
            )

        st.divider()

        st.subheader("7-Day Content Plan")

        plan_path = base_path / "plan" / "plan.json"

        if plan_path.exists():

            with open(plan_path, "rb") as file:

                st.download_button(
                label="Download plan.json",
                data=file,
                file_name="plan.json",
            )

        else:

            st.warning(
            "plan.json was not generated."
        )

        st.divider()

        st.subheader("Generated Posts")

        posts_path = base_path / "content" / "posts"

        if posts_path.exists():

            for post in posts_path.glob("*.png"):

                st.image(str(post))

                with open(post, "rb") as file:

                    st.download_button(
                    label="Download",
                    data=file,
                    file_name=post.name,
                )

        else:

            st.warning(
            "No posts were generated."
        )

        st.divider()

        st.subheader("Generated Videos")

        videos_path = base_path / "content" / "videos"

        if videos_path.exists():

            for video_folder in videos_path.iterdir():

                video_path = video_folder / f"{video_folder.name}.mp4"

                if video_path.exists():

                    st.video(str(video_path))

                    with open(video_path, "rb") as file:

                        st.download_button(
                        label="Download",
                        data=file,
                        file_name=video_path.name,
                    )

                    st.divider()

        else:

            st.warning(
            "No videos were generated."
            )
        st.divider()  

        st.subheader("Reviewer Output")

        review_path = base_path / "reviews" / "review.json"

        if review_path.exists():

            with open(review_path, "rb") as file:

                st.download_button(
                label="Download review.json",
                data=file,
                file_name="review.json",
            )

        else:

            st.warning(
            "review.json was not generated."
        )