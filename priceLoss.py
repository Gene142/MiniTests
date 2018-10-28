from unittest import TestCase


def price_loss_calculation(prices):
    highest_loss = 0
    if len(prices) < 2:
        return highest_loss
    for x in range(1, len(prices)):
        loss = abs(prices[x] - prices[x-1])
        if loss > highest_loss:
            highest_loss = loss
    return highest_loss


class TestPriceLossCalculation (TestCase):
    def test_price_loss_calculation(self):
        normaldata = [45, 50, 55, 70, 25, 45]
        x = price_loss_calculation(normaldata)
        self.assertEqual(x, 45)
        onedata = [4] # same as no data in list
        t = price_loss_calculation(onedata)
        self.assertEqual(t, 0)
        negdata = [1, 5, 20, 45, -50, 73, 82]
        p = price_loss_calculation(negdata)
        self.assertEqual(p, 123)


TestPriceLossCalculation("test_price_loss_calculation")

