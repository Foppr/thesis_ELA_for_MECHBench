import numpy as np

class OscillatorySaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and decay rates with slight mutation
        self.freqs = [2.0 + 3.0 * np.sin(i * 0.6 + 0.4) for i in range(dim)]
        self.decay_rates = [0.5 + 0.5 * np.cos(i * 0.7 + 1.1) for i in range(dim)]
        self.saddle_centers = [np.sin(i * 0.9 + 0.2) * 4.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillatory component with modified frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            oscillatory += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.6) + \
                          np.sin(freq * x[i] * 1.4) * np.cos(freq * x[i] * 0.5) + \
                          0.4 * np.sin(3.0 * freq * x[i]) + \
                          0.2 * np.sin(5.0 * freq * x[i])  # Added higher harmonic
        
        # Exponential decay interactions with altered decay rates
        decay = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            decay += np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 1.8) + \
                     0.3 * np.exp(-0.3 * x[i]**2) + \
                     0.1 * np.exp(-0.7 * x[i]**2)  # Added multiple Gaussian terms
        
        # Saddle-point cluster structure with modified center positions
        saddle = 0.0
        for i in range(self.dim):
            center = self.saddle_centers[i]
            saddle += (x[i] - center) ** 2 * (x[i] + center) ** 2 + \
                      0.15 * x[i]**3 + \
                      0.05 * x[i]**4  # Added quartic term for additional nonlinearity
        
        # Cross-dimensional coupling with periodic modulations
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modulation_i = np.sin(0.6 * (i + j) + 1.3)
                modulation_j = np.cos(0.4 * (i - j) + 0.9)
                coupling += (x[i] * x[j]) * modulation_i * modulation_j + \
                           0.08 * np.sin(x[i] + x[j]) + \
                           0.03 * np.cos(x[i] - x[j])  # Added cosine coupling
        
        # Combined function with dynamic scaling
        total = 1.5 * oscillatory + 1.0 * decay + 0.8 * saddle + 0.6 * coupling
        
        return total