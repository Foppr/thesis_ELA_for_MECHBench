import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with dynamic centers
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            center = 2.0 * np.sin(0.5 * self.t + i * 0.3)
            result += np.exp(-0.5 * ((xi - center) / 1.5)**2) * (1.0 + 0.3 * np.sin(3.0 * self.t + i))
            
        # Harmonic interference with time-varying amplitudes
        amp_mod = 1.0 + 0.5 * np.sin(2.0 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += amp_mod * np.sin(4.0 * xi + 0.3 * self.t) * np.cos(2.0 * xi + 0.2 * self.t)
            
        # Cross-dimensional coupling with varying strength
        coupling_strength = 0.8 + 0.4 * np.sin(1.5 * self.t)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += coupling_strength * np.sin(0.5 * (xi + xj)) * np.cos(0.3 * (xi - xj))
                
        # Multi-scale periodicity with dynamic frequencies
        freq_mod = 1.0 + 0.6 * np.sin(1.2 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * np.sin(freq_mod * xi + 0.4 * self.t) * np.cos(freq_mod * xi + 0.3 * self.t)
            
        # Saddle point configuration with time-varying topology
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                result += 0.3 * (xi**2 - xj**2) * np.sin(0.8 * (xi + xj) + 0.1 * self.t)
                
        # Enhanced basin structure with varying depths
        for i in range(self.dim):
            xi = x[i]
            result += 0.2 * (xi**4 - 2*xi**2) * np.exp(-xi**2/2.0) * (1.0 + 0.2 * np.sin(2.5 * self.t))
            
        # Additional chaotic modulation with polynomial terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * xi**3 * np.sin(6.0 * xi + 0.2 * self.t) * (1.0 + 0.1 * np.cos(3.0 * self.t))
            
        # Complex interaction terms with dynamic phase shifts
        for i in range(self.dim):
            xi = x[i]
            result += 0.15 * np.sin(5.0 * xi + 0.25 * self.t) * np.cos(4.0 * xi + 0.3 * self.t) * np.exp(-xi**2/3.0)
            
        # Increased nonlinearity with time-varying exponents
        exp_mod = 1.5 + 0.3 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            xi = x[i]
            result += 0.25 * (xi**exp_mod) * np.sin(3.0 * xi + 0.1 * self.t)
            
        # Cross-dimensional harmonic coupling with phase modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                result += 0.08 * np.sin(0.3 * (xi + xj) + 0.2 * self.t) * np.cos(0.4 * (xi - xj) + 0.15 * self.t)
                
        return result