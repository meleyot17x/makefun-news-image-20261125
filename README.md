# THE BEACON POST — Tuesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/meleyot17x/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/meleyot17x/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Bounty: https://make.fun/bounty/news-image-20261125

One front page that sums up a single day's news: **Tuesday 25 November
2026**. Thirty-seven dated stories across nine regions, drawn as an
original turmeric-and-brown-ink newspaper page at 1024×1024.

What is on the page:

- A lead trio of the day's heaviest stories — the Gaza drone strikes,
  Baghdad's order to seize the Kurdish oilfields, and the EU's new
  Russia sanctions — each with a full layered scene, a two-fact deck, a
  data chip and a source/certainty tag.
- Ten more full cards: NATO AWACS to Poland, the Iranian claim of three
  tankers mined in Hormuz (labelled as a claim), the 700,000 Russian
  war-dead analysis, Nvidia's Monday close, the PCE report due that day
  (no figure printed — it had not been published), Xiamen Airlines'
  50-jet Boeing order, Madrid 5–1 PSV, twelve revived coral species,
  Fiji's disaster declaration and the Thanksgiving storm threat.
- A number strip of eight figures tied to the cards, a colour-coded
  nine-region strip with honest counts, a six-slot timeline, a dotted
  world map with the thirteen full cards pinned by number, a DATE CHECK
  box naming five stories that are *not* that day's news, and 24 further
  numbered briefs (stories 14–37).

Every number comes from that day's reporting; claims are printed as
claims. All drawings are original, made for this page.

## Running

`main.py` uses only the Python standard library. It copies the embedded
`entry.png` to `/output/entry.png`, byte for byte, on every run.

## Building the page

`compose_a.py` and `compose_b.py` render the two candidate layouts from
`beacon_data.py` (the day's locked story pool), `beacon_draw.py`
(original flat scenes and the dotted map) and `beacon_sections.py`
(shared page furniture). The duel winner becomes `entry.png`.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=zc743eea&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
