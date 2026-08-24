import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay with trigonometric modulation
        exp_term = np.sum(np.exp(-0.5 * np.sum(x**2)) * 
                         np.cos(2 * np.pi * np.sum(x**1.5)) * 
                         np.sin(3 * np.pi * np.sum(x**2.5)) * 
                         np.cos(4 * np.pi * np.sum(x**3.5)) * 
                         np.sin(5 * np.pi * np.sum(x**4.5))) / self.dim
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_term = np.sum((1 + 0.1 * np.sin(self.dim * 0.5)) * 
                          np.exp(-0.1 * np.sum(x**2)) * 
                          np.cos(2 * np.pi * x) * 
                          np.sin(3 * np.pi * x) * 
                          np.cos(4 * np.pi * x) * 
                          np.sin(5 * np.pi * x)) / self.dim
        
        # Cross-dimensional coupling with dynamic weights
        cross_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                weight = 1.0 + 0.5 * np.sin(i * 0.3 + self.dim * 0.7)
                cross_term += weight * np.abs(x[i] - x[i+1]) * np.cos(np.pi * (x[i] + x[i+1]))
        cross_term /= (self.dim - 1)
        
        # Multi-oscillator harmonic landscape
        harmonic_term = np.sum(np.sin(2 * np.pi * x) * 
                              np.cos(3 * np.pi * x) * 
                              np.sin(4 * np.pi * x) * 
                              np.cos(5 * np.pi * x) * 
                              np.sin(6 * np.pi * x) * 
                              np.cos(7 * np.pi * x) * 
                              np.sin(8 * np.pi * x) * 
                              np.cos(9 * np.pi * x) * 
                              np.sin(10 * np.pi * x) * 
                              np.cos(11 * np.pi * x)) / self.dim
        
        # Adaptive noise component
        noise = 0.01 * np.random.rand() * np.sum(np.sin(self.dim * x) * np.cos(self.dim * x))
        
        # Combine all terms with dynamic weights
        weights = [0.3 + 0.1 * np.sin(self.dim * 0.2),
                  0.25 + 0.1 * np.cos(self.dim * 0.3),
                  0.2 + 0.1 * np.sin(self.dim * 0.4),
                  0.15 + 0.1 * np.cos(self.dim * 0.5),
                  0.1 + 0.1 * np.sin(self.dim * 0.6)]
        
        result = (weights[0] * exp_term + 
                 weights[1] * cond_term + 
                 weights[2] * cross_term + 
                 weights[3] * harmonic_term + 
                 weights[4] * noise)
        
        return result