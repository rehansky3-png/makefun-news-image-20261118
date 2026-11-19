# THE WORLD — Wednesday 18 November 2026

A one-image summary of the world's news on 18 November 2026, laid out as a
broadsheet front page. 46 stories from six continents, drawn as a single
1024×1024 picture (`entry.png`).

## What is on the page

- **Lead story — war in the Gulf:** the U.S.–Iran war widens across the
  Gulf, with strikes on both sides and shipping through Hormuz disrupted.
- **Where it happened:** a schematic world map with 12 numbered dots
  marking the main stories.
- **The day in figures:** 5 tankers sunk, a 56–44 Senate, Nvidia's
  $115.8bn quarter, gold at $3,724.91, 11,000+ Ebola cases, and 144
  disputed items in the COP31 draft.
- **Three illustrated panels:** the Kerch Bridge arch down, a tanker
  ablaze in the Strait of Hormuz, and the Shenzhen summit flags ahead of
  Thursday's trilateral meeting.
- **Three columns of briefs** covering the Gulf and Middle East, Europe,
  Asia-Pacific, the Americas, tech and markets, and Africa — plus a short
  "ALSO" line at the foot of the page.

## How to run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program is stdlib-only (`os`, `shutil`, `sys`). It checks that
`entry.png` sits next to it and is no larger than 1,048,576 bytes, creates
the output directory when needed, and copies the picture to
`$MAKEFUN_OUTPUT_DIR/entry.png`. It draws nothing — the artwork is
pre-made and ships as `entry.png`.

## Determinism

The output is a byte-for-byte copy of `entry.png`, so repeated runs
produce identical files: same size, same SHA-256.

## License

MIT — see `LICENSE`.

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rehansky3-png/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rehansky3-png/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
