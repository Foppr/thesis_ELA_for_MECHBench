import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.logistic_r = 3.9 + 0.3 * np.sin(0.8 * self.t)
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with higher frequency modulation and nonlinearity
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.0 + 0.7 * np.sin(4.0 * self.t + i * 1.3) * np.cos(2.0 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Stronger periodic attractor with multi-frequency coupling and phase shifts
        freq_mod = 1.0 + 0.5 * np.sin(1.3 * self.t) * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 1.0 * (xi**2) * np.cos(freq_mod * xi + 0.6 * self.t)
            
        # Enhanced dynamic curvature with time-varying nonlinearity and higher-order terms
        curv_factor = 0.9 + 0.7 * np.sin(2.0 * self.t) * np.cos(1.0 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/2.0)
            
        # Complex saddle point configuration with higher-order coupling and phase interference
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.7 * (xi**2 - xj**2) * np.sin(0.9 * (xi + xj)) * np.cos(0.4 * (xi - xj))
                
        # Multi-scale periodicity with stronger phase coupling and additional harmonic components
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(18.0 * xi + 0.3 * self.t) * np.cos(6.0 * xi + 0.4 * self.t)
            
        # Refined basin depth with controlled scaling and additional harmonic terms
        scale_factor = 1.7 + 1.0 * np.sin(1.0 * self.t) * np.cos(0.7 * self.t)
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/1.0))
        
        # Enhanced coupled logistic dynamics with increased nonlinearity and temporal coupling
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.2 * logistic_val * np.sin(3.5 * xi + 0.6 * self.t)
            
        # Enhanced oscillating harmonic components with added interference and phase modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**2) * np.sin(12.0 * xi + 0.5 * self.t) * np.cos(6.0 * xi + 0.3 * self.t)
            
        # Additional harmonic interference terms with higher complexity and time-varying phases
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(8.0 * xi + 0.3 * self.t) * np.cos(4.0 * xi + 0.2 * self.t)
            
        # New high-order polynomial terms for increased complexity and chaotic behavior
        for i in range(self.dim):
            xi = x[i]
            result += 0.07 * (xi**5) * np.sin(2.5 * xi + 0.4 * self.t)
            
        # Cross-dimensional coupling with time-varying interaction strength and phase shifts
        cross_coupling = 0.4 + 0.3 * np.sin(1.5 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += cross_coupling * x[i] * x[j] * np.cos(0.6 * (x[i] + x[j]) + 0.15 * self.t)
                
        # Additional chaotic interference terms with exponential decay and phase modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.08 * np.exp(-xi**2/3.0) * np.sin(14.0 * xi + 0.2 * self.t)
            
        # Multi-dimensional harmonic interference with frequency modulation and amplitude control
        for i in range(self.dim):
            xi = x[i]
            result += 0.12 * np.cos(9.0 * xi + 0.35 * self.t) * np.sin(7.0 * xi + 0.25 * self.t)
            
        # Enhanced nonlinearity with polynomial interaction and adaptive scaling
        poly_factor = 1.2 + 0.6 * np.sin(1.4 * self.t)
        result += poly_factor * np.sum((x**6) * np.exp(-x**2/1.5))
        
        return result