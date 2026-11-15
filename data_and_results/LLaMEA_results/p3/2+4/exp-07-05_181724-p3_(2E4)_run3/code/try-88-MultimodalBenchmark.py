import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential potential wells with varying scales
        exp_well = np.sum(np.exp(-0.5 * x_norm**2) - np.exp(-2.0 * x_norm**2))
        
        # Nested exponential terms with different coupling strengths
        nested_exp = np.sum(np.exp(-0.1 * x_norm**4) + np.exp(-0.05 * x_norm**6))
        
        # Cross-dimensional coupling with chaotic sine modulation
        coupling = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                coupling += np.sin(10 * x_norm[i] * x_norm[i+1]) * (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Polynomial interaction terms with alternating signs
        poly_interaction = np.sum((-1)**np.arange(self.dim) * x_norm**3)
        
        # Saddle-point structure using hyperbolic tangents
        saddle = np.sum(np.tanh(x_norm)**2 - 0.5 * x_norm**2)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        freq_mod = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Radial basis function with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                rbf += np.exp(-5.0 * (x_norm[i] - center)**2)
        
        # Chaotic logistic map component for added complexity
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(100 * np.sin(x_norm[i]) * np.cos(x_norm[i+1]))
        
        # Combine all components with carefully tuned weights
        return (0.25 * exp_well + 
                0.2 * nested_exp + 
                0.15 * coupling + 
                0.1 * poly_interaction + 
                0.1 * saddle + 
                0.1 * freq_mod + 
                0.08 * rbf + 
                0.07 * chaotic)