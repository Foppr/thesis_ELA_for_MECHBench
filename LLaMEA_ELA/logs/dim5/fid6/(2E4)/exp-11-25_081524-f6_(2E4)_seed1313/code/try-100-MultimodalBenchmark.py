import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive conditioning
        rbfs = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            rbfs += np.exp(-0.5 * dist / (1.0 + 0.1 * np.abs(x[i])))
        
        # Cross-dimensional exponential coupling with varying strengths
        exp_coupling = 0.0
        for i in range(self.dim-1):
            exp_coupling += np.exp(-0.2 * np.abs(x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2)
        
        # Dynamic global skewness mechanism
        skewness = 0.0
        for i in range(self.dim):
            skewness += (x[i]**3) * np.sin(0.5 * self.dim + x[i])
        
        # Polynomial ridge structures with dynamic exponents
        ridges = 0.0
        for i in range(self.dim-1):
            ridges += (np.abs(x[i] - x[i+1])**(2.0 + 0.3 * np.sin(i))) * (1.0 + 0.2 * np.cos(x[i]))
        
        # Adaptive sinusoidal modulation with frequency scaling
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(3.0 * x[i] + 0.5 * self.dim) * np.cos(2.0 * x[i])
        
        # Dimensionality-dependent scaling factor
        dim_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return (rbfs + exp_coupling + skewness + ridges + sin_mod) * dim_scale