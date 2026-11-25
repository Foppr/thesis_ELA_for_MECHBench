import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.logistic_r = 3.9 + 0.1 * np.sin(0.5 * self.t)
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient components with logistic map dynamics
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map driven chaotic modulation
            chaos_factor = 1.0 + 0.3 * np.sin(2.0 * self.t + i * 0.7) * np.cos(1.5 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Periodic attractor landscape with time-varying frequencies
        freq_mod = 1.0 + 0.2 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * (xi**2) * np.cos(freq_mod * xi + 0.3 * self.t)
            
        # Dynamic curvature with time-varying Hessian effects
        curv_factor = 0.8 + 0.4 * np.sin(1.2 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/4.0)
            
        # Saddle point configuration with coupled variables
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.3 * (xi**2 - xj**2) * np.sin(0.5 * (xi + xj))
                
        # Multi-scale periodicity with phase coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * np.sin(10.0 * xi + 0.1 * self.t) * np.cos(3.0 * xi + 0.2 * self.t)
            
        # Adaptive basin depth with time-dependent scaling
        scale_factor = 1.5 + 0.5 * np.sin(0.6 * self.t)
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/2.0))
        
        # Coupled logistic dynamics in the landscape
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.1 * logistic_val * np.sin(2.0 * xi + 0.4 * self.t)
            
        # Oscillating harmonic components
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * (xi**2) * np.sin(7.0 * xi + 0.3 * self.t) * np.cos(4.0 * xi + 0.1 * self.t)
            
        return result