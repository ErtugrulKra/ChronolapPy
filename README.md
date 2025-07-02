# Chronolap

Advanced stopwatch with lap tracking for Python developers.

## Installation

```bash
pip install chronolap
```


```python

from chronolap import ChronolapTimer

timer = ChronolapTimer()
timer.start()
# your code
timer.lap("First section")
timer.stop()

for lap in timer.laps:
    print(lap)

```

## ⏱️ Python vs .NET: Stopwatch Comparison

| Feature                | .NET `Stopwatch`           | Python (built-in)            | Chronolap (This Project)       |
|------------------------|----------------------------|-------------------------------|--------------------------------|
| Start / Stop           | ✅ `Start()`, `Stop()`      | ❌ (requires manual handling) | ✅ `start()`, `stop()`         |
| Restart                | ✅ `Restart()`              | ❌                             | ✅ `restart()`                 |
| Elapsed Time           | ✅ `Elapsed`, `ElapsedMs`   | ✅ `perf_counter()` difference| ✅ `elapsed`, `elapsed_ms`     |
| Lap Support            | ❌                          | ❌                             | ✅ `lap()`, `laps`             |
| Sync Measurement       | ❌                          | ❌                             | ✅ `measure(func)`             |
| Async Measurement      | ❌                          | ❌                             | ✅ `async_measure(async_func)`|
| High-resolution Timer  | ✅ Hardware-based           | ⚠️ Platform-dependent          | ✅ Uses `time.perf_counter()`  |

> 📌 The built-in `Stopwatch` in .NET has no direct equivalent in Python. **Chronolap** fills this gap with a fully featured stopwatch, lap tracking, and performance measurement tool.


## Support

If you find this project useful, consider supporting me:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/ertugrulkara)

## License

MIT © Ertugrul Kara
