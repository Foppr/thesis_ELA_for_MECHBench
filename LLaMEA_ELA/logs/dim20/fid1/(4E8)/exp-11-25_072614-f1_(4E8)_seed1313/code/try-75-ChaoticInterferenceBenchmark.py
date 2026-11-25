import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 2.0) * np.sin(4.0 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with phase shifts
        trig_term = np.sum(np.sin(1.5 * x) * np.cos(2.7 * x) * np.sin(4.3 * x) * np.cos(6.1 * x)) / self.dim
        
        # Saddle point structure with adaptive polynomial weights and cross-terms
        saddle_term = np.sum(x**6 * np.sin(x)**3 + x**5 * np.cos(x)**3 + x**2 * np.sin(x**2.7)) / (self.dim * 10.0)
        
        # Chaos-inducing logarithmic component with fractal-like oscillation
        chaos_term = np.sum(np.log(1.0 + x**3.7) * np.sin(x**1.9)) / self.dim
        
        # Novel radial symmetry component with radial decay and angular modulation
        radial_term = np.sum((np.linalg.norm(x, ord=2)**2 / (1.0 + np.linalg.norm(x, ord=2)**1.7)) * np.cos(np.linalg.norm(x, ord=2)**0.9)) / self.dim
        
        # Additional hyper-multimodal term with varying amplitude and frequency
        multi_term = np.sum(np.sin(7.2 * x) * np.exp(-x**2 / 6.0) * np.cos(3.5 * x)) / self.dim
        
        # Adaptive weighting with dynamic adjustment based on dimensionality
        weight_exp = 0.29 + 0.02 * np.sin(self.dim / 8.0)
        weight_trig = 0.31 + 0.05 * np.cos(self.dim / 10.0)
        weight_saddle = 0.24 + 0.05 * np.sin(self.dim / 5.0)
        weight_chaos = 0.12 + 0.03 * np.cos(self.dim / 6.0)
        weight_radial = 0.05 + 0.04 * np.sin(self.dim / 13.0)
        weight_multi = 0.07
        
        total = (weight_exp * exp_term + 
                weight_trig * trig_term + 
                weight_saddle * saddle_term + 
                weight_chaos * chaos_term + 
                weight_radial * radial_term + 
                weight_multi * multi_term)
        
        return total