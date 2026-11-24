# One image summing up 24 November 2026 world news

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/vmakeer/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/vmakeer/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun bounty
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124).

A program that draws a one-page newspaper front page — the day's world
news in a single 1024×1024 image — with Pillow and the Python standard
library only. No network access; two runs produce byte-identical output.

## The stories

- **Markets:** Nvidia's board reinstates Jensen Huang as CEO; shares jump
  31%, adding $952 billion in a day, and the Nasdaq climbs 6.5%.
- **Ukraine:** Russia re-strikes repaired power lines around Odesa;
  240,000 people are without heating and schools go remote.
- **Europe:** Moscow accuses NATO member Estonia of acts "on the verge of
  triggering open war" after a border closure; Tallinn denies the claim.
- **Asia:** South Korea's President Lee reshuffles his security team,
  naming Kang Kum-sil as the first woman to lead the NIS.
- **Travel:** A Delta weight-and-balance outage delays 2,100 flights
  ahead of Thanksgiving; 92 more are canceled on Monday.
- **Also:** the Indonesia factory fire toll rises to 24 dead, 30 missing;
  China sentences an official to death for leaking state secrets.

## Run

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # or any directory
```

`main.py` runs `draw.py`, which renders `entry.png` (1024×1024,
under 1 MiB).

## License

MIT — see LICENSE.
