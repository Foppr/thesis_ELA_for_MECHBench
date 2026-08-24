import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for dynamic behavior
        self.chaotic_seq = np.sin(np.arange(dim) * np.pi / 4.0) * 0.5 + 0.5
        self.freq_seq = np.cos(np.arange(dim) * np.pi / 3.0) * 0.4 + 0.6
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic terms with chaotic scaling
        result = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * self.chaotic_seq[i]
            result += scale * (x[i] - 1.0)**2 + 0.3 * (x[i] + 2.0)**2
        
        # Non-separable chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 2.0 + 1.5 * self.chaotic_seq[i] * self.chaotic_seq[j]
                phase = self.freq_seq[i] * self.freq_seq[j]
                result += coeff * np.sin(3.0 * (x[i] + x[j]) + phase) * (x[i] - x[j])**2
        
        # Trigonometric modulation with dynamic frequencies
        for i in range(self.dim):
            freq = 2.0 + 1.2 * self.freq_seq[i]
            amp = 0.8 + 0.3 * self.chaotic_seq[i]
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + self.chaotic_seq[i])
        
        # Dynamic global shift based on input values
        shift = np.array([0.5 * np.sin(x[i] * np.pi / 5.0) for i in range(self.dim)])
        result += 0.2 * np.sum((x - shift)**2)
        
        # High-frequency chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(20.0 * x[i] + self.chaotic_seq[i] * np.pi) * np.cos(15.0 * x[i] + self.freq_seq[i] * np.pi)
        result += noise
        
        # Higher-order polynomial and chaotic coupling
        result += 0.005 * np.sum(x**4) + 0.003 * np.sum(x**6) + 0.001 * np.sum(x**8)
        
        # Additional multimodal sinusoidal landscape
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.04 * np.sin(10.0 * x[i] + self.chaotic_seq[i] * np.pi) * np.cos(8.0 * x[i] + self.freq_seq[i] * np.pi)
        result += multimodal
        
        return result