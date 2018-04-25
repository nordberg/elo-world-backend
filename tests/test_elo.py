from routes.elo import calculate_new_elo, MatchResult

def test_calculate_new_elo_gives_correct_elo():
    new_elo_1, new_elo_2 = calculate_new_elo(1000, 1000, MatchResult.WIN)
    assert new_elo_1 == 123
    assert new_elo_2 == 123
