import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial coupling with cross-terms
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i] ** 3) * (x[j] ** 2) * np.sin(x[i] + x[j])
        
        # Dynamic sinusoidal modulation with time-varying frequencies
        dynamic_sin = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.5 * i)
            dynamic_sin += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Adaptive penalty corridors with varying severity
        adaptive_penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                adaptive_penalty += (np.abs(x[i]) - 4.0) ** 3 * np.exp(-0.2 * (x[i] ** 2))
            else:
                adaptive_penalty += 0.1 * (np.abs(x[i]) - 2.0) ** 4
        
        # Chaotic component with modified logistic map and cross-coupling
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                chaotic += x[i] * (r * (1 - x[i])) + 0.1 * np.sin(x[i])
            else:
                chaotic += x[i] * (r * (1 - x[i-1])) + 0.05 * np.cos(x[i-1])
        
        # Multi-scale Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        centers = np.linspace(-4.5, 4.5, 7)
        for center in centers:
            gaussian_peaks += np.exp(-0.5 * np.sum((x - center) ** 2) / (1.0 + 0.1 * np.abs(center))) * np.cos(3 * np.pi * np.sum((x - center) ** 2))
        
        # Cross-term exponential attraction basins
        cross_attraction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j]) ** 2 + 1e-8)
                cross_attraction += np.exp(-dist) * np.sin(2 * np.pi * dist)
        
        # Combined fitness with adjusted weights
        return 0.4 * poly_coupling + 0.3 * dynamic_sin + 0.2 * adaptive_penalty + 0.05 * chaotic + 0.05 * gaussian_peaks + cross_attraction