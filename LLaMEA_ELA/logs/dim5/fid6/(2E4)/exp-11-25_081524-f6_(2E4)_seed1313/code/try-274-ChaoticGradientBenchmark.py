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
            # Enhanced chaotic modulation with stronger coupling
            chaos_factor = 1.0 + 0.4 * np.sin(2.5 * self.t + i * 0.8) * np.cos(1.2 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Improved periodic attractor landscape with stronger frequency coupling
        freq_mod = 1.0 + 0.3 * np.sin(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * (xi**2) * np.cos(freq_mod * xi + 0.4 * self.t)
            
        # Enhanced dynamic curvature with stronger time-varying effects
        curv_factor = 0.7 + 0.5 * np.sin(1.5 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/3.0)
            
        # Strengthened saddle point configuration with more complex coupling
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.4 * (xi**2 - xj**2) * np.sin(0.6 * (xi + xj))
                
        # Enhanced multi-scale periodicity with stronger phase coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.sin(12.0 * xi + 0.15 * self.t) * np.cos(4.0 * xi + 0.25 * self.t)
            
        # Refined basin depth with more controlled scaling
        scale_factor = 1.3 + 0.7 * np.sin(0.7 * self.t)
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/1.5))
        
        # Enhanced coupled logistic dynamics in the landscape
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.12 * logistic_val * np.sin(2.5 * xi + 0.45 * self.t)
            
        # Strengthened oscillating harmonic components
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * (xi**2) * np.sin(8.0 * xi + 0.35 * self.t) * np.cos(4.5 * xi + 0.15 * self.t)
            
        # Additional harmonic interference terms for increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.08 * np.sin(5.0 * xi + 0.2 * self.t) * np.cos(2.0 * xi + 0.1 * self.t)
            
        # Slight modification: reduced exponential decay rate and increased harmonic amplitude
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * (xi**4) * np.exp(-xi**2/2.0)  # Modified decay rate
            
        # Additional interaction term with altered coupling strength
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                xi = x[i]
                xj = x[i+1]
                xk = x[i+2]
                result += 0.25 * xi * xj * xk * np.sin(0.5 * (xi + xj + xk))  # New interaction
                
        return result