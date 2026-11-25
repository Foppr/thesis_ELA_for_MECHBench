import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified polynomial base with stronger higher-order terms
        f_val = 2.0 * np.sum(x_norm**4) + 0.6 * np.sum(x_norm**7)
        
        # Enhanced trigonometric perturbations with higher frequencies
        f_val += 3.5 * np.sum(np.sin(6 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Strengthened Gaussian-like attractive points with tighter variance
        gaussian_penalty = 0.0
        centers = np.linspace(-0.8, 0.8, 9)
        for c in centers:
            gaussian_penalty += 2.0 * np.exp(-20 * np.sum((x_norm - c)**2))
        
        f_val += gaussian_penalty
        
        # Increased cross-dimensional interactions with more complex coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                cross_term += 0.6 * np.sin(2.0 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(1.2 * np.pi * (x_norm[i] - x_norm[j]))
        f_val += cross_term
        
        # Adjusted penalty to ensure global minimum is at origin with sharper curvature
        f_val += 0.25 * np.sum(np.abs(x_norm)**3.8)
        
        return f_val