import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay modulated by trigonometric functions
        exp_term = np.sum(np.exp(-np.abs(x) / (1.0 + 0.5 * np.sin(x * 2.3))) * 
                         np.cos(x * 3.1) * np.sin(x * 1.7)) / self.dim
        
        # Trigonometric oscillations with adaptive frequency and amplitude
        trig_term = np.sum((1.0 + 0.3 * np.sin(self.dim * 0.7)) * 
                          np.sin(x * (2.0 + 0.2 * np.cos(self.dim * 0.5))) * 
                          np.cos(x * (1.5 + 0.1 * np.sin(self.dim * 0.3))) * 
                          np.sin(x * (1.2 + 0.15 * np.cos(self.dim * 0.8))) * 
                          np.cos(x * (0.9 + 0.1 * np.sin(self.dim * 0.6)))) / self.dim
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = np.sum((1.0 + 0.2 * np.sin(self.dim * 0.4)) * 
                          x**2 * np.exp(-x**2 / (2.0 + 0.3 * np.cos(self.dim * 0.9))) + 
                          (0.5 + 0.1 * np.cos(self.dim * 0.6)) * x**3 * np.exp(-x**2 / (3.0 + 0.2 * np.sin(self.dim * 0.7)))) / self.dim
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                strength = 0.8 + 0.4 * np.sin(i * 0.5 + self.dim * 0.3)
                cross_term += strength * np.sin(x[i] * x[i+1] * 0.5) * np.cos(x[i] + x[i+1] * 0.3)
        cross_term /= (self.dim - 1)
        
        # Multi-scale harmonic noise with dimensionality influence
        noise = np.sum(0.05 * np.sin(self.dim * x) * np.cos(x * 0.7) + 
                      0.03 * np.sin(x * 1.3) * np.cos(self.dim * x * 0.4) + 
                      0.02 * np.sin(x * 2.1) * np.cos(x * 1.1) * np.sin(self.dim * 0.8)) / self.dim
        
        # Combine all terms with dynamic weights
        weights = [0.35 + 0.1 * np.sin(self.dim * 0.5), 
                  0.30 + 0.1 * np.cos(self.dim * 0.7), 
                  0.20 + 0.05 * np.sin(self.dim * 0.9), 
                  0.15 + 0.05 * np.cos(self.dim * 1.1)]
        
        result = (weights[0] * exp_term + 
                 weights[1] * trig_term + 
                 weights[2] * cond_term + 
                 weights[3] * cross_term)
        
        return result + noise