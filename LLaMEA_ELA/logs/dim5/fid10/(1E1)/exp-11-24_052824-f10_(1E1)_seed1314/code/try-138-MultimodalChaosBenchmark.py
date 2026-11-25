import numpy as np

class MultimodalChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaos generation
        self.chaos_factors = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Clip input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying centers and widths
        rbf = 0.0
        centers = np.linspace(-4, 4, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if i < len(centers) else x[np.random.randint(0, len(x))]
            width = 0.5 + 0.5 * np.sin(i)
            rbf += np.exp(-width * np.sum((x - center)**2))
        
        # Trigonometric chaos component with adaptive frequencies
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(self.chaos_factors[i] * x[i])
            trig_chaos += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive conditioning component (conditioning changes based on x values)
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.abs(x[i])
            conditioning += cond_factor * x[i]**4
        
        # Coupled sine-wave interference pattern
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interference += np.sin(3 * x[i] + 2 * x[j]) * np.cos(x[i] - x[j])
        
        # Asymmetric saddle with multiple wells
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**2 * np.exp(-0.5 * x[i]**2)
        
        # High-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10 * x[i]) * np.cos(5 * x[i]) * (1 + 0.3 * np.sin(x[i]))
        
        # Combine all components with different weights
        return (0.2 * rbf + 
                0.3 * trig_chaos + 
                0.25 * conditioning + 
                0.15 * interference + 
                0.1 * saddle + 
                0.05 * high_freq + 
                0.05 * np.sum(x**6))