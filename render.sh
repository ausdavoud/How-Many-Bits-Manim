#!/usr/bin/env bash
# Renders every scene with Manim Slides, then builds the reveal.js deck.
#
#   ./render.sh                    # -> slides.html (+ slides_assets/)
#   ./render.sh site/slides.html   # what the GitHub Pages build uses
#
# Extra Manim flags can go in MANIM_FLAGS, e.g. MANIM_FLAGS=-ql for a quick low-quality pass.
set -euo pipefail
cd "$(dirname "$0")"

out="${1:-slides.html}"

scenes=(
  001_question:Question
  002_first_guess:FirstGuess
  003_where_it_fails:WhereItFails
  004_largest_number:LargestNumber
  005_any_base:AnyBase
  006_formula:Formula
  007_bonus:Bonus
  008_answers:Answers
)

classes=()
for entry in "${scenes[@]}"; do
  file="${entry%%:*}"
  cls="${entry##*:}"
  # shellcheck disable=SC2086
  manim-slides render ${MANIM_FLAGS:-} "scene/$file.py" "$cls"
  classes+=("$cls")
done

mkdir -p "$(dirname "$out")"
manim-slides convert "${classes[@]}" "$out" \
  -c "title=How many bits?" -ccontrols=true -cprogress=true -chash=true
