import numpy as np

class OscillatorySaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and decay rates
        self.freqs = [2.0 + 1.5 * np.sin(i * 0.7 + 0.5) for i in range(dim)]
        self.decay_rates = [0.5 + 0.3 * np.cos(i * 0.6 + 1.0) for i in range(dim)]
        self.saddle_centers = [np.sin(i * 0.8 + 0.3) * 3.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component
        oscillatory = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                          np.sin(freq * x[i] * 1.3) * np.cos(freq * x[i] * 0.4)
        
        # Exponential decay interactions
        decay = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 2.0)
        
        # Saddle-point cluster structure
        saddle = 0.0
        for i in range(self.dim):
            center = self.saddle_centers[i]
            saddle += (x[i] - center) ** 2 * (x[i] + center) ** 2
        
        # Cross-dimensional coupling with periodic modulations
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modulation_i = np.sin(0.5 * (i + j) + 1.2)
                modulation_j = np.cos(0.5 * (i - j) + 0.8)
                coupling += (x[i] * x[j]) * modulation_i * modulation_j
        
        # Combined function with dynamic scaling
        total = 1.2 * oscillatory + 0.9 * decay + 0.7 * saddle + 0.5 * coupling
        
        return total