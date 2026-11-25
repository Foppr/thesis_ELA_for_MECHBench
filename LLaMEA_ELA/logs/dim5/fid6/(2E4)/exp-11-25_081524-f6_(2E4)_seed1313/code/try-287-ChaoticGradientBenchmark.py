import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.logistic_r = 3.9 + 0.2 * np.sin(0.7 * self.t)
        
    def f(self, x):
        self.t += 0.015
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with higher frequency modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.0 + 0.6 * np.sin(3.0 * self.t + i * 1.1) * np.cos(1.5 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Stronger periodic attractor with multi-frequency coupling
        freq_mod = 1.0 + 0.4 * np.sin(1.1 * self.t) * np.cos(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.8 * (xi**2) * np.cos(freq_mod * xi + 0.5 * self.t)
            
        # Enhanced dynamic curvature with time-varying nonlinearity
        curv_factor = 0.8 + 0.6 * np.sin(1.8 * self.t) * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/2.5)
            
        # Complex saddle point configuration with higher-order coupling
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.6 * (xi**2 - xj**2) * np.sin(0.8 * (xi + xj)) * np.cos(0.3 * (xi - xj))
                
        # Multi-scale periodicity with stronger phase coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(15.0 * xi + 0.2 * self.t) * np.cos(5.0 * xi + 0.3 * self.t)
            
        # Refined basin depth with controlled scaling and additional harmonic terms
        scale_factor = 1.5 + 0.8 * np.sin(0.9 * self.t) * np.cos(0.6 * self.t)
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/1.2))
        
        # Enhanced coupled logistic dynamics with increased nonlinearity
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.15 * logistic_val * np.sin(3.0 * xi + 0.5 * self.t)
            
        # Enhanced oscillating harmonic components with added interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * (xi**2) * np.sin(10.0 * xi + 0.4 * self.t) * np.cos(5.0 * xi + 0.2 * self.t)
            
        # Additional harmonic interference terms with higher complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * np.sin(7.0 * xi + 0.25 * self.t) * np.cos(3.0 * xi + 0.15 * self.t)
            
        # New high-order polynomial terms for increased complexity
        for i in range(self.dim):
            xi = x[i]
            result += 0.05 * (xi**5) * np.sin(2.0 * xi + 0.3 * self.t)
            
        # Cross-dimensional coupling with time-varying interaction strength
        cross_coupling = 0.3 + 0.2 * np.sin(1.2 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += cross_coupling * x[i] * x[j] * np.cos(0.5 * (x[i] + x[j]) + 0.1 * self.t)
                
        # Additional chaotic modulation with exponential decay
        exp_decay = np.exp(-self.t/10.0)
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * exp_decay * np.sin(8.0 * xi + 0.6 * self.t) * np.cos(4.0 * xi + 0.4 * self.t)
            
        # Increased multi-modal interference with fractal-like structure
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * np.sin(20.0 * xi + 0.3 * self.t) * np.cos(10.0 * xi + 0.2 * self.t) * np.exp(-xi**2/5.0)
            
        # Adaptive basin structures with time-varying depth
        basin_depth = 1.0 + 0.5 * np.sin(2.0 * self.t) * np.cos(1.0 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += basin_depth * (xi**6) * np.exp(-xi**2/3.0)
            
        # Enhanced harmonic interference with complex phase coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * np.sin(12.0 * xi + 0.5 * self.t) * np.cos(6.0 * xi + 0.3 * self.t) * np.sin(3.0 * xi + 0.1 * self.t)
            
        return result