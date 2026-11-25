import numpy as np

class DynamicSaddleBenchmark:
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
            # Enhanced chaotic behavior with modified sine term and additional quadratic component
            chaotic += param * x[i] * (1 - x[i]**2) + 0.15 * np.sin(1.5 * x[i] * np.pi) + 0.05 * x[i]**2
            
        # Fractal basin component using fractional Brownian motion characteristics
        fractal = 0
        for i in range(self.dim):
            # Create more pronounced fractal behavior with varying exponents
            exponent = 1.2 + 0.8 * np.sin(i * np.pi / (self.dim + 1))
            fractal += np.abs(x[i])**exponent
            
        # Adaptive ridge structure that changes based on coordinate values
        ridges = 0
        for i in range(self.dim):
            strength = self.ridge_strength[i]
            # Enhanced ridge with additional cosine component and hyperbolic tangent
            ridge = strength * (np.exp(-x[i]**2) + 0.7 * np.sin(x[i]) + 0.3 * np.cos(2 * x[i]) + 0.1 * np.tanh(x[i]))
            ridges += ridge
            
        # Cross-dimension interaction with fractal scaling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified interaction with higher frequency terms and amplitude scaling
                scale_factor = (i + 1) * (j + 1) / (self.dim**2)
                interaction += scale_factor * np.sin(3.0 * x[i] * x[j]) * np.cos(2.0 * (x[i] + x[j])) * (1 + 0.3 * np.sin(i * j))
                
        # Add hyperbolic saddle term for increased non-smoothness
        saddle = 0
        for i in range(self.dim):
            saddle += 0.5 * np.abs(x[i]) * np.tanh(x[i])
            
        # Combine all components with adjusted weights
        result = 2.0 * chaotic + 1.5 * fractal + 1.2 * ridges + 0.6 * interaction + 0.8 * saddle
        
        # Add dimensionality-dependent modulation with improved scaling
        dim_modulation = np.log(self.dim + 1) * 0.2
        result *= (1.0 + dim_modulation)
        
        return result