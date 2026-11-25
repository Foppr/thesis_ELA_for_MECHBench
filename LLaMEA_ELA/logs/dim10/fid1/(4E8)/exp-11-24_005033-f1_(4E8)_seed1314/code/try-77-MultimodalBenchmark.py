import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal-like recursive component with nested oscillations
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Modified nested sine-cosine recursive pattern
            nested_term = np.sin(12 * xi) * np.cos(18 * xi) + 0.6 * np.sin(24 * xi) * np.cos(30 * xi)
            result += nested_term * np.exp(-0.12 * xi**2)
        
        # Modified dynamic elliptic conditioning with dimension-dependent scaling
        elliptic = 0.0
        for i in range(self.dim):
            # Adaptive elliptic shape based on dimension index with modified factor
            scale_factor = 1.0 + 0.6 * np.sin(0.6 * i)
            elliptic += scale_factor * (x[i]**2 + 0.15 * x[i]**4)
        result += 0.35 * elliptic
        
        # Altered cross-dimensional coupling with recursive interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified fractal-like coupling pattern with quartic terms
                coupling += (np.sin(6 * x[i]) * np.cos(6 * x[j]) + 
                           0.4 * np.sin(12 * x[i]) * np.cos(12 * x[j]) + 
                           0.2 * (x[i]**4) * (x[j]**4)) * \
                           np.exp(-0.06 * (x[i] - x[j])**2)
        result += 0.25 * coupling
        
        # Adaptive gradient modulation with multi-scale noise
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale noise components with altered frequencies
            noise += 0.12 * np.sin(60 * x[i]) + 0.06 * np.sin(120 * x[i]) + 0.03 * np.sin(240 * x[i])
        result += noise
        
        # Add a global scaling factor that depends on the number of dimensions
        result *= (1.0 + 0.12 * self.dim)
        
        return result