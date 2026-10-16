"""Assembles the GitHub Pages site after ./render.sh site/slides.html has run.

Adds the landing page, a still from every scene (used for link previews and the README),
and the whole presentation as a single video.
"""

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
PREVIEWS = SITE / "previews"

# scene classes, in render.sh order
SCENES = [
    "Question", "FirstGuess", "WhereItFails", "LargestNumber",
    "AnyBase", "Formula", "Bonus", "Answers",
]


def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def duration(video):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def scene_video(cls):
    # Manim writes media/videos/<file>/<quality>/<Scene>.mp4, e.g. 480p15 or 1080p60;
    # take the highest resolution, in case a quick low-quality pass is lying around
    matches = sorted(ROOT.glob(f"media/videos/*/*/{cls}.mp4"), key=lambda p: int(p.parent.name.split("p")[0]))
    if not matches:
        raise SystemExit(f"no rendered video for {cls}")
    return matches[-1]


def main():
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    videos = [scene_video(cls) for cls in SCENES]

    for cls, video in zip(SCENES, videos):
        # a still from about two thirds in: most scenes fade out at the very end
        ffmpeg("-ss", f"{duration(video) * 0.66:.2f}", "-i", str(video), "-frames:v", "1",
               "-vf", "scale=1280:-2", "-q:v", "3", str(PREVIEWS / f"{cls}.jpg"))

    # the whole presentation as one video, re-encoded: flat vector animation compresses
    # to well under half the size of Manim's output without visible loss
    concat = SITE / "concat.txt"
    joined = SITE / "joined.mp4"
    concat.write_text("".join(f"file '{v}'\n" for v in videos))
    ffmpeg("-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(joined))
    ffmpeg("-i", str(joined), "-vf", "fps=30", "-c:v", "libx264", "-crf", "26", "-preset", "slow",
           "-tune", "animation", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
           str(SITE / "how-many-bits.mp4"))
    concat.unlink()
    joined.unlink()

    shutil.copy(ROOT / "web" / "index.html", SITE / "index.html")
    (SITE / ".nojekyll").touch()
    print(f"site ready: {len(SCENES)} scenes")


if __name__ == "__main__":
    main()
