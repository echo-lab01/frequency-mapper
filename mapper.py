#!/usr/bin/env python3
import math

def frequency_to_band(freq_hz):
    """
    Very rough dummy mapping of frequency to a 'band' label.
    This function is intentionally simple and not scientifically accurate.
    """
    if freq_hz < 300:
        return "low"
    elif freq_hz < 3000:
        return "mid"
    else:
        return "high"

def main():
    test_freqs = [100, 440, 1000, 5000, 10000]
    for f in test_freqs:
        print(f"{f} Hz -> {frequency_to_band(f)}")

if __name__ == "__main__":
    main()
