import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_norm**2)
        
        # Nested harmonic oscillations with varying frequencies
        harmonic1 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        harmonic2 = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(16 * np.pi * x_norm))
        harmonic3 = np.sum(np.sin(32 * np.pi * x_norm) * np.cos(64 * np.pi * x_norm))
        
        # Polynomial interactions with dynamic exponents
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 * x_norm[j]**2 + x_norm[i]**2 * x_norm[j]**3)
        
        # Dynamic radial basis functions with time-varying widths
        rbf_sum = 0.0
        for i in range(self.dim):
            # Varying widths based on dimension index
            width = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            rbf_sum += np.exp(-width * x_norm[i]**2)
        
        # Chaotic saddle point component using sine-cosine coupling
        saddle = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                saddle += np.sin(x_norm[i]) * np.cos(x_norm[i+1]) * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2)
        
        # Sharp transition regions using sigmoidal functions
        transition = 0.0
        for i in range(self.dim):
            transition += 1.0 / (1.0 + np.exp(-10 * (x_norm[i] - 0.5)))
            transition += 1.0 / (1.0 + np.exp(10 * (x_norm[i] + 0.5)))
        
        # Combined with exponential decay and oscillatory terms
        exponential = np.sum(np.exp(-0.5 * x_norm**2) - 1.0)
        oscillatory = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Weighted combination of all components
        return (0.2 * quadratic + 
                0.25 * harmonic1 + 
                0.2 * harmonic2 + 
                0.15 * harmonic3 + 
                0.1 * poly_interaction + 
                0.1 * rbf_sum + 
                0.08 * saddle + 
                0.05 * transition + 
                0.03 * exponential + 
                0.02 * oscillatory + 
                noise)