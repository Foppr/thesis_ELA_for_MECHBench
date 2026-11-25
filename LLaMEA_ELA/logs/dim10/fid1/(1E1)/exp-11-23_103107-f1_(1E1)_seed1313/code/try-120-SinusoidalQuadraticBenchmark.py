import numpy as np

class SinusoidalQuadraticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                           (1 + 0.5 * np.sin(0.5 * np.pi * x)**2))
        
        # Polynomial penalty terms with different degrees and centers
        polynomial_penalty = 0
        for i in range(self.dim):
            xi = x[i]
            polynomial_penalty += 0.1 * xi**4 + 0.3 * xi**3 - 0.5 * xi**2 + 2 * xi + 1
        
        # Cross-dimensional quadratic interactions with coupling coefficients
        cross_quadratic = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_quadratic += 0.5 * (x[i] - x[j])**2 * np.sin(0.1 * (x[i] + x[j])**2)
                
        # Combined exponential and trigonometric penalty with multiple local minima
        combined_penalty = 0
        for i in range(self.dim):
            dist_from_center = abs(x[i] - 2.5)
            combined_penalty += np.exp(-0.1 * dist_from_center**2) * \
                              np.sin(4 * np.pi * dist_from_center)**2 + \
                              0.5 * np.exp(-0.05 * (dist_from_center - 1.5)**2) * \
                              np.cos(2 * np.pi * dist_from_center)**2
        
        # Global scaling and combination of all components
        return 1.2 * (sinusoidal + polynomial_penalty + cross_quadratic + combined_penalty)