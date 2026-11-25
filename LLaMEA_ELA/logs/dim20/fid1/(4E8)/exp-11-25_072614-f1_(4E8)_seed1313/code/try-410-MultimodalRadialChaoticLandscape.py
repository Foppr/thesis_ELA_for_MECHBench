import numpy as np

class MultimodalRadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_params = np.random.rand(dim) * 10.0 + 1.0
        self.radial_params = np.random.rand(dim) * 5.0 + 1.0
        self.conditioning_params = np.random.rand(dim) * 2.0 + 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        radial_term = 0.0
        for i in range(self.dim):
            radial_term += self.radial_params[i] * np.exp(-0.5 * (x[i] / self.conditioning_params[i])**2)
            
        # Sinusoidal oscillation component
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(self.chaotic_params[i] * x[i]) * np.cos(0.5 * x[i])
            
        # Chaotic conditioning component
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += self.conditioning_params[i] * np.sin(x[i] * (1.0 + 0.1 * np.sin(i)))
            
        # Interconnected valleys and ridges
        valley_term = 0.0
        for i in range(self.dim):
            valley_term += np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            
        # Combine all components
        result = radial_term + sin_term + chaotic_term + valley_term
        
        return result