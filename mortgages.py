
class Mortgage:
    def __init__(self, principal, term, yearly_nominal_rate):
        self._principal = principal
        self._term = term
        self._rate = yearly_nominal_rate

    def monthly_payment(self):
        rate = 1 + self._rate / 12
        return (self._principal * (rate) ** (self._term * 12)) / ((1 - rate ** (self._term * 12)) / (1 - rate))

    def calculate_simple(self):
        mp = self.monthly_payment()
        rate = 1 + self._rate / 12
        curr_principal = [self._principal]
        curr_interest = [0]
        cum_interest = [0]
        principal_decrease = [0]
        total_principal_paid = [0]
        total_amt_paid = [0]
        dates = ['Year: 1, Month: 0']

        # Loop through and calculate
        for y in range(self._term):
            for m in range(12):
                payment = mp # TODO: Work in a case where we overpay
                new_interest = curr_principal[-1] * (rate - 1)
                new_principal = curr_principal[-1] * (rate) - mp
                date = f'Year: {y + 1}, Month: {m + 1}'

                # updates
                curr_principal.append(new_principal)
                curr_interest.append(new_interest)
                cum_interest.append(cum_interest[-1] + new_interest)
                principal_decrease.append(curr_principal[-2] - curr_principal[-1])
                total_principal_paid.append(total_principal_paid[-1] + principal_decrease[-1])
                total_amt_paid.append(total_amt_paid[-1] + mp)
                dates.append(date)
        
        return {'Date':dates, 'Principal':curr_principal, 'Interest':curr_interest, 
                'Cumulative Interest':cum_interest, 'Cumulative Principal Paid':total_principal_paid, 
                'Principal Decrease':principal_decrease, 'Total Amount Paid':total_amt_paid}


if __name__ == '__main__':
    import pandas as pd
    mortgage = Mortgage(400000, 30, .072)
    calc = mortgage.calculate_simple()
    pd.DataFrame(calc).to_clipboard(index=False)
