# Ekstraklasa Striker Benchmark

A scouting project I built to practice data analysis on football data. The idea was simple — take Ekstraklasa striker stats, clean them up in Python, and visualize the results in Tableau.

The main question I wanted to answer: **does Lech Poznań actually play worse without Ishak, or is it just a feeling?**

![Dashboard](dashboard.webp)

## What I found


| Metric | With Ishak | Without Ishak |
|--------|-----------|---------------|
| Avg. Goals Scored | 1.90 | 1.40 |
| Avg. Points per Game | 1.83 | 1.40 |
| Loss Rate | 13.8% | 40.0% |

Lech lose 3x more often without him in the starting lineup. The scatter plot puts this in context — Ishak sits in the top-right quadrant when benchmarked against every Ekstraklasa forward with 500+ minutes on G+A per 90 vs Shot Conversion Rate.

## How it works

`ekstraklasa_scraper.py` — loads two Excel exports from FBref (standard stats + shooting stats), merges them, filters for forwards with 500+ minutes and calculates G+A per 90 and shot conversion rate.

`ishak_impact.py` — loads Ishak's match log and Lech's fixture list, merges them by date, and splits results into "with Ishak" vs "without Ishak".

Both scripts output CSV files which I then loaded into Tableau to build the dashboard.

## Data

Raw data exported manually from [FBref](https://fbref.com) — Ekstraklasa 2025/26 season.

## Tools

Python (Pandas), Tableau
