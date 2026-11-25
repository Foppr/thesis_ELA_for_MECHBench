import numpy as np

class OscillatorySaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and decay rates with slight mutations
        self.freqs = [2.5 + 2.0 * np.sin(i * 0.75 + 0.6) for i in range(dim)]
        self.decay_rates = [0.6 + 0.4 * np.cos(i * 0.65 + 1.1) for i in range(dim)]
        self.saddle_centers = [np.sin(i * 0.85 + 0.35) * 3.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component with mutated terms
        oscillatory = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.75) + \
                          np.sin(freq * x[i] * 1.4) * np.cos(freq * x[i] * 0.45)
        
        # Exponential decay interactions with mutated coefficients
        decay = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 2.2)
        
        # Saddle-point cluster structure with mutated terms
        saddle = 0.0
        for i in range(self.dim):
            center = self.saddle_centers[i]
            saddle += (x[i] - center) ** 2 * (x[i] + center) ** 2
        
        # Cross-dimensional coupling with mutated modulations
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modulation_i = np.sin(0.6 * (i + j) + 1.3)
                modulation_j = np.cos(0.6 * (i - j) + 0.9)
                coupling += (x[i] * x[j]) * modulation_i * modulation_j
        
        # Combined function with mutated scaling factors
        total = 1.5 * oscillatory + 1.1 * decay + 0.8 * saddle + 0.6 * coupling
        
        return total