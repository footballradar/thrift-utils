from decimal import Decimal

# Import this module and then run install_common passing in the
# constructor for BetType; this module will then contain short names
# for home, away, over and under bets from 0 to 4 goals.


def install_common(betTypeFactory):
    for i in range(0, 17):
        decimal_goals = Decimal(i) / Decimal(4)
        short_name = str(decimal_goals).replace('.', '')

        def set_global_bet_type(
                varName,
                betTypeName,
                totalGoals=None,
                team1Hcp=None):
            globals()[varName.format(short_name)] = betTypeFactory(
                name=betTypeName,
                team1Hcp=team1Hcp,
                totalGoals=totalGoals,
                back=True
            )


        set_global_bet_type(
            'over_{}',
            'HcpOverBT',
            totalGoals=float(decimal_goals)
        )

        set_global_bet_type(
            'under_{}',
            'HcpUnderBT',
            totalGoals=float(decimal_goals)
        )

        set_global_bet_type(
            'ah1_{}',
            'HcpTeam1BT',
            team1Hcp=float(decimal_goals)
        )

        set_global_bet_type(
            'ah1_m{}',
            'HcpTeam1BT',
            team1Hcp=-float(decimal_goals)
        )

        set_global_bet_type(
            'ah2_{}',
            'HcpTeam2BT',
            team1Hcp=float(decimal_goals)
        )

        set_global_bet_type(
            'ah2_m{}',
            'HcpTeam2BT',
            team1Hcp=-float(decimal_goals)
        )
