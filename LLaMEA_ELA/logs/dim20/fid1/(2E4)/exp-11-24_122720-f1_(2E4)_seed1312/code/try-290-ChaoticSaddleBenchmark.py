import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.chaos_params = [np.random.uniform(0.1, 0.9) for _ in range(dim)]
        self.ridge_strength = [np.random.uniform(0.5, 2.0) for _ in range(dim)]
        self.fractal_dim = 1.5 + np.random.rand() * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map-like dynamics
        chaotic = 0
        for i in range(self.dim):
            param = self.chaos_params[i]
            # Logistic map inspired term with chaotic behavior
            chaotic += param * x[i] * (1 - x[i]**2) + 0.1 * np.sin(x[i] * np.pi)
            
        # Fractal basin component using fractional Brownian motion characteristics
        fractal = 0
        for i in range(self.dim):
            # Create fractal-like behavior with varying exponents
            exponent = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            fractal += np.abs(x[i])**exponent
            
        # Adaptive ridge structure that changes based on coordinate values
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Create adaptive ridge with non-linear response
            ridge = strength * (np.exp(-x[i]**2) + 0.5 * np.sin(x[i]))
            ridges += ridge
            
        # Cross-dimension interaction with fractal scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-scaled interaction terms
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                interaction += scale_factor * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Combine all components with dynamic weighting
        result = 1.5 * chaotic + 1.0 * fractal + 0.8 * ridges + 0.3 * interaction
        
        # Add dimensionality-dependent modulation
        dim_modulation = np.log(self.dim + 1) * 0.1
        result *= (1.0 + dim_modulation)
        
        return result