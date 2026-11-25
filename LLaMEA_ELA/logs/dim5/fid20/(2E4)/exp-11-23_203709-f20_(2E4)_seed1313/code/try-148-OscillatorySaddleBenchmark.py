import numpy as np

class OscillatorySaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute oscillatory frequencies and decay rates with significant mutation
        self.freqs = [3.0 + 3.5 * np.sin(i * 0.9 + 0.7) for i in range(dim)]
        self.decay_rates = [0.8 + 0.6 * np.cos(i * 0.8 + 1.5) for i in range(dim)]
        self.saddle_centers = [np.sin(i * 1.0 + 0.5) * 4.0 for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Intensified periodic oscillatory component with stronger harmonics
        oscillatory = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            oscillatory += (np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + 
                           np.sin(freq * x[i] * 1.3) * np.cos(freq * x[i] * 0.4) + 
                           0.5 * np.sin(3.0 * freq * x[i]) + 
                           0.2 * np.sin(5.0 * freq * x[i]))  # Added higher harmonic
        
        # Stronger exponential decay interactions with enhanced decay rates
        decay = 0.0
        for i in range(self.dim):
            rate = self.decay_rates[i]
            decay += (np.exp(-rate * np.abs(x[i])) * np.sin(x[i] * 2.0) + 
                     0.3 * np.exp(-0.5 * x[i]**2) + 
                     0.1 * np.exp(-0.3 * x[i]**3))  # Added cubic decay term
        
        # Enhanced saddle-point cluster structure with stronger nonlinearity
        saddle = 0.0
        for i in range(self.dim):
            center = self.saddle_centers[i]
            saddle += (x[i] - center) ** 2 * (x[i] + center) ** 2 + 
                      0.2 * x[i]**4 +  # Added quartic term for stronger nonlinearity
                      0.15 * x[i]**3  # Increased cubic contribution
        
        # Augmented cross-dimensional coupling with stronger modulations
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                modulation_i = np.sin(0.8 * (i + j) + 1.5)
                modulation_j = np.cos(0.7 * (i - j) + 1.0)
                coupling += (x[i] * x[j]) * modulation_i * modulation_j + 
                           0.1 * np.sin(x[i] + x[j]) + 
                           0.08 * np.cos(x[i] - x[j])  # Added cosine coupling
        
        # Combined function with increased complexity and dynamic scaling
        total = 1.5 * oscillatory + 1.2 * decay + 1.0 * saddle + 0.8 * coupling
        
        return total