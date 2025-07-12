def score_players(jersey_dict):
    ranked = [{"player": k, "score": v} for k, v in jersey_dict.items()]
    ranked.sort(key=lambda x: -x["score"])
    return ranked