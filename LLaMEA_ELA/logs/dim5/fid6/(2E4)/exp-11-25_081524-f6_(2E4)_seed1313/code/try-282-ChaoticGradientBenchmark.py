import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.logistic_r = 3.9 + 0.3 * np.sin(0.8 * self.t)
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with higher frequency modulation and increased nonlinearity
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaos_factor = 1.0 + 0.7 * np.sin(4.0 * self.t + i * 1.3) * np.cos(2.0 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor
            
        # Stronger periodic attractor with multi-frequency coupling and additional harmonic terms
        freq_mod = 1.0 + 0.5 * np.sin(1.3 * self.t) * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 1.0 * (xi**2) * np.cos(freq_mod * xi + 0.6 * self.t)
            
        # Enhanced dynamic curvature with time-varying nonlinearity and higher-order terms
        curv_factor = 0.9 + 0.7 * np.sin(2.0 * self.t) * np.cos(1.0 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/2.0)
            
        # Complex saddle point configuration with higher-order coupling and cross-dimensional terms
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.7 * (xi**2 - xj**2) * np.sin(0.9 * (xi + xj)) * np.cos(0.4 * (xi - xj))
                
        # Multi-scale periodicity with stronger phase coupling and additional interference
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(18.0 * xi + 0.3 * self.t) * np.cos(6.0 * xi + 0.4 * self.t)
            
        # Refined basin depth with controlled scaling, additional harmonic terms and higher-order polynomials
        scale_factor = 1.7 + 0.9 * np.sin(1.0 * self.t) * np.cos(0.7 * self.t)
        result += scale_factor * np.sum((x**5) * np.exp(-x**2/1.0))
        
        # Enhanced coupled logistic dynamics with increased nonlinearity and modified interaction
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.2 * logistic_val * np.sin(4.0 * xi + 0.6 * self.t)
            
        # Enhanced oscillating harmonic components with added interference and higher frequency terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * (xi**2) * np.sin(12.0 * xi + 0.5 * self.t) * np.cos(6.0 * xi + 0.3 * self.t)
            
        # Additional harmonic interference terms with higher complexity and modified frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(8.0 * xi + 0.3 * self.t) * np.cos(4.0 * xi + 0.2 * self.t)
            
        # New high-order polynomial terms for increased complexity and additional sinusoidal modulation
        for i in range(self.dim):
            xi = x[i]
            result += 0.08 * (xi**6) * np.sin(2.5 * xi + 0.4 * self.t)
            
        # Cross-dimensional coupling with time-varying interaction strength and additional harmonic terms
        cross_coupling = 0.4 + 0.3 * np.sin(1.5 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += cross_coupling * x[i] * x[j] * np.cos(0.6 * (x[i] + x[j]) + 0.15 * self.t)
                
        # Additional complex harmonic interference with higher frequency components
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * np.sin(20.0 * xi + 0.1 * self.t) * np.cos(8.0 * xi + 0.25 * self.t)
            
        return result