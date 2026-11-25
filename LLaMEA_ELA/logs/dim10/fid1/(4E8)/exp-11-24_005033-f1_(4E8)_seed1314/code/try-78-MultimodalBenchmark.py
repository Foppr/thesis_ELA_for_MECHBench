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
            # Enhanced nested sine-cosine recursive pattern with chaotic modulation
            nested_term = (np.sin(12 * xi) * np.cos(18 * xi) + 
                          0.6 * np.sin(24 * xi) * np.cos(30 * xi) + 
                          0.3 * np.sin(36 * xi) * np.cos(42 * xi))
            result += nested_term * np.exp(-0.15 * xi**2)
        
        # Dynamic elliptic conditioning with dimension-dependent scaling
        elliptic = 0.0
        for i in range(self.dim):
            # Enhanced adaptive elliptic shape with quadratic scaling
            scale_factor = 1.0 + 0.7 * np.sin(0.3 * i) + 0.3 * np.cos(0.7 * i)
            elliptic += scale_factor * (x[i]**2 + 0.15 * x[i]**4)
        result += 0.4 * elliptic
        
        # Cross-dimensional coupling with recursive interaction and quartic terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced fractal-like coupling pattern with quartic interactions
                coupling += (np.sin(6 * x[i]) * np.cos(6 * x[j]) + 
                           0.4 * np.sin(12 * x[i]) * np.cos(12 * x[j]) + 
                           0.2 * (x[i]**4) * (x[j]**4)) * \
                           np.exp(-0.03 * (x[i] - x[j])**2)
        result += 0.3 * coupling
        
        # Adaptive gradient modulation with multi-scale noise and chaotic elements
        noise = 0.0
        for i in range(self.dim):
            # Enhanced multi-scale noise components with chaotic sine terms
            noise += 0.15 * np.sin(60 * x[i]) + 0.08 * np.sin(120 * x[i]) + 0.04 * np.sin(240 * x[i]) + 0.02 * np.sin(480 * x[i])
        result += noise
        
        # Add a global scaling factor that depends on the number of dimensions
        result *= (1.0 + 0.15 * self.dim)
        
        return result