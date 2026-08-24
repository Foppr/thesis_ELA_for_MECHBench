import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(3.0 * x[i]) + 0.3 * np.sin(7.0 * x[i]) + 0.2 * np.sin(11.0 * x[i])
        
        # Radial basis function terms with varying centers and widths
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < self.dim:
                result += 0.8 * np.exp(-0.5 * ((x[i] - centers[i]) / 1.5)**2)
        
        # Asymmetric saddle point terms with cubic and quartic components
        for i in range(self.dim):
            result += 0.4 * x[i]**3 + 0.1 * x[i]**4
        
        # Cross-term interactions with cosine coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.cos(2.0 * (x[i] - x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add noise-like perturbations with chaotic-like behavior
        for i in range(self.dim):
            result += 0.1 * np.sin(13.0 * x[i]) * np.cos(9.0 * x[i]) + 0.05 * np.sin(27.0 * x[i])
        
        # Dimensionality scaling factor
        result *= (1.0 + 0.05 * self.dim)
        
        return result