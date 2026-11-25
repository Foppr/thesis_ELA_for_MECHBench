import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay interactions between dimensions
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_decay += np.exp(-0.5 * (x[i] - x[j])**2) / (1.0 + np.abs(x[i] - x[j]))
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        gaussian_peaks = 0.0
        scales = [0.5, 1.0, 2.0, 4.0]
        for scale in scales:
            gaussian_peaks += np.sum(np.exp(-0.5 * ((x - scale) / (0.5 * scale))**2))
        
        # Adaptive penalty corridors based on dimension-wise distances from center
        penalties = 0.0
        for i in range(self.dim):
            penalties += 10.0 * np.exp(-0.1 * (x[i] - 2.5)**2) + 5.0 * np.exp(-0.05 * (x[i] + 2.5)**2)
        
        # Chaotic gradient modulation using logistic map
        chaotic_mod = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            chaotic_mod += np.sin(r * x[i] * (1 - x[i]))
        
        # Combined fitness function with mixed smoothness and ruggedness
        return exp_decay + gaussian_peaks + penalties + chaotic_mod