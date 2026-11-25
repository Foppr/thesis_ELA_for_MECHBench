import numpy as np

class OscillatorySaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and decay rates with slight mutation
        self.freqs = [2.5 + 2.0 * np.sin(i * 0.7 + 0.5) for i in range(dim)]
        self.decay_rates = [0.6 + 0.4 * np.cos(i * 0.6 + 1.0) for i in range(dim)]
        self.saddle_centers = [np.sin(i * 0.8 + 0.3) * 3.5 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component with modified frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                          np.sin(freq * x[i] * 1.3) * np.cos(freq * x[i] * 0.4) + \
                          0.3 * np.sin(3.0 * freq * x[i])  # Added cubic harmonic
        
        # Exponential decay interactions with altered decay rates
        decay = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 2.0) + \
                     0.2 * np.exp(-0.5 * x[i]**2)  # Added Gaussian term
        
        # Saddle-point cluster structure with modified center positions
        saddle = 0.0
        for i in range(self.dim):
            center = self.saddle_centers[i]
            saddle += (x[i] - center) ** 2 * (x[i] + center) ** 2 + \
                      0.1 * x[i]**3  # Added cubic term for additional nonlinearity
        
        # Cross-dimensional coupling with periodic modulations
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modulation_i = np.sin(0.5 * (i + j) + 1.2)
                modulation_j = np.cos(0.5 * (i - j) + 0.8)
                coupling += (x[i] * x[j]) * modulation_i * modulation_j + \
                           0.05 * np.sin(x[i] + x[j])  # Added sine coupling
        
        # Combined function with dynamic scaling
        total = 1.2 * oscillatory + 0.9 * decay + 0.7 * saddle + 0.5 * coupling
        
        return total