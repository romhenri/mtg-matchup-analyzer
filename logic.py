import pandas as pd
import re
import json
from collections import defaultdict

def get_insights(csv_file):
    df = pd.read_csv(csv_file)
    places = ['1st Place', '2nd Place', '3rd Place', '4th Place']
    
    matchups_freq = defaultdict(int)
    wins = defaultdict(lambda: defaultdict(int))
    losses = defaultdict(lambda: defaultdict(int))
    deck_usage = defaultdict(int)
    
    valid_decks = set()

    for _, row in df.iterrows():
        match_decks = []
        for place in places:
            if place not in df.columns:
                continue
            
            raw_name = row[place]
            if pd.isna(raw_name):
                continue
                
            name = str(raw_name).strip()
            name = re.sub(r'\(.*?\)', '', name).strip()
            
            if not name or name in ['-', '>-']:
                continue
            if name.startswith('*') or name.startswith('>'):
                continue
                
            clean_name = name.replace('[', '').replace(']', '').strip()
            if not clean_name:
                continue
                
            valid_decks.add(clean_name)
            match_decks.append(clean_name)
        
        if len(match_decks) == 2:
            d1 = match_decks[0]
            d2 = match_decks[1]
            
            pair = tuple(sorted([d1, d2]))
            matchups_freq[pair] += 1
            
            wins[d1][d2] += 1
            losses[d2][d1] += 1
            
            deck_usage[d1] += 1
            deck_usage[d2] += 1

    common = sorted(
        [{"deck1": k[0], "deck2": k[1], "count": v} for k, v in matchups_freq.items()],
        key=lambda x: x['count'],
        reverse=True
    )
    
    unique_never = []
    decks_list = list(valid_decks)
    for i in range(len(decks_list)):
        for j in range(i + 1, len(decks_list)):
            d1, d2 = decks_list[i], decks_list[j]
            pair = tuple(sorted([d1, d2]))
            if pair not in matchups_freq:
                unique_never.append({"deck1": d1, "deck2": d2})
                    
    invincible = []
    for u in valid_decks:
        for opp in wins[u]:
            if losses[u][opp] == 0:
                invincible.append({"user_deck": u, "opponent_deck": opp, "wins": wins[u][opp]})
                
    invincible = sorted(invincible, key=lambda x: x['wins'], reverse=True)
    
    most_used = sorted(
        [{"deck": k, "usage": v} for k, v in deck_usage.items()],
        key=lambda x: x['usage'],
        reverse=True
    )
                
    return json.dumps({
        "most_common_matchups": common,
        "never_happened": unique_never,
        "invincibility": invincible,
        "most_used_decks": most_used
    })