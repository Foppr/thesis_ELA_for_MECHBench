import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Logarithmic spiral periodic terms with varying radii
        spiral_terms = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Spiral pattern with exponential growth
            spiral_terms += np.sin(xi * np.log(np.abs(xi) + 1e-6)) * np.cos(xi * np.exp(0.1 * xi))
        
        # Complex exponential coupling with adaptive weights
        exp_coupling = 0.0
        for i in range(self.dim - 1):
            exp_coupling += np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(x[i] * x[i+1])
        
        # Fractal-like self-similar structure using recursive sine-cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(np.pi * x[i]) * np.cos(np.pi * x[i]) * np.sin(2 * np.pi * x[i])
        
        # Adaptive noise component that scales with dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.01 * (i + 1)) * np.sin(x[i]**2)
        
        # Hyperbolic tangent interaction with polynomial decay
        hyperbolic = 0.0
        for i in range(self.dim):
            hyperbolic += np.tanh(x[i]) * (1.0 / (1.0 + np.exp(-0.1 * x[i]**2)))
        
        # Multi-scale oscillatory component with varying frequencies
        multi_freq = 0.0
        for i in range(self.dim):
            multi_freq += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.sin(2 * x[i])
        
        # Combine all terms
        result = result + 0.5 * spiral_terms + 0.3 * exp_coupling + 0.4 * fractal + 0.1 * noise + 0.2 * hyperbolic + 0.15 * multi_freq
        
        return result