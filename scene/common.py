from manim import *  # noqa: F403
from manim_slides import Slide


class BaseSlide(Slide):
    # the web deck only plays forward, and reversing long clips can hang Manim Slides
    skip_reversing = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # render the final frame of each slide, so a paused slide never shows an unfinished animation
        self.wait_time_between_slides = 0.1


def chapter(scene, text):
    """Small chapter label in the top-right corner, like the 1's Complement slides."""
    label = Tex(text).scale(0.75).to_edge(UR).set_color_by_gradient(WHITE, GRAY)
    scene.add(label)
    return label


def digit_row(count, symbol, base="2", font_size=40, side=1.0, dots_after=None):
    """( [s] [s] ... [s] )_base as a row of boxes. dots_after inserts a cdots after that many boxes."""
    cells = [Square(side).add(MathTex(symbol, font_size=font_size)) for _ in range(count)]
    if dots_after is not None:
        cells.insert(dots_after, MathTex(r"\cdots"))
    return VGroup(MathTex("("), *cells, MathTex(rf")_{{{base}}}")).arrange(RIGHT)


def gather(sources, target, indices):
    """Move each source into target[index] and fade in the rest of target."""
    moves = [ReplacementTransform(src, target[i]) for src, i in zip(sources, indices)]
    rest = VGroup(*[part for j, part in enumerate(target) if j not in indices])
    return AnimationGroup(*moves, FadeIn(rest))
