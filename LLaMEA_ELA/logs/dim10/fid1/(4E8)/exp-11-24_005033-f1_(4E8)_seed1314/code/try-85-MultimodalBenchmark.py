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
            nested_term = (np.sin(15 * xi) * np.cos(20 * xi) + 
                          0.7 * np.sin(30 * xi) * np.cos(40 * xi) + 
                          0.4 * np.sin(45 * xi) * np.cos(60 * xi) +
                          0.2 * np.sin(75 * xi) * np.cos(90 * xi))
            result += nested_term * np.exp(-0.2 * xi**2)
        
        # Dynamic elliptic conditioning with dimension-dependent scaling
        elliptic = 0.0
        for i in range(self.dim):
            # Enhanced adaptive elliptic shape with quadratic and quartic scaling
            scale_factor = 1.0 + 0.8 * np.sin(0.4 * i) + 0.4 * np.cos(0.8 * i) + 0.2 * np.sin(1.2 * i)**2
            elliptic += scale_factor * (x[i]**2 + 0.2 * x[i]**4 + 0.05 * x[i]**6)
        result += 0.5 * elliptic
        
        # Cross-dimensional coupling with recursive interaction and higher-order quartic terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced fractal-like coupling pattern with quartic and quintic interactions
                coupling += (np.sin(8 * x[i]) * np.cos(8 * x[j]) + 
                           0.5 * np.sin(16 * x[i]) * np.cos(16 * x[j]) + 
                           0.3 * (x[i]**4) * (x[j]**4) +
                           0.1 * (x[i]**5) * (x[j]**5)) * \
                           np.exp(-0.05 * (x[i] - x[j])**2)
        result += 0.4 * coupling
        
        # Adaptive gradient modulation with multi-scale noise and chaotic elements
        noise = 0.0
        for i in range(self.dim):
            # Enhanced multi-scale noise components with chaotic sine terms and additional harmonics
            noise += 0.2 * np.sin(80 * x[i]) + 0.12 * np.sin(160 * x[i]) + 0.08 * np.sin(320 * x[i]) + 0.05 * np.sin(640 * x[i]) + 0.03 * np.sin(1280 * x[i])
        result += noise
        
        # Add a global scaling factor that depends on the number of dimensions
        result *= (1.0 + 0.2 * self.dim)
        
        return result