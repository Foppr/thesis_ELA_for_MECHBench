import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial decay component with varying exponents
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r**3.2 * np.exp(-0.1 * r)
        
        # High-frequency trigonometric waves in each dimension
        wave_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 + 15.0 * np.sin(i * 0.7)
            wave_term += np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Cross-dimensional interaction terms with asymmetric coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            cross_term += (xi**2 + xj**2) * np.sin(5.0 * xi * xj) * np.cos(3.0 * xi - xj)
        
        # Clustered global minima with localized perturbations
        cluster_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple local minima locations
            centers = [2.5, -2.5, 0.0]
            min_dist = float('inf')
            for center in centers:
                dist = np.abs(xi - center)
                if dist < min_dist:
                    min_dist = dist
            cluster_term += min_dist**2.5
        
        # Asymmetric saddle points with exponential modulation
        saddle_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            saddle_term += np.exp(-0.5 * xi**2) * np.sin(10.0 * xi) * np.cos(7.0 * xi)
        
        # Add noise-like perturbations with fractal-like scaling
        noise_term = 0.05 * np.sum(np.sin(50.0 * x) * np.cos(30.0 * x))
        
        return radial_term + wave_term + cross_term + cluster_term + saddle_term + noise_term