const WEEKDAYS = {
  0: 'sunday',
  1: 'monday',
  2: 'tuesday',
  3: 'wednesday',
  4: 'thursday',
  5: 'friday',
  6: 'saturday'
}

const WEEKDAYS_SHORT = {
  0: 'sun',
  1: 'mon',
  2: 'tue',
  3: 'wed',
  4: 'thu',
  5: 'fri',
  6: 'sat'
}

const MONTH_STR = {
  0: 'january',
  1: 'february',
  2: 'march',
  3: 'april',
  4: 'may',
  5: 'june',
  6: 'july',
  7: 'august',
  8: 'september',
  9: 'october',
  10: 'november',
  11: 'december'
}

function padTo2Digits (num) {
  return num.toString().padStart(2, '0')
}

export function getDate (date) {
  return {
    day: date.getDate(),
    month: date.getMonth(),
    monthText: MONTH_STR[date.getMonth()],
    year: date.getFullYear(),
    weekDay: WEEKDAYS[date.getDay()],
    weekDayShort: WEEKDAYS_SHORT[date.getDay()],
    time: date.getTime(),
    date
  }
}

export function outputDate (date) {
  return [
    date.getFullYear(),
    padTo2Digits(date.getMonth() + 1),
    padTo2Digits(date.getDate())
  ].join('-')
}
