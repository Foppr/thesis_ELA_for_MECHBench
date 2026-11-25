import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        self.memory = np.zeros(dim)
        self.logistic_r = 3.9 + 0.1 * np.sin(0.5 * self.t)
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with memory effects
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Memory-dependent chaotic modulation
            mem_factor = 0.5 + 0.5 * np.sin(0.3 * self.t + i * 0.8 + self.memory[i])
            chaos_factor = 1.0 + 0.4 * np.sin(2.0 * self.t + i * 0.7) * np.cos(1.5 * self.t)
            result += (xi**2 - 4.0 * xi + 4.0) * chaos_factor * mem_factor
            
        # Multi-scale periodic attractor landscape with phase coupling
        freq_mod = 1.0 + 0.3 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * (xi**2) * np.cos(freq_mod * xi + 0.3 * self.t) * np.sin(0.4 * xi + 0.2 * self.t)
            
        # Dynamic curvature with time-varying Hessian effects and memory
        curv_factor = 0.8 + 0.4 * np.sin(1.2 * self.t) + 0.2 * np.cos(0.6 * self.t + self.memory[i] if i < len(self.memory) else 0)
        for i in range(self.dim):
            xi = x[i]
            result += curv_factor * (xi**3 - 3.0 * xi) * np.exp(-xi**2/4.0)
            
        # Complex saddle point configuration with multi-dimensional coupling
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                xi = x[i]
                xj = x[i+1]
                xk = x[i+2]
                result += 0.4 * (xi**2 - xj**2) * np.sin(0.5 * (xi + xj)) * np.cos(0.3 * xk)
                
        # Multi-scale periodicity with phase coupling and memory
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * np.sin(10.0 * xi + 0.1 * self.t) * np.cos(3.0 * xi + 0.2 * self.t) * np.sin(0.5 * self.t + i * 0.3)
            
        # Adaptive basin depth with time-dependent scaling and memory
        scale_factor = 1.5 + 0.5 * np.sin(0.6 * self.t) + 0.3 * np.cos(0.4 * self.t + self.memory[i] if i < len(self.memory) else 0)
        result += scale_factor * np.sum((x**4) * np.exp(-x**2/2.0))
        
        # Coupled logistic dynamics with memory and adaptive parameters
        for i in range(self.dim):
            xi = x[i]
            logistic_val = self.logistic_r * xi * (1.0 - xi)
            result += 0.12 * logistic_val * np.sin(2.0 * xi + 0.4 * self.t) * np.cos(0.2 * self.t + i * 0.1)
            
        # Oscillating harmonic components with multi-frequency coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.18 * (xi**2) * np.sin(7.0 * xi + 0.3 * self.t) * np.cos(4.0 * xi + 0.1 * self.t) * np.sin(0.5 * xi + 0.2 * self.t)
            
        # Cross-dimensional chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * x[i] * x[j] * np.sin(0.3 * (x[i] + x[j]) + 0.1 * self.t)
                
        # Memory update
        self.memory = 0.9 * self.memory + 0.1 * x
        
        return result