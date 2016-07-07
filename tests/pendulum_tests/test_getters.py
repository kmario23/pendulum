# -*- coding: utf-8 -*-

import pytz
from pendulum import Pendulum

from .. import AbstractTestCase


class GettersTest(AbstractTestCase):

    def test_year(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(1234, d.year)

    def test_month(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(5, d.month)

    def test_day(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(6, d.day)

    def test_hour(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(7, d.hour)

    def test_minute(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(8, d.minute)

    def test_second(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(9, d.second)

    def test_microsecond(self):
        d = Pendulum(1234, 5, 6, 7, 8, 9)
        self.assertEqual(0, d.microsecond)

        d = Pendulum(1234, 5, 6, 7, 8, 9, 101112)
        self.assertEqual(101112, d.microsecond)

    def test_tzinfo(self):
        d = Pendulum.now()
        self.assertEqual(pytz.timezone('America/Toronto').zone, d.tzinfo.zone)

    def test_day_of_week(self):
        d = Pendulum(2012, 5, 7, 7, 8, 9)
        self.assertEqual(Pendulum.MONDAY, d.day_of_week)

    def test_day_of_year(self):
        d = Pendulum(2012, 5, 7)
        self.assertEqual(128, d.day_of_year)

    def test_days_in_month(self):
        d = Pendulum(2012, 5, 7)
        self.assertEqual(31, d.days_in_month)

    def test_timestamp(self):
        d = Pendulum(1970, 1, 1, 0, 0, 0)
        self.assertEqual(0, d.timestamp)
        self.assertEqual(60, d.add_minute().timestamp)

    def test_float_timestamp(self):
        d = Pendulum(1970, 1, 1, 0, 0, 0, 123456)
        self.assertEqual(0.123456, d.float_timestamp)

    def test_age(self):
        d = Pendulum.now()
        self.assertEqual(0, d.age)
        self.assertEqual(1, d.add_year().age)

    def test_local(self):
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'America/Toronto').local)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'America/New_York').local)
        self.assertFalse(Pendulum.create_from_date(2012, 1, 1, 'UTC').local)
        self.assertFalse(Pendulum.create_from_date(2012, 1, 1, 'Europe/London').local)

    def test_utc(self):
        self.assertFalse(Pendulum.create_from_date(2012, 1, 1, 'America/Toronto').utc)
        self.assertFalse(Pendulum.create_from_date(2012, 1, 1, 'Europe/Paris').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'Atlantic/Reykjavik').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'Europe/Lisbon').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'Africa/Casablanca').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'Africa/Dakar').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'UTC').utc)
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1, 'GMT').utc)

    def test_is_dst(self):
        self.assertFalse(Pendulum.create_from_date(2012, 1, 1, 'America/Toronto').is_dst)
        self.assertTrue(Pendulum.create_from_date(2012, 7, 1, 'America/Toronto').is_dst)

    def test_offset_with_dst(self):
        self.assertEqual(-18000, Pendulum.create_from_date(2012, 1, 1, 'America/Toronto').offset)

    def test_offset_no_dst(self):
        self.assertEqual(-14400, Pendulum.create_from_date(2012, 6, 1, 'America/Toronto').offset)

    def test_offset_for_gmt(self):
        self.assertEqual(0, Pendulum.create_from_date(2012, 6, 1, 'GMT').offset)

    def test_offset_hours_with_dst(self):
        self.assertEqual(-5, Pendulum.create_from_date(2012, 1, 1, 'America/Toronto').offset_hours)

    def test_offset_hours_no_dst(self):
        self.assertEqual(-4, Pendulum.create_from_date(2012, 6, 1, 'America/Toronto').offset_hours)

    def test_offset_hours_for_gmt(self):
        self.assertEqual(0, Pendulum.create_from_date(2012, 6, 1, 'GMT').offset_hours)

    def test_is_leap_year(self):
        self.assertTrue(Pendulum.create_from_date(2012, 1, 1).is_leap_year())
        self.assertFalse(Pendulum.create_from_date(2011, 1, 1).is_leap_year())

    def test_is_long_year(self):
        self.assertTrue(Pendulum.create_from_date(2015, 1, 1).is_long_year())
        self.assertFalse(Pendulum.create_from_date(2016, 1, 1).is_long_year())

    def test_week_of_month(self):
        self.assertEqual(5, Pendulum.create_from_date(2012, 9, 30).week_of_month)
        self.assertEqual(4, Pendulum.create_from_date(2012, 9, 28).week_of_month)
        self.assertEqual(3, Pendulum.create_from_date(2012, 9, 20).week_of_month)
        self.assertEqual(2, Pendulum.create_from_date(2012, 9, 8).week_of_month)
        self.assertEqual(1, Pendulum.create_from_date(2012, 9, 1).week_of_month)

    def test_week_of_year_first_week(self):
        self.assertEqual(52, Pendulum.create_from_date(2012, 1, 1).week_of_year)
        self.assertEqual(1, Pendulum.create_from_date(2012, 1, 2).week_of_year)

    def test_week_of_year_last_week(self):
        self.assertEqual(52, Pendulum.create_from_date(2012, 12, 30).week_of_year)
        self.assertEqual(1, Pendulum.create_from_date(2012, 12, 31).week_of_year)

    def test_timezone(self):
        d = Pendulum.create_from_date(2000, 1, 1, 'America/Toronto')
        self.assertEqual('America/Toronto', d.timezone.zone)

        d = Pendulum.create_from_date(2000, 1, 1, -5)
        self.assertEqual(None, d.timezone.zone)

    def test_tz(self):
        d = Pendulum.create_from_date(2000, 1, 1, 'America/Toronto')
        self.assertEqual('America/Toronto', d.tz.zone)

        d = Pendulum.create_from_date(2000, 1, 1, -5)
        self.assertEqual(None, d.tz.zone)

    def test_timezone_name(self):
        d = Pendulum.create_from_date(2000, 1, 1, 'America/Toronto')
        self.assertEqual('America/Toronto', d.timezone_name)

        d = Pendulum.create_from_date(2000, 1, 1, -5)
        self.assertEqual(None, d.timezone_name)

    def test_is_week_day(self):
        d = Pendulum.now().next(Pendulum.MONDAY)
        self.assertTrue(d.is_week_day())
        d = d.next(Pendulum.SATURDAY)
        self.assertFalse(d.is_week_day())

    def test_is_weekend(self):
        d = Pendulum.now().next(Pendulum.MONDAY)
        self.assertFalse(d.is_weekend())
        d = d.next(Pendulum.SATURDAY)
        self.assertTrue(d.is_weekend())

    def test_is_today(self):
        d = Pendulum.now()
        self.assertTrue(d.is_today())
        d = d.sub(days=1)
        self.assertFalse(d.is_today())

    def test_is_yesterday(self):
        d = Pendulum.now()
        self.assertFalse(d.is_yesterday())
        d = d.sub(days=1)
        self.assertTrue(d.is_yesterday())

    def test_is_tomorrow(self):
        d = Pendulum.now()
        self.assertFalse(d.is_tomorrow())
        d = d.add(days=1)
        self.assertTrue(d.is_tomorrow())

    def test_is_future(self):
        d = Pendulum.now()
        self.assertFalse(d.is_future())
        d = d.add(days=1)
        self.assertTrue(d.is_future())

    def test_is_past(self):
        with self.wrap_with_test_now():
            d = Pendulum.now()
            self.assertFalse(d.is_past())
            d = d.sub(days=1)
            self.assertTrue(d.is_past())

    def is_same_day(self):
        d = Pendulum.now()
        d2 = d.start_of('day')
        self.assertTrue(d.is_same_day(d2))

    def is_day_of_week(self):
        for i in Pendulum._days.values():
            d = Pendulum.now().next(getattr(Pendulum, i.upper()))
            self.assertTrue(getattr(d, 'is_{}s'.format(i.lower()))())
