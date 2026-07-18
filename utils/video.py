import random

from moviepy import (
    ImageClip,
    AudioFileClip,
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
    audio_path,
    output_path,
):
    """
    Creates an mp4 video using the
    provided images and audio.
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
        # Add Audio
        # ------------------------------

        if (
            audio_path is not None
            and audio_path.exists()
        ):

            audio = AudioFileClip(

                str(audio_path),

            )

            print(
                f"\nVideo Duration : {video.duration}"
            )

            print(
                f"Audio Duration : {audio.duration}"
            )

            video = video.with_audio(

                audio,

            )

            print(
                f"Audio Added : {video.audio}\n"
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

        return output_path


    except Exception as error:

        raise RuntimeError(
            "Failed to generate the video."
        ) from error