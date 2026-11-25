import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for stability
        self.fractal_dims = [0.5 + 0.3 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.noise_levels = [0.1 + 0.2 * np.cos(i * np.pi / (dim + 2)) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal geometric component using self-similar patterns
        fractal_term = 0
        for i in range(self.dim):
            # Self-similar pattern with varying dimensionality
            dim_factor = self.fractal_dims[i]
            fractal_term += (np.sin(x[i] ** (2 + dim_factor)) * 
                           np.cos(x[i] ** (1.5 + dim_factor)) * 
                           np.exp(-0.05 * abs(x[i])))
        
        # Adaptive noise injection with dynamic amplitude
        noise_term = 0
        for i in range(self.dim):
            # Inject noise that scales with problem dimensionality
            noise_amp = self.noise_levels[i] * (1.0 + 0.1 * np.sin(self.dim * np.pi / (i + 1)))
            noise_term += np.random.normal(0, noise_amp) * np.exp(-0.1 * x[i]**2)
        
        # Dynamic dimensionality scaling effect
        dim_scaling = 1.0 + 0.3 * np.sin(self.dim * np.pi / 4) * np.cos(self.dim * np.pi / 5)
        
        # Cross-dimensional interaction with fractal coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength based on dimension
                coupling_strength = 0.5 + 0.3 * np.sin((i+j) * np.pi / (self.dim + 1))
                cross_term += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Basin attraction component with multiple local minima
        basin_term = 0
        for i in range(self.dim):
            # Multiple attraction centers with varying strengths
            center1 = 2.0 * np.sin(i * np.pi / (self.dim + 3))
            center2 = -2.0 * np.cos(i * np.pi / (self.dim + 4))
            basin_term += ((x[i] - center1)**2 + (x[i] - center2)**2) * np.exp(-0.01 * abs(x[i]))
        
        # Global scaling and weighting
        weight1 = 0.3 + 0.1 * np.sin(self.dim * np.pi / 6)
        weight2 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 7)
        weight3 = 0.2 + 0.1 * np.sin(self.dim * np.pi / 8)
        weight4 = 0.25 + 0.1 * np.cos(self.dim * np.pi / 9)
        
        return (weight1 * fractal_term + 
                weight2 * noise_term + 
                weight3 * cross_term + 
                weight4 * basin_term) * dim_scaling