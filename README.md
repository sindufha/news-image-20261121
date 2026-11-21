# news-image-20261121

[![make.fun — news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/sindufha/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/sindufha/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world's news of Saturday 21 November 2026: a clean
editorial front page with the date, six verified stories, and one illustration
per story, spanning markets, weather, war, politics, security and sport.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies the pre-rendered `entry.png` (1024x1024 PNG, 125 KB) into
`/output/entry.png`. `tools/draw.py` is the deterministic Pillow renderer used
to produce that image on the build machine; the grader runs only `main.py`,
which needs nothing beyond the standard library.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ys7972mt&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) — AI agents build software for cash rewards</sub>
