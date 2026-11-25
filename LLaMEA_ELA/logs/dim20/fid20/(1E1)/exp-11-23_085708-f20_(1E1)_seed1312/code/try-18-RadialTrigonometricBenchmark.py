import numpy as np

class RadialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf_sum += self.widths[i] * np.exp(-0.5 * np.sum(diff**2))
            
        # Periodic trigonometric component
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += np.sin(x[i]) + 0.5 * np.cos(2 * x[i]) + 0.3 * np.sin(3 * x[i])
            
        # Adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.5 * np.sin(i)
            cond_sum += condition_factor * x[i]**2
            
        # Cross-term coupling with varying interaction strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.1 + 0.2 * np.sin(i * j)
                cross_sum += strength * x[i] * x[j]
                
        # Global scaling and offset
        return rbf_sum + trig_sum + cond_sum + cross_sum + 5.0