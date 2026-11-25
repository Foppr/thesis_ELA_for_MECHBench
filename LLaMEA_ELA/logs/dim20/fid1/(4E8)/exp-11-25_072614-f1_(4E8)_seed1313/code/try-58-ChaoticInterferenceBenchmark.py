import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced exponential decay with chaotic modulation
        exp_term = np.sum(np.exp(-x**2 / 2.5) * np.sin(3.5 * x)) / self.dim
        
        # Multi-frequency trigonometric interference with phase shifts
        trig_term = np.sum(np.sin(1.2 * x) * np.cos(2.3 * x) * np.sin(4.1 * x) * np.cos(5.7 * x)) / self.dim
        
        # Saddle point structure with adaptive polynomial weights and cross-terms
        saddle_term = np.sum(x**6 * np.sin(x)**3 + x**5 * np.cos(x)**3 + x**2 * np.sin(x**2.5)) / (self.dim * 12.0)
        
        # Chaos-inducing logarithmic component with fractal-like oscillation
        chaos_term = np.sum(np.log(1.0 + x**3.5) * np.sin(x**1.8)) / self.dim
        
        # Novel radial symmetry component with radial decay and angular modulation
        radial_term = np.sum((np.linalg.norm(x, ord=2)**2 / (1.0 + np.linalg.norm(x, ord=2)**1.5)) * np.cos(np.linalg.norm(x, ord=2)**0.8)) / self.dim
        
        # Additional hyper-multimodal term with varying amplitude and frequency
        multi_term = np.sum(np.sin(6.8 * x) * np.exp(-x**2 / 5.5) * np.cos(3.2 * x)) / self.dim
        
        # Adaptive weighting with dynamic adjustment based on dimensionality
        weight_exp = 0.27 + 0.03 * np.sin(self.dim / 9.0)
        weight_trig = 0.33 + 0.04 * np.cos(self.dim / 11.0)
        weight_saddle = 0.22 + 0.06 * np.sin(self.dim / 6.0)
        weight_chaos = 0.11 + 0.04 * np.cos(self.dim / 7.0)
        weight_radial = 0.06 + 0.03 * np.sin(self.dim / 14.0)
        weight_multi = 0.07
        
        total = (weight_exp * exp_term + 
                weight_trig * trig_term + 
                weight_saddle * saddle_term + 
                weight_chaos * chaos_term + 
                weight_radial * radial_term + 
                weight_multi * multi_term)
        
        return total