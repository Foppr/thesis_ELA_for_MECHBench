import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with multiple roots and chaotic behavior
        poly_term = np.sum(x_norm**8) + 0.3 * np.sum(x_norm**6) + 0.1 * np.sum(x_norm**4)
        
        # Trigonometric terms with chaotic tent map interactions
        trig_term = 0.0
        for i in range(self.dim):
            # Chaotic tent map inspired interaction
            tent_val = 1.0 - 2.0 * np.abs(x_norm[i] - 0.5)
            trig_term += (np.sin(15 * np.pi * x_norm[i]) * np.cos(10 * np.pi * x_norm[i]) + 
                         0.5 * np.sin(8 * np.pi * x_norm[i])**2 * np.cos(6 * np.pi * x_norm[i]) +
                         0.3 * tent_val * np.sin(12 * np.pi * x_norm[i]))
        
        # Radial basis function component with chaotic centers
        rbf_term = 0.0
        # Use chaotic sequence for center placement
        centers = np.array([np.sin(np.pi * i * 1.618) for i in range(self.dim)])
        for i in range(self.dim):
            rbf_term += np.exp(-7.0 * (x_norm[i] - centers[i])**2) + \
                       0.4 * np.exp(-4.0 * (x_norm[i] + centers[i])**2) + \
                       0.2 * np.exp(-6.0 * (x_norm[i] - 0.3 * centers[i])**2)
        
        # Cross-dimensional coupling with chaotic interaction strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction scope
                # Chaotic strength modulation
                strength = 0.6 * (1 + np.sin(np.pi * (i + j) * 1.618))
                cross_term += strength * np.sin(8 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[j])
        
        # Asymmetric penalty term with chaotic modification
        asym_term = 0.0
        for i in range(self.dim):
            # Chaotic asymmetry
            asym_factor = 1.0 + 0.5 * np.sin(np.pi * i * 1.618)
            asym_term += asym_factor * ((x_norm[i] - 0.2)**4 + 0.3 * (x_norm[i] + 0.3)**3)
        
        # Combine all terms with different weights
        result = 0.9 * poly_term + 0.7 * trig_term + 0.5 * rbf_term + 0.3 * cross_term + 0.4 * asym_term
        
        return result