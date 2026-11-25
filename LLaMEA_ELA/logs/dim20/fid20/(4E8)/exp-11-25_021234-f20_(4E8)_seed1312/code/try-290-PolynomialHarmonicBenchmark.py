import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with higher-order interactions
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**4 + 0.4 * x[i]**6 + 0.15 * x[i]**8) * np.exp(-0.2 * x[i]**2)
            
        # Radial harmonic interactions with dynamic weights and phase shifts
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.5 + 0.3 * np.sin(0.4 * i + 0.2 * r)
            phase = 0.5 * np.cos(0.3 * i + 0.2 * r)
            f2 += weight * np.sin(3.0 * x[i] + phase) * np.cos(2.0 * x[i])
            
        # Cross-dimensional coupling with fractal-like modulation and time-varying coefficients
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.1 + 0.4 * np.sin(0.25 * (i + j) + 0.3 * r)
                interaction = x[i]**4 * x[j] + x[i] * x[j]**4
                f3 += coupling_strength * interaction * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms with exponential scaling and modified penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                scale = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * r)
                penalty = scale * (5.0 - np.abs(x[i]))**3.0
                f4 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Multi-scale chaotic modulation with enhanced fractal properties
        f5 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.3 + 0.8 * np.sin(0.5 * i + 0.3 * r) * np.cos(0.4 * i + 0.2 * r)
            f5 += chaos_factor * x[i]**5 * np.exp(-0.15 * x[i]**2)
            
        # Fractal-like cross-dimensional interactions with sinusoidal modulation and dynamic frequency
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 0.7 + 0.5 * np.sin(0.4 * (i - j) + 0.3 * r)
                freq = 2.0 + 1.5 * np.cos(0.2 * (i + j) + 0.2 * r)
                f6 += mod * np.sin(freq * (x[i] + x[j])) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Time-varying harmonic terms with adaptive phase and frequency
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.2 * i + 0.4 * r)
            freq = 3.0 + 2.5 * np.cos(0.2 * i + 0.3 * r)
            f7 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.1 * x[i]**2)
            
        # Enhanced quartic cross-terms with modified coefficients and dynamic interaction
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 0.7 + 0.5 * np.sin(0.2 * (i + j) + 0.4 * r)
                f8 += time_coeff * x[i]**4 * x[j]**4 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with complex penalty functions
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.3:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**4.0
                f9 += penalty * np.exp(-0.2 * x[i]**2)
                
        # Adaptive radial conditioning with enhanced complexity and multi-scale modulation
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.8 * np.sin(0.3 * i + 0.2 * r)
            freq = 3.5 + 2.5 * np.cos(0.2 * i + 0.1 * r)
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.06 * r**2)
            
        # Cross-dimensional coupling with updated weights and higher-order interactions
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.6 * np.cos(0.3 * (i - j) + 0.4 * r)
                f11 += weight * x[i]**5 * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11