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
    st.divider()

    if st.button("RUN PIPELINE"):

        with st.spinner("Running BusinessIntelAI Pipeline..."):

            run_pipeline(source_path)
            

        st.success("Pipeline executed successfully!")

        st.divider()

        st.subheader("Business Analysis")

        analysis_path = Path("data") / uploaded_file.name.removesuffix(".md") / "analysis" / "analysis.md"

        if analysis_path.exists():

            with open(analysis_path, "rb") as file:

                st.download_button(
                label="Download analysis.md",
                data=file,
                file_name="analysis.md",
            )

        else:

            st.warning(
            "analysis.md was not generated."
            )

        st.divider()

        st.subheader("Content Strategy")

        strategy_path = Path("data") / uploaded_file.name.removesuffix(".md") / "strategy" / "strategy.json"

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

        plan_path = Path("data") / uploaded_file.name.removesuffix(".md") / "plan" / "plan.json"

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

        posts_path = Path("data") / uploaded_file.name.removesuffix(".md") / "content" / "posts"

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

        videos_path = Path("data") / uploaded_file.name.removesuffix(".md") / "content" / "videos"

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

        review_path = Path("data") / uploaded_file.name.removesuffix(".md") / "reviews" / "review.json"

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