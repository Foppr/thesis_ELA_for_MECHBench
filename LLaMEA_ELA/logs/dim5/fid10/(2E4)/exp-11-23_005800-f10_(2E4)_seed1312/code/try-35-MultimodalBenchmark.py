import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Modified polynomial base with stronger higher-order terms and altered weights
        f_val = 1.8 * np.sum(x_norm**4) + 0.7 * np.sum(x_norm**8)
        
        # Enhanced trigonometric perturbations with higher frequencies and modified amplitudes
        f_val += 4.0 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Strengthened Gaussian-like attractive points with tighter variance and more centers
        gaussian_penalty = 0.0
        centers = np.linspace(-0.9, 0.9, 11)
        for c in centers:
            gaussian_penalty += 2.5 * np.exp(-25 * np.sum((x_norm - c)**2))
        
        f_val += gaussian_penalty
        
        # Increased cross-dimensional interactions with more complex coupling and extended range
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling range
                cross_term += 0.7 * np.sin(2.5 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(1.5 * np.pi * (x_norm[i] - x_norm[j]))
        f_val += cross_term
        
        # Adjusted penalty to ensure global minimum is at origin with sharper curvature
        f_val += 0.3 * np.sum(np.abs(x_norm)**4.0)
        
        return f_val