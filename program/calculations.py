

class Calculation:
    
    def games_tag_score(games_genres: dict[str, list],
                        time_played: dict[str, float]
                        ) -> tuple[dict[str, float], float]:
        
        total_tag_score: dict[str, float] = {}
        total_score: float = 0

        for game, genres in games_genres.items():
            for tag in genres:
                total_tag_score[tag] = round(total_tag_score.get(tag, 0) + time_played[game], 1)
                total_score += time_played[game]

        return total_tag_score, total_score


    def recommendation_rating(games_score: dict[str, float],
                              total_score: float, 
                              target_tags: dict[str, list[str]],
                              ) -> float:
        
        target_tags_score: dict[str, float] = {}
        final_rating: float = 0.0
        target_id: str = next(iter(target_tags))

        for tag in target_tags[target_id]:
            if tag in games_score:
                target_tags_score[tag] = target_tags_score.get(tag, 0) + games_score[tag]

        for score in target_tags_score.values():
            final_rating += score

        final_rating /= total_score

        return final_rating




