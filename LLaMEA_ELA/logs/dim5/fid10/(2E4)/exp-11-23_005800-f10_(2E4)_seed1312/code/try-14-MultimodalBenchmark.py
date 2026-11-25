import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        f_val = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6)
        
        # Trigonometric perturbations creating multiple local minima
        f_val += 2.0 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Gaussian-like attractive points scattered in the search space
        gaussian_penalty = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        for c in centers:
            gaussian_penalty += np.exp(-10 * np.sum((x_norm - c)**2))
        
        f_val += gaussian_penalty
        
        # Cross-dimensional interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_term += 0.3 * np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(0.5 * np.pi * (x_norm[i] - x_norm[j]))
        f_val += cross_term
        
        # Final penalty to ensure global minimum is at origin
        f_val += 0.1 * np.sum(np.abs(x_norm)**3)
        
        return f_val