# MTG Matchup Analyzer

![GitHub repo size](https://img.shields.io/github/repo-size/romhenri/mtg-matchup-analyzer?style=for-the-badge)

> Web app that analyzes Magic: The Gathering match data from CSV files. Upload tournament results and get insights: most common matchups, matchups that never occurred, win rates per deck, invincibility (decks that never lost to certain opponents), and most used decks. Export results as JSON.

### How to run

```bash
pip install streamlit pandas matplotlib
streamlit run app.py
```

### Schema

Example CSV with required columns:

```csv
1st Place,2nd Place,3rd Place,4th Place
Mono Red Aggro,Azorius Control,,,
Golgari Midrange,Mono Red Aggro,,,
Azorius Control,Golgari Midrange,,,
```

| 1st Place         | 2nd Place         | 3rd Place | 4th Place |
|-------------------|-------------------|----------|-----------|
| Mono Red Aggro    | Azorius Control   |          |           |
| Golgari Midrange | Mono Red Aggro    |          |           |
| Azorius Control   | Golgari Midrange  |          |           |

<hr>

### Languages and Technologies

<div display="inline_block">
<a href="https://www.python.org/" target="_blank"><img align="center" alt="Python" height="54" width="54" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></a>
<a href="https://streamlit.io/" target="_blank"><img align="center" alt="Streamlit" height="54" width="54" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg"></a>
<a href="https://pandas.pydata.org/" target="_blank"><img align="center" alt="Pandas" height="54" width="54" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"></a>
<a href="https://matplotlib.org/" target="_blank"><img align="center" alt="Matplotlib" height="54" width="54" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg"></a>
</div>

<hr>

### Authorship

<table>
  <tr>
    <td width="40%" align="center">
      <a href="https://github.com/romhenri">
        <img src="https://avatars.githubusercontent.com/u/123867521?v=4" width="200px" alt="Romulo Henri's photo on GitHub"/><br>
        <p>
          <b>Rômulo Henri</b>
        </p>
      </a>
    </td>
    <td width="75%" align="center">

        <sub>Started: February 2026</sub>
    </td>
  </tr>
</table>
