import random

from moviepy import (
    ImageClip,
    AudioFileClip,
    VideoFileClip,
    concatenate_videoclips,
)


# ------------------------------------
# Video Configuration
# ------------------------------------

IMAGE_DURATION = 3

FPS = 24

TRANSITION_DURATION = 0.5

ZOOM_FACTOR = 1.10


EFFECTS = [

    "zoom_in",
    "zoom_out",

]


# ------------------------------------
# Apply Effects
# ------------------------------------

def apply_random_effect(
    clip,
    effect,
):
    """
    Applies the provided effect
    to an image clip.
    """

    if effect == "zoom_in":

        clip = clip.resized(
            lambda t:
            1 + (
                (ZOOM_FACTOR - 1)
                * (t / IMAGE_DURATION)
            )
        )

    elif effect == "zoom_out":

        clip = clip.resized(
            lambda t:
            ZOOM_FACTOR - (
                (ZOOM_FACTOR - 1)
                * (t / IMAGE_DURATION)
            )
        )

    return clip


# ------------------------------------
# Create Video
# ------------------------------------

def create_video(
    image_paths,
    output_path,
):
    """
    Creates an audio-less mp4 video
    using the provided images.
    """

    try:

        clips = []

        # ------------------------------
        # Create Image Clips
        # ------------------------------

        for image_path in image_paths:

            clip = (

                ImageClip(
                    str(image_path),
                )
                .with_duration(
                    IMAGE_DURATION,
                )

            )

            effect = random.choice(
                EFFECTS,
            )

            clip = apply_random_effect(
                clip,
                effect,
            )

            clips.append(
                clip,
            )

        # ------------------------------
        # Merge Image Clips
        # ------------------------------

        video = concatenate_videoclips(

            clips,

            method="compose",

        )

        # ------------------------------
        # Save Video
        # ------------------------------

        output_path.parent.mkdir(

            parents=True,
            exist_ok=True,

        )

        video.write_videofile(

            str(output_path),

            fps=FPS,

            codec="libx264",

            audio_codec="aac",

        )

        # ------------------------------
        # Close Resources
        # ------------------------------

        video.close()

        for clip in clips:

            clip.close()

        return output_path

    except Exception as error:

        raise RuntimeError(
            "Failed to generate the video."
        ) from error


# ------------------------------------
# Add Voiceover
# ------------------------------------

def add_voiceover(
    video_path,
    voiceover_path,
):
    """
    Adds the generated voiceover to the
    provided mp4 video safely.
    """

    try:

        # ------------------------------
        # Temporary Output Path
        # ------------------------------

        temp_path = (

            video_path.parent
            / f"{video_path.stem}_temp.mp4"

        )

        # ------------------------------
        # Load Video
        # ------------------------------

        video = VideoFileClip(
            str(video_path),
        )

        # ------------------------------
        # Load Voiceover
        # ------------------------------

        audio = AudioFileClip(
            str(voiceover_path),
        )

        # ------------------------------
        # Add Voiceover
        # ------------------------------

        final_video = video.with_audio(
            audio,
        )

        # ------------------------------
        # Write Temporary Video
        # ------------------------------

        final_video.write_videofile(

            str(temp_path),

            fps=FPS,

            codec="libx264",

            audio_codec="aac",

        )

        # ------------------------------
        # Close Resources
        # ------------------------------

        final_video.close()

        audio.close()

        video.close()

        # ------------------------------
        # Replace Original Video
        # ------------------------------

        temp_path.replace(
            video_path,
        )

        return video_path

    except Exception as error:

        raise RuntimeError(
            "Failed to add the voiceover to the video."
        ) from error