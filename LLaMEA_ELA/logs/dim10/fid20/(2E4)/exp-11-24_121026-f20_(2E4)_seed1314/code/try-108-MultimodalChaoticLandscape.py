import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic modulation
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            rbfs[i] = np.exp(-np.sum((x_norm - np.sin(i * np.pi / self.dim))**2))
        
        # Sinusoidal oscillation with chaotic frequency modulation
        sin_term = np.sum(np.sin(10 * x_norm + 0.5 * np.sin(3 * x_norm))**2)
        
        # Chaotic perturbation using tent map
        tent_map = np.zeros(self.dim)
        for i in range(self.dim):
            if x_norm[i] < 0.5:
                tent_map[i] = 2 * x_norm[i]
            else:
                tent_map[i] = 2 * (1 - x_norm[i])
        
        # Combined chaotic and radial component
        chaotic_radial = np.sum(rbfs * tent_map)
        
        # Polynomial interaction with trigonometric coupling
        poly_interaction = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm)**2)
        
        # Multi-scale sinusoidal modulation with chaotic amplitude
        multi_scale = np.sum(np.sin(15 * x_norm) * np.cos(7 * x_norm) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Cross-dimensional coupling with exponential decay
        cross_dim = 0.5 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Fractional power and logarithmic barrier
        fractional = np.sum(np.abs(x_norm)**1.3 * np.log(1 + np.abs(x_norm)))
        
        # Nested chaotic oscillation
        nested_osc = np.sum(np.sin(np.pi * x_norm * np.sin(2 * x_norm))**4)
        
        # Final combination with varying weights
        return (0.5 * np.sum(rbfs) + 
                0.3 * sin_term + 
                0.2 * chaotic_radial + 
                0.15 * poly_interaction + 
                0.1 * multi_scale + 
                0.08 * cross_dim + 
                0.05 * fractional + 
                0.1 * nested_osc)