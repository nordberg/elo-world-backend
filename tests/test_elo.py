from routes.elo import calculate_new_elo, WIN, DRAW, LOSE

def test_calculate_new_elo_gives_correct_elo():
    assert 2403, 1997 == calculate_new_elo(2400, 2000, WIN)
    assert 2371, 2029 == calculate_new_elo(2400, 2000, LOSE)
