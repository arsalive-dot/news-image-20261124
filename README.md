[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/arsalive-dot/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/arsalive-dot/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# The World in One Day — Tuesday 24 November 2026

A dense colour infographic atlas summing up one day of world news in a
single 1024×1024 image: 46 stories in all.

The three biggest stories of the day lead the page. In Riyadh, a Houthi
drone hit the 80-storey PIF Tower — the tallest tower in the city — for
the second time in five days; 11 people were hurt, two critically, and
the Saudi coalition blamed the Houthis, who announced no fresh attack.
On Wall Street, Nvidia's comeback rally faded in a day: the stock fell
5.86% to $155.38 after Monday's 31.5% surge, the Nasdaq dropped 1.48%
while the Dow rose 423 points to top 50,000 for the first time. And in
Gaza City, Israel killed Hamas security chief Naim Abu Nahal, 50, in a
drone strike; seven people were killed on Tuesday despite the ceasefire.

Below the leads: a UTC timeline of the day, 10 illustrated stories (a
Zaporizhzhia flat-block strike, Asian stocks leaping, a record landmine
toll, ~175 migrants missing off Senegal, the Iranian rial plunging, UK
sanctions on the Houthis, Real Madrid's 5–1 win over PSV, the Medal of
Freedom for Rudy Giuliani, US consumer confidence jumping, and a tanker
hit in the Strait of Hormuz), a world map with 16 numbered pins, a
figures strip with the day's verified numbers, and a numbered list of 33
more stories. Claims that could not be independently confirmed are
marked CLAIM. Tuesday was a trading day, so all market figures are
Tuesday 24 November closes, labelled as such. Every figure, location
and meeting was checked against the sources listed in the image
(Reuters, AP, AFP, Al Jazeera, BBC, CNN, and others).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies the bundled `entry.png` to `out/entry.png`. Stdlib only, no
network access, deterministic output — running it three times in a row
produces byte-identical files. The program checks the bundled file is a
real PNG and that the copy landed whole before it reports success.
