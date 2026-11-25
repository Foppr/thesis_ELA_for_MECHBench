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
            chaos_factor = 1.0 + 0.8 * np.sin(3.5 * self.t + i * 1.5) * np.cos(2.0 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Improved periodic attractor landscape with stronger frequency coupling
        freq_mod = 1.0 + 0.6 * np.sin(1.5 * self.t)  # Slight frequency change
        for i in range(self.dim):
            xi = x[i]
            result += 1.0 * (xi**2) * np.cos(freq_mod * xi + 0.6 * self.t)
            
        # Enhanced dynamic curvature with stronger time-varying effects
        curv_factor = 1.0 + 0.7 * np.sin(2.5 * self.t)  # Slight frequency change
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/2.0)
            
        # Strengthened saddle point configuration with more complex coupling
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.8 * (xi**2 - xj**2) * np.sin(1.1 * (xi + xj))  # Slight change
                
        # Enhanced multi-scale periodicity with stronger phase coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.6 * np.sin(16.0 * xi + 0.25 * self.t) * np.cos(6.0 * xi + 0.35 * self.t)  # Changed frequencies
            
        # Refined basin depth with more controlled scaling
        scale_factor = 1.8 + 0.9 * np.sin(1.1 * self.t)  # Slight change
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/1.0))
        
        # Enhanced coupled logistic dynamics in the landscape
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.2 * logistic_val * np.sin(3.5 * xi + 0.6 * self.t)  # Slight change
            
        # Strengthened oscillating harmonic components
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**2) * np.sin(12.0 * xi + 0.5 * self.t) * np.cos(6.0 * xi + 0.3 * self.t)  # Changed frequencies
            
        # Additional harmonic interference terms for increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(7.0 * xi + 0.3 * self.t) * np.cos(3.0 * xi + 0.2 * self.t)  # Changed frequencies
            
        # Mutation: Slight adjustment to curvature and interaction terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * (xi**4 - 2*xi**2) * np.sin(4.0 * xi + 0.2 * self.t)  # Slight change
            
        # Mutation: Reduced coupling strength in harmonic interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * np.sin(6.0 * xi + 0.3 * self.t) * np.cos(2.5 * xi + 0.2 * self.t)  # Changed frequencies
            
        # Additional chaotic interference terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(22.0 * xi + 0.35 * self.t) * np.cos(9.0 * xi + 0.25 * self.t)  # Changed frequencies
            
        # Enhanced multi-modal structure with stronger local minima
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**6 - 3*xi**4 + 3*xi**2) * np.exp(-xi**2/3.8)  # Slight change
            
        # Increased dimensionality coupling with cross-terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.07 * (xi**2 + xj**2) * np.sin(0.4 * (xi - xj))  # Slight change
                
        # Novel perturbation terms for increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.05 * np.sin(18.0 * xi + 0.4 * self.t) * np.cos(7.5 * xi + 0.3 * self.t) * np.exp(-xi**2/5.0)
            
        # Additional higher-order interaction terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.08 * (xi**5 - 2*xi**3 + xi) * np.sin(2.5 * xi + 0.1 * self.t) * np.cos(4.0 * xi + 0.2 * self.t)
            
        # Increased nonlinearity with modified exponential decay
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * (xi**3 - xi) * np.exp(-xi**2/1.8)
            
        return result