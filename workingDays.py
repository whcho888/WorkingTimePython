#-*- coding: utf-8 -*-
from datetime import datetime, timedelta

#If you use django, use datetime instead of datetime. Just replace datetime -> datetime in this file :)
#from django.utils import datetime


class Holidays:
    def __is_working_day__(self, dt, holidays):
        return dt.weekday() < 5 and dt.date() not in holidays

    def __get_xday_before_workingDate__(self, now, holidays, pastDay=0):
        while not pastDay == -1:
            if self.__is_working_day__(now, holidays):
                pastDay -= 1
                if pastDay == -1: break
            now = now - timedelta(days=1)
        return now.date()

    def __get_before_workingDate__(self, now, holidays):
        while not self.__is_working_day__(now, holidays):
            now = now - timedelta(days=1)
        return now.date()

    def __get_after_workingDate__(self, now, holidays):
        while not self.__is_working_day__(now, holidays):
            now = now + timedelta(days=1)
        return now.date()


class KoreanBDay(Holidays):
    thisYear = datetime.now().year
    holidays = []

    def __init__(self):
        self.thisYear = datetime.now().year

        self.holidays = [
            datetime(self.thisYear, 1, 1).date(),      # 신정
            datetime(self.thisYear, 2, 7).date(),      # 설연휴
            datetime(self.thisYear, 2, 8).date(),      # 설연휴
            datetime(self.thisYear, 2, 9).date(),      # 설연휴
            datetime(self.thisYear, 3, 1).date(),      # 삼일절
            datetime(self.thisYear, 5, 5).date(),      # 어린이날
            datetime(self.thisYear, 5, 14).date(),     # 석가탄신일
            datetime(self.thisYear, 6, 6).date(),      # 현충일
            datetime(self.thisYear, 8, 15).date(),     # 광복절
            datetime(self.thisYear, 9, 14).date(),     # 추석연휴
            datetime(self.thisYear, 9, 15).date(),     # 추석연휴    TODO: 연휴기간 확정시 대체 휴일 체킹
            datetime(self.thisYear, 9, 16).date(),     # 추석연휴
            datetime(self.thisYear, 10, 3).date(),     # 개천절
            datetime(self.thisYear, 10, 9).date(),     # 한글날
            datetime(self.thisYear, 12, 25).date(),    # 크리스마스

            #대체 휴일
            datetime(self.thisYear, 2, 10).date(),     # 설연휴 대체 휴일
        ]

    def print_year(self):
        print self.thisYear

    def reset_year(self):
        self.thisYear = datetime.now().year

    def is_working_day(self, dt, pastDay=0):
        return self.__is_working_day__(dt - timedelta(days=pastDay), self.holidays)

    # 오늘로 부터 pastday 일 전 기준에서 그 직전 영업일 (pastDay = 1 이면, 어제가 영업일인지 확인. 아니라면 그 전 가장 가까운 영업일을 date 형태로 반환)
    # If pastday is 1, then search yesterday first. Go past until first working day would be and return date of that
    # working date.
    def get_before_workingDate(self, now, pastDay=0):
        return self.__get_before_workingDate__(now - timedelta(days=pastDay), self.holidays)

    # 오늘로부터 영업일 기준 pastday 일 전 영업일 (pastDay = 1 이면, 오늘 기준으로 두번째 영업일을 date 형태로 반환)
    # If pastday is 1, then return second working date from today.
    def get_xday_before_workingDate(self, now, pastDay=0):
        return self.__get_xday_before_workingDate__(now, self.holidays, pastDay)

    def get_after_workingDate(self, now, pastDay=0):
        return self.__get_after_workingDate__(now - timedelta(days=pastDay), self.holidays)

    def print_holidays(self):
        print self.holidays


KBD = KoreanBDay()