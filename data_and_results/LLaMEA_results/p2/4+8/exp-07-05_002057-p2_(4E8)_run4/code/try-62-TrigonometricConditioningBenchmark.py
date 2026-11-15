import numpy as np

class TrigonometricConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.freqs = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic trigonometric component
        trig_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.freqs[i]
            amp = self.amplitudes[i]
            trig_component += amp * np.sin(freq * xi) * np.cos(freq * xi)
        
        # Adaptive conditioning with exponential scaling
        cond_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            cond_factor = self.conditioning_factors[i]
            cond_component += cond_factor * np.exp(0.1 * xi**2) * xi**4
        
        # Cross-dimensional interaction with saddle points
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_component += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
        
        # Quadratic basin with global minimum at origin
        quadratic = np.sum(x**2) / self.dim
        
        # Combine components with varying weights
        result = 0.25 * trig_component + 0.3 * cond_component + 0.25 * cross_component + 0.2 * quadratic
        
        return result