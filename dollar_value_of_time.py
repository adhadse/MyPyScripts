# Copyright 2022 MyPyScripts Author. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
People don't really know what their hour/minute is worth of.
If we know what value your hour or minute is of, we can make meaningful financial
decisions.
Say, how much time you're exchanging for the thing that you are buying or does it
make sense to spend more than an hour for a thing that costs lower than your hourly
worth (Well NO).

This script can help you decide your hour worth. The rest is your responsibility.
"""


def value_of_time(income, month_or_year, include_only_work_hours, work_hours=None):
  """
  Calculates value of time (in hour, minute and day)
  includes all time that doesn't contribute to your income (leisure time)

  Params:
    income: income (can be in any currency)
    month_or_year: income param value is monthly or yearly
    include_only_work_hours: does the value need to be calculated with respect
      to only work hours (time you spend on work that generate your income)
    work_hours: total work hours (Per Week)
  Returns:
    None
  """
  if month_or_year == "month":
    value_per_month = income
  else:
    value_per_month = income / 12

  if include_only_work_hours:
    print(f"\nYour Value of Hour: {round(value_per_month / (4.34 * work_hours), 1)}")
    print(f"Your Value of Minute: "
          f"{round(value_per_month / (4.34 * work_hours * 60), 1)}")
  else:
    print(f"\nYour Value of Hour: {round(value_per_month / 730, 1)}")
    print(f"Your Value of Minute: {round(value_per_month / (730*60), 1)}")

  # The value of day doesn't really depend on how much you earn an hour.
  print(f"Your Value of Day: {round(value_per_month / 30.41, 1)}")


if __name__ == '__main__':
  m_or_y = str(input("Income is is months or in Year (m/y): "))
  if m_or_y not in ['m', 'M', 'y', 'Y']:
    raise ValueError(f"Input was expected to be either (m, M, y, Y). Found: "
                     f"{m_or_y}")

  incl_only_wrk_hours = str(input("Include only work hours: (t/f): "))
  if incl_only_wrk_hours not in ['t', 'T', 'f', 'F']:
    raise ValueError(f"Input was expected to be either (t, T, f, F). Found:"
                     f"{incl_only_wrk_hours}")

  if incl_only_wrk_hours == 't' or incl_only_wrk_hours == 'T':
    wrk_hours = int(input("Input your total work hour (Per week) "))
    if wrk_hours > 168:
      raise ValueError("Sorry, this Python Script is for Humans not for "
                       "extraterrestrials. On Earth we have only 168 hours in a 7 day "
                       "week.")
    incl_only_wrk_hours = True
  else:
    incl_only_wrk_hours = False
    wrk_hours = None

  if m_or_y == 'm' or m_or_y == 'M':
    income = float(input(f"Your current income (per month): "))
    value_of_time(income, "month", incl_only_wrk_hours, wrk_hours)
  elif m_or_y == 'y' or m_or_y == 'Y':
    income = float(input(f"Your current income (per year): "))
    value_of_time(income, "year", incl_only_wrk_hours, wrk_hours)
