from decimal import *

# Import this module and then run install_common passing in the
# constructor for BetType; this module will then contain short names
# for home, away, over and under bets from 0 to 4 goals.


def install_common(betTypeFactory):
    for i in range(0, 17):
        decimal_goals = Decimal(i) / Decimal(4)
        short_name = str(decimal_goals).replace('.', '')
        globals()['over_{}'.format(short_name)] = betTypeFactory(
            name='HcpOverBT',
            totalGoals=float(decimal_goals),
            back=True
        )

        globals()['under_{}'.format(short_name)] = betTypeFactory(
            name='HcpUnderBT',
            totalGoals=float(decimal_goals),
            back=True
        )

        globals()['ah1_{}'.format(short_name)] = betTypeFactory(
            name='HcpTeam1BT',
            team1Hcp=float(decimal_goals),
            back=True
        )

        globals()['ah1_m{}'.format(short_name)] = betTypeFactory(
            name='HcpTeam1BT',
            team1Hcp=-float(decimal_goals),
            back=True
        )

        globals()['ah2_{}'.format(short_name)] = betTypeFactory(
            name='HcpTeam2BT',
            team1Hcp=float(decimal_goals),
            back=True
        )

        globals()['ah2_m{}'.format(short_name)] = betTypeFactory(
            name='HcpTeam2BT',
            team1Hcp=float(decimal_goals),
            back=True
        )
