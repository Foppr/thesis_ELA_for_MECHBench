import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map constants for chaotic behavior
        self.r_values = np.linspace(3.6, 4.0, dim)
        # Fractional Brownian motion scaling factors
        self.hurst = 0.3 + np.random.rand(dim) * 0.4
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested logistic map chaos component with varying parameters
        chaos = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize chaotic sequence with random start
            xi = np.random.rand()
            # Let it settle to attractor
            for _ in range(20):  
                xi = r * xi * (1 - xi)
            # Compute chaotic contribution using fractional scaling
            for _ in range(10):
                xi = r * xi * (1 - xi)
            chaos += xi * (1 + 0.1 * np.sin(i * 2 * np.pi / self.dim))
        
        # Fractional Brownian motion-like wave interference
        wave = 0.0
        for i in range(self.dim):
            h = self.hurst[i]
            # Generate fractional noise component
            freq = 2**(i % 4 + 1)  # Varying frequencies
            wave += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i] / 2.0)
            wave += np.sin(freq * np.pi * x_norm[i] / 3.0) * np.cos(freq * np.pi * x_norm[i])
        
        # Saddle-point polynomial coupling with multi-scale terms
        poly = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale polynomial with saddle points
            poly += (xi**5 - 2*xi**3 + xi) * (1 + 0.2 * np.cos(5 * xi))
            
        # Cross-dimensional coupling using nested trigonometric products
        coupling = 1.0
        for i in range(self.dim):
            term = np.sin(np.pi * x_norm[i] / 2.0) * np.cos(np.pi * x_norm[i] / 3.0)
            coupling *= (1 + 0.1 * term)
            
        # Exponential modulation with multi-scale decay
        exp_mod = 0.0
        for i in range(self.dim):
            scale = 2**(i % 3 + 1)  # Multi-scale exponential decay
            exp_mod += np.exp(-scale * x_norm[i]**2) * np.sin(scale * x_norm[i])
            
        # Additional chaotic modulation using golden ratio
        phi = (1 + np.sqrt(5)) / 2
        modulator = np.sum(np.sin(phi * x_norm) + np.cos(phi * x_norm))
        
        # Combine all components with varying weights and scaling
        result = (0.3 * chaos + 
                 0.3 * wave + 
                 0.2 * poly + 
                 0.1 * coupling + 
                 0.05 * exp_mod + 
                 0.05 * modulator)
        
        # Add a global shift to increase difficulty
        return result + 2.5 * np.sin(np.sum(x_norm**2) / self.dim)