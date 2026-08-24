import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute basis centers and weights for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.5, 2.0, 20)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with Gaussian kernels
        rbf = np.sum(self.weights * np.exp(-np.sum((x - self.centers)**2, axis=1) / (2 * 0.5**2)))
        
        # Trigonometric wave interference pattern with multiple frequencies
        wave = np.sum(np.sin(10 * x) * np.cos(8 * x) * np.sin(6 * x) * np.cos(4 * x) * np.sin(2 * x))
        
        # Adaptive dimension weighting based on input values
        dim_weights = np.abs(x) / (np.max(np.abs(x)) + 1e-8)
        dim_weighted = np.sum(dim_weights * x**2)
        
        # Cross-dimensional interaction with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i] - x[i+1])**4 * np.sin(15 * np.pi * x[i]) * np.cos(13 * np.pi * x[i+1])
        
        # Multi-scale periodic modulation with dynamic amplitude
        mod_term = np.sum(np.sin(25 * np.pi * x) * np.cos(23 * np.pi * x) * 
                         np.sin(21 * np.pi * x) * np.cos(19 * np.pi * x) * 
                         np.sin(17 * np.pi * x) * np.cos(15 * np.pi * x))
        
        # Add noise-like perturbations for increased ruggedness
        noise = np.sum(0.1 * np.sin(50 * x) * np.cos(48 * x))
        
        # Combine all components with optimized coefficients
        return 0.4 * rbf + 0.3 * wave + 0.2 * dim_weighted + 0.15 * cross_term + 0.25 * mod_term + 0.1 * noise + 3.0