from chronolap import ChronolapTimer

timer = ChronolapTimer()
timer.start()
# your code
timer.lap("First section")
timer.stop()

for lap in timer.laps:
    print(lap)
