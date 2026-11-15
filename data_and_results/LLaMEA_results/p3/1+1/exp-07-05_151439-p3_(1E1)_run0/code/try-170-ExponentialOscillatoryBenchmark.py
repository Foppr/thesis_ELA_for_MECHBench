import numpy as np

class ExponentialOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay term with oscillatory modulation
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.cos(2 * np.pi * x) * np.sin(3 * np.pi * x)) / self.dim
        
        # Multimodal trigonometric component with varying frequencies
        trig_term = np.sum(np.sin(5 * x) * np.cos(7 * x) * np.sin(9 * x) * np.cos(11 * x)) / self.dim
        
        # Adaptive dimensional coupling with dynamic scaling
        coupling_term = 0
        if self.dim > 1:
            for i in range(self.dim - 1):
                scale = 1.0 + 0.5 * np.sin(self.dim * 0.5 + i * 0.3)
                coupling_term += scale * np.exp(-0.1 * (x[i] - x[i+1])**2) * np.cos(2 * np.pi * (x[i] + x[i+1]))
        coupling_term /= (self.dim - 1)
        
        # Hybrid polynomial-exponential component
        poly_exp_term = np.sum((1.0 + 0.3 * np.sin(x)) * x**4 + 0.5 * np.exp(-x**2) * np.cos(4 * x)) / self.dim
        
        # Dynamic noise component with dimensional dependence
        noise = np.sum(0.01 * np.random.randn() * np.sin(self.dim * 0.1 * x)) / self.dim
        
        # Combine all terms with adaptive weights
        weights = [0.35 + 0.05 * np.sin(self.dim * 0.2), 
                  0.30 + 0.05 * np.cos(self.dim * 0.3),
                  0.20 + 0.05 * np.sin(self.dim * 0.4),
                  0.15 + 0.05 * np.cos(self.dim * 0.5)]
        
        result = weights[0] * exp_term + weights[1] * trig_term + weights[2] * coupling_term + weights[3] * poly_exp_term
        
        return result + noise