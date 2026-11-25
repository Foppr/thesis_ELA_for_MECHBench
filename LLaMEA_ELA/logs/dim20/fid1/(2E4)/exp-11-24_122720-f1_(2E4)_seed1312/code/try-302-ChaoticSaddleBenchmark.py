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
            exponent = 1.0 + 0.7 * np.sin(i * np.pi / (self.dim + 1))  # Increased variation
            fractal += np.abs(x[i])**exponent
            
        # Adaptive ridge structure that changes based on coordinate values
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Create adaptive ridge with non-linear response
            ridge = strength * (np.exp(-x[i]**2) + 0.7 * np.sin(x[i]))  # Increased sine contribution
            ridges += ridge
            
        # Cross-dimension interaction with fractal scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-scaled interaction terms with modified frequency
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                interaction += scale_factor * np.sin(1.5 * x[i] * x[j]) * np.cos(1.2 * (x[i] + x[j]))  # Modified frequencies
                
        # Combine all components with dynamic weighting
        result = 1.8 * chaotic + 1.2 * fractal + 1.0 * ridges + 0.4 * interaction  # Increased weights for challenge
        
        # Add dimensionality-dependent modulation
        dim_modulation = np.log(self.dim + 1) * 0.15  # Slightly increased modulation
        result *= (1.0 + dim_modulation)
        
        return result