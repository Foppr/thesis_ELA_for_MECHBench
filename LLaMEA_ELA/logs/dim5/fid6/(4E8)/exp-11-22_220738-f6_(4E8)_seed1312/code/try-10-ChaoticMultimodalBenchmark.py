import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay term with varying rates
        exp_term = np.sum(np.exp(-np.abs(x_norm)) * (1 + 0.5 * np.sin(3 * x_norm)))
        
        # Trigonometric oscillations with multiple frequencies
        trig_term = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm))
        
        # Random perturbation component to increase chaos
        random_pert = np.sum(np.random.uniform(-0.1, 0.1, self.dim) * np.sin(7 * x_norm))
        
        # Combined landscape with different scaling factors
        return exp_term + 0.3 * trig_term + 0.05 * random_pert