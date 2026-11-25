import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced quadratic basin term with dimension-dependent scaling
        quadratic_term = 0.3 * np.sum(x_normalized**2) * (1 + 0.1 * self.dim)
        
        # Chaotic sinusoidal components with exponential decay and dynamic frequencies
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 15 * (1.7 ** i) * (1 + 0.3 * np.sin(0.5 * i))
            chaotic_term += np.sin(freq * x_normalized[i]) * np.exp(-0.3 * i) * (1 + 0.3 * x_normalized[i]**4)
        
        # Cross-dimensional interactions with variable coupling strength and dynamic phase shifts
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 * (1 - np.exp(-0.15 * (i + j))) * (1 + 0.2 * np.cos(0.3 * (i - j)))
                phase_shift = 0.1 * np.sin(0.4 * (i + j))
                cross_term += coupling * np.sin(10 * np.pi * x_normalized[i] + phase_shift) * np.cos(7 * np.pi * x_normalized[j] + phase_shift)
        
        # Dynamic global minimum shift with enhanced complexity
        shift = 0.4 * (self.dim / 15.0)
        shift_term = 1.0 * np.sum((x_normalized - shift)**4) + 0.5 * np.sum((x_normalized + shift)**2)
        
        # Additional high-frequency oscillatory component for increased complexity
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(25 * x_normalized[i]) * np.cos(18 * x_normalized[i]) * np.exp(-0.2 * i)
        
        return quadratic_term + chaotic_term + cross_term + shift_term + high_freq_term