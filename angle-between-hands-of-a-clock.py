def solution(hour, minutes):
  # 12 hours on the clock
  # 1 h represents 30 degree 
  # 60 minutes on the cloco
  # 1 m represents 6 degree

  h = (hour + minutes/60) * 30 # convert minute to hour, hour hand points to the minutes between hour
  m = minutes * 6

  # find the angle of the hour and minute
  angle = abs(h-m)

  # return the smallest angle
  return min(angle, 360 - angle)
