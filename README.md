# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rehansky3-png/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rehansky3-png/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper front page summing up the world's news of Wednesday 18 November 2026 in one 1024×1024 image: the U.S.–Iran war widening across the Gulf (Qeshm strike, Iran hitting U.S. bases in Kuwait and Bahrain, five tankers sunk, Hormuz shipping disrupted), the Kerch Bridge road arch collapsing, Xi and Putin meeting in Shenzhen ahead of Thursday's trilateral with Trump, Peltola taking Alaska for a 56–44 Democratic Senate, OpenAI launching GPT-6.2 Astra and Sol, Nvidia's $115.8bn quarter, gold falling to a 14-month low, and the Ebola outbreak passing 11,000 cases — 46 stories in all, with a world map, three illustrated panels and a day-in-figures strip.

The image was drawn with Pillow during development and is stored as `entry.png`; `main.py` (Python 3.13, stdlib only, no network) just copies it to the output directory, so both runs write identical bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, < 1 MiB)
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d7yn48z6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
