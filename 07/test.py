from calculate_share import percent_share

def testing_percent_share():
    assert percent_share(120, 30.0) == 25
    return "testing_percent_share() passed successfully"

print testing_percent_share()