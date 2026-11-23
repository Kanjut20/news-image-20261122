# Sum up 22 November's world news in one image

- Bounty: https://make.fun/bounty/news-image-20261122
- Reward: $100 total, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20)
- Deadline: Tue, 24 Nov 2026, 00:00 UTC = 07:00 WIB
- Entry: `main.py` (Python 3.13) copies the bundled `entry.png` to `/output/entry.png`.
  No network, deterministic — both runs write the same bytes.
- Image: 1024×1024 PNG, under 1 MiB. Six stories + an "ALSO" footer.

## The six stories (22 Nov 2026)

1. COP31 in Antalya ends with no deal — nearly 200 nations fail to agree on fossil fuels / climate finance.
2. ICJ rules Myanmar committed genocide against the Rohingya.
3. Zelenskyy says Ukraine was behind the drone strike that sank a Russian warship in Benghazi, Libya.
4. Iran strikes tankers near the Strait of Hormuz; Bahrain says an attack hit a plant, injuring 2.
5. Israeli settlers torch homes and cars in West Bank villages; Israel's opposition calls it terrorism.
6. 34 workers missing after a candy-factory fire in Indonesia; rescue teams recover remains.

Footer: Kyiv-area strike kills 3; Nigeria boat capsizes, 24 dead; Mexico cartel leader captured.

## Sources (checked 23 Nov 2026 — each story below)

1. COP31, Antalya — collapsed Sunday 22 Nov 2026 with no deal; fossil-fuel language was the main obstacle, 190+ countries, longest COP on record.
   - UN News: https://news.un.org/en/story/2026/11/1168855
   - CNN: https://www.cnn.com/2026/11/22/climate/cop31-summit-collapses-in-fossil-fuel-failure?cid=external-feeds_iluminar_meta
2. ICJ, Myanmar/Rohingya — judgment delivered Thu 19 Nov 2026 (9–6): Myanmar committed genocide against the Rohingya in the 2016–2017 clearance operations; reparations ordered.
   - UN News: https://news.un.org/en/story/2026/11/1168836
   - Human Rights Watch: https://www.hrw.org/news/2026/11/19/world-court-finds-myanmar-committed-rohingya-genocide
3. Benghazi, Libya — attack early Sunday 22 Nov 2026 at Benghazi naval base; Zelenskyy confirmed on Mon 23 Nov that Ukrainian sea drones sank the Russian corvette Merkury, destroyed a Ka-27 helicopter, and hit the cargo ship MV Angara.
   - CNN (22 Nov): https://www.cnn.com/2026/11/22/africa/russian-vessel-libya-suspected-drone-attack-intl?cid=external-feeds_iluminar_meta
   - Reuters (23 Nov): https://www.reuters.com/world/europe/zelenskiy-says-ukraine-sank-russian-corvette-near-libyas-coast-hit-cargo-ship-2026-11-23/
4. Strait of Hormuz / Bahrain — two tankers hit Sat 21 Nov 2026 near the strait (UKMTO); Bahrain said Iran struck a civilian industrial facility the same day; on Sun 22 Nov Bahrain reported 2 people injured, one critically.
   - AFP: https://www.nampa.org/text/23072293
   - Corticorp (22 Nov round-up): https://news.corticorp.com/story/2026-11-22-iran-theater-na-1
5. West Bank — settlers torched cars and homes in Kafr Malik, Deir as-Sudan, Deir Abu Masha'al and At-Tuwani early Sunday 22 Nov 2026; opposition figure Gadi Eisenkot called it "Jewish terrorism".
   - Reuters: https://www.reuters.com/world/middle-east/israels-eisenkot-condemns-arson-attacks-by-jewish-settlers-west-bank-2026-11-22/
   - CNN: https://www.cnn.com/2026/11/22/middleeast/west-bank-attacks-eisenkot-intl?cid=external-feeds_iluminar_meta
6. Indonesia candy-factory fire — fire broke out Sat 21 Nov 2026 ~5pm at the PT Fonusa Agung Mulia factory in Cikande, Banten; on Sun 22 Nov rescuers recovered body bags and searched for dozens still missing (reported figures that day varied by source and time, roughly 29–50 missing).
   - Xinhua (22 Nov): https://www.nampa.org/text/23072379
   - Reuters (23 Nov, toll confirmed Monday): https://www.reuters.com/world/asia-pacific/indonesia-says-24-killed-factory-blaze-rescuers-search-dozens-missing-2026-11-23/

### Date notes — read before submitting

The image frames all six stories as 22 Nov news. Three of them need care:
- ICJ ruling: delivered Thu 19 Nov, not 22 Nov — it was still in the news on 22 Nov, but the judgment itself is 19 Nov.
- Benghazi: the attack itself was early Sun 22 Nov, but Zelenskyy's confirmation that Ukraine was behind it came Mon 23 Nov.
- Hormuz/Bahrain: the tanker strikes and the industrial-site attack were Sat 21 Nov; the "2 injured" update was reported Sun 22 Nov.
- Indonesia fire: the "34 missing" figure in the image could not be matched to any single 22 Nov report — that day's reported missing figures ranged roughly 29–50 by source and time. The fire itself (Sat 21 Nov evening) and the Sunday rescue search are confirmed.

These do not change the image file, which is left untouched here. If the entry is rebuilt, prefer stories whose key event actually happened on 22 Nov.

## Still needed to submit (not done — needs Abay)

- The public GitHub repo already exists: https://github.com/Kanjut20/news-image-20261122 (latest commit 4baa18a, "Add make.fun badges to README").
  It holds `main.py`, `entry.png`, `LICENSE`, `README.md` — but NOT `build_image.py` yet. That file exists locally in this folder and regenerates `entry.png` byte-identically (verified 23 Nov 2026), so upload it to the repo too if it should be part of the snapshot.
- A make.fun account + API key and a Solana wallet to receive USDC (see https://make.fun/skill.md).
- The AI coding-agent transcripts of the sessions that built it, uploaded with the submission.
- At most 10 submissions a day / 20 total; the last submission before the deadline is the final entry.
