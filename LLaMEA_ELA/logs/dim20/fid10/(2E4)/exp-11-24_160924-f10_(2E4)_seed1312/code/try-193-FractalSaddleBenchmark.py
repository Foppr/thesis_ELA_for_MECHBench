import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        np.random.seed(42)
        self.scale_factors = np.random.uniform(0.5, 2.0, dim)
        self.fractal_dims = np.random.uniform(1.1, 1.9, dim)
        self.saddle_weights = np.random.uniform(-1.0, 1.0, dim)
        self.peak_positions = np.random.uniform(-3.0, 3.0, (dim, 5))
        self.peak_heights = np.random.uniform(1.0, 5.0, (dim, 5))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add multi-modal peak components with fractal scaling
        for i in range(self.dim):
            xi = x[i]
            scale = self.scale_factors[i]
            fractal_dim = self.fractal_dims[i]
            
            # Fractal-like peak structure
            peak_sum = 0.0
            for j in range(5):
                pos = self.peak_positions[i, j]
                height = self.peak_heights[i, j]
                # Multi-scale Gaussian peaks with fractal scaling
                peak_sum += height * np.exp(-scale * (xi - pos)**2 / (1.0 + 0.1 * fractal_dim * np.abs(xi - pos)))
            
            result += peak_sum
            
        # Add saddle point interactions
        for i in range(self.dim):
            xi = x[i]
            saddle_weight = self.saddle_weights[i]
            # Saddle point contribution with varying steepness
            result += saddle_weight * (xi**2 - 1.0)**2 * np.cos(0.5 * xi)
            
        # Add cross-dimensional fractal coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                # Fractal coupling with dimension-dependent scaling
                coupling = (1.0 + 0.3 * np.sin(0.2 * (i + j)))
                result += coupling * np.sin(xi * xj) * np.exp(-0.1 * (xi**2 + xj**2))
                
        # Add self-similar structure through recursive scaling
        if self.dim > 1:
            # Create a hierarchical fractal structure
            for k in range(1, min(4, self.dim + 1)):
                if self.dim >= k * 2:
                    # Use pairs of dimensions to create self-similarity
                    for i in range(0, self.dim - k*2 + 1, k):
                        xi, xj = x[i], x[i+k]
                        result += 0.5 * np.sin(xi + xj) * np.cos(xi - xj) * (1.0 + 0.2 * np.tanh(xi * xj))
                        
        # Add global fractal modulation
        fractal_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Scale-invariant modulation
            fractal_mod += np.sin(xi) * np.cos(0.5 * xi) * np.exp(-0.05 * xi**2)
            
        result += 0.3 * fractal_mod
        
        # Add asymmetry and final scaling
        asymmetry = np.sum(x**3) * 0.01
        result += asymmetry
        
        return result