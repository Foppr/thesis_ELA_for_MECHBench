import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with asymmetric penalty
        r = np.sqrt(np.sum(x_norm**2))
        radial = r * (1 + 0.3 * np.sin(4 * np.pi * r) + 0.2 * np.cos(2 * np.pi * r))
        
        # Enhanced periodic lattice structure with cubic terms
        periodic = np.sum(np.sin(2 * np.pi * x_norm)**3 + np.cos(3 * np.pi * x_norm)**3)
        
        # Modified cross-dimensional interaction terms with higher-order coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i]**3 - x_norm[j]**3) * np.sin(x_norm[i] + x_norm[j])
        
        # Asymmetric cubic terms
        asym_cube = np.sum(np.where(x_norm > 0, x_norm**3, 0.3 * x_norm**3))
        
        # Additional quadratic interaction term
        quad_interaction = 0.5 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Add a global scaling factor and noise
        noise = 0.005 * np.random.random()
        
        return 1.5 * radial + 1.2 * periodic + 0.4 * cross_term + asym_cube + 0.3 * quad_interaction + noise