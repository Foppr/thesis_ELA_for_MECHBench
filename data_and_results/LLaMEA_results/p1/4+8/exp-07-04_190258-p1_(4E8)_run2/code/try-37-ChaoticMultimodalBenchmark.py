import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay base
        exp_decay = np.sum(np.exp(-0.1 * np.abs(x)))
        
        # Trigonometric modulation with varying frequencies
        trig_mod = 0
        for i in range(self.dim):
            trig_mod += np.sin(3 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Polynomial cross-terms with varying degrees
        poly_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_cross += 0.1 * (x[i]**3 + x[j]**3) * (x[i]**2 + x[j]**2)
        
        # Saddle-point enhanced structure with sinusoidal perturbations
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2) * np.sin(2 * x[i])
        
        # Chaotic interaction term
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        return exp_decay + trig_mod + poly_cross + saddle + chaotic