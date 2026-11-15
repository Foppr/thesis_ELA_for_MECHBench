import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3 + 0.4 * np.random.rand(dim)  # Varying Hurst parameters
        self.amplitudes = 2.0 + 3.0 * np.random.rand(dim)  # Random amplitudes
        self.frequencies = 1.0 + 2.0 * np.random.rand(dim)  # Random frequencies
        self.phase_shifts = 2 * np.pi * np.random.rand(dim)  # Random phases
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure
        fractal = 0.0
        for i in range(self.dim):
            # Create fractal-like behavior using fractional Brownian motion components
            scaled_x = x_norm[i] * self.frequencies[i]
            # Use sine and cosine with varying Hurst parameters for fractal behavior
            fractal += (self.amplitudes[i] * 
                       np.sin(scaled_x + self.phase_shifts[i]) * 
                       np.cos(scaled_x**2 + self.phase_shifts[i]) * 
                       np.exp(-self.hurst[i] * np.abs(scaled_x)))
        
        # Multi-scale ruggedness component
        ruggedness = 0.0
        for i in range(self.dim):
            # Add multiple frequency components to increase ruggedness
            ruggedness += np.sum([
                0.5 * np.sin(2**(j+1) * self.frequencies[i] * x_norm[i] + self.phase_shifts[i]) * 
                np.cos(2**(j+1) * self.frequencies[i] * x_norm[i]**2 + self.phase_shifts[i])
                for j in range(3)
            ])
        
        # Quadratic basin for convergence guidance
        quadratic = np.sum(x_norm**2)
        
        # Add scale-dependent noise for increased complexity
        noise = 0.05 * np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm) * 
                             np.exp(-0.1 * np.abs(x_norm)))
        
        return fractal + ruggedness + quadratic + noise