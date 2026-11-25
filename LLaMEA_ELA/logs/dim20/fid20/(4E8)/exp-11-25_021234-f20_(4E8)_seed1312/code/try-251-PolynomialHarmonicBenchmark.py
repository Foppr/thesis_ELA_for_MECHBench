import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**2 + 0.5 * x[i]**4 + 0.2 * x[i]**6) * np.exp(-0.1 * x[i]**2)
            
        # Radial harmonic interactions with time-varying weights
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.3 * np.sin(0.2 * i + 0.1 * r)
            f2 += weight * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional coupling with varying interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.4 * np.sin(0.15 * (i + j) + 0.2 * r)
                interaction = x[i]**2 * x[j] + x[i] * x[j]**2
                f3 += coupling_strength * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms with adaptive scaling
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                scale = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * r)
                penalty = scale * (5.0 - np.abs(x[i]))**3
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale chaotic modulation with exponential decay
        f5 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.8 * np.sin(0.5 * i + 0.3 * r) * np.cos(0.4 * i + 0.2 * r)
            f5 += chaos_factor * x[i]**3 * np.exp(-0.08 * x[i]**2)
            
        # Fractal-like cross-dimensional interactions with sine modulation
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 0.7 + 0.3 * np.sin(0.25 * (i - j) + 0.3 * r)
                f6 += mod * np.sin(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Time-varying harmonic terms with dynamic phase shifts
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.1 * i + 0.4 * r)
            freq = 2.0 + 3.0 * np.cos(0.1 * i + 0.2 * r)
            f7 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.06 * x[i]**2)
            
        # Enhanced quartic cross-terms with time-varying coefficients
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 0.5 + 0.5 * np.sin(0.1 * (i + j) + 0.3 * r)
                f8 += time_coeff * x[i]**4 * x[j]**2 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with polynomial penalties
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**4
                f9 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Adaptive radial conditioning with enhanced complexity
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.8 * np.sin(0.2 * i + 0.1 * r)
            freq = 3.5 + 2.5 * np.cos(0.1 * i + 0.05 * r)
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.03 * r**2)
            
        # Cross-dimensional coupling with modified weights
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.cos(0.2 * (i - j) + 0.3 * r)
                f11 += weight * x[i]**3 * x[j] * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11