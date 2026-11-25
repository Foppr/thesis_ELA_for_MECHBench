import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like self-similarity pattern with recursive sine-cosine combinations
        fractal_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                             np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Adaptive elliptic potentials with dimension-dependent scaling
        elliptic_term = np.sum((x_norm**2 + 0.1 * x_norm**4) * (1 + 0.2 * np.sin(np.pi * x_norm)))
        
        # Cross-dimensional harmonic coupling with varying interaction strengths
        harmonic_coupling = 0.0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                harmonic_coupling += np.sin(4 * np.pi * dist) * np.cos(3 * np.pi * dist)
        
        # Multi-scale repulsion field with exponential and polynomial decay
        center_distance = np.sqrt(np.sum(x_norm**2))
        repulsion_term = 1.5 / (1.0 + center_distance**2 + 0.1 * center_distance**4 + 
                              0.05 * center_distance**6)
        
        # Add dimensionality-dependent noise for robustness
        noise = 0.02 * np.random.normal(0, 1, self.dim)
        
        # Condition number varying interaction through adaptive weights
        condition_weights = 1.0 + 0.3 * np.sin(2 * np.pi * x_norm)
        weighted_term = np.sum(condition_weights * x_norm**3)
        
        return fractal_term + elliptic_term + harmonic_coupling - repulsion_term + weighted_term + np.sum(noise)