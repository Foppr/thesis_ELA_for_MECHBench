import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Polynomial potential term
        poly_term = np.sum(x**4) * 0.01
        
        # Sinusoidal oscillation term with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2.0
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i == 0:
                prev_x = x[-1]
            else:
                prev_x = x[i-1]
            chaotic_term += np.sin(prev_x * x[i] * 2.0) * 0.1
            
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
        
        # Add noise and scaling
        noise = np.sum(np.random.uniform(-0.01, 0.01, self.dim))
        
        return poly_term - sin_term + chaotic_term + cross_term + noise