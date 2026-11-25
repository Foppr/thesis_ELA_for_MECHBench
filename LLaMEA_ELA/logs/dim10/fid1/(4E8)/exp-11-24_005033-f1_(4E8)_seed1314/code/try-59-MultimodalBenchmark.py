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
            # Nested sine-cosine recursive pattern
            nested_term = np.sin(10 * xi) * np.cos(15 * xi) + 0.5 * np.sin(20 * xi) * np.cos(25 * xi)
            result += nested_term * np.exp(-0.1 * xi**2)
        
        # Dynamic elliptic conditioning with dimension-dependent scaling
        elliptic = 0.0
        for i in range(self.dim):
            # Adaptive elliptic shape based on dimension index
            scale_factor = 1.0 + 0.5 * np.sin(0.5 * i)
            elliptic += scale_factor * (x[i]**2 + 0.1 * x[i]**4)
        result += 0.3 * elliptic
        
        # Cross-dimensional coupling with recursive interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling pattern
                coupling += (np.sin(5 * x[i]) * np.cos(5 * x[j]) + 
                           0.3 * np.sin(10 * x[i]) * np.cos(10 * x[j])) * \
                           np.exp(-0.05 * (x[i] - x[j])**2)
        result += 0.2 * coupling
        
        # Adaptive gradient modulation with multi-scale noise
        noise = 0.0
        for i in range(self.dim):
            # Multi-scale noise components
            noise += 0.1 * np.sin(50 * x[i]) + 0.05 * np.sin(100 * x[i]) + 0.02 * np.sin(200 * x[i])
        result += noise
        
        # Add a global scaling factor that depends on the number of dimensions
        result *= (1.0 + 0.1 * self.dim)
        
        return result