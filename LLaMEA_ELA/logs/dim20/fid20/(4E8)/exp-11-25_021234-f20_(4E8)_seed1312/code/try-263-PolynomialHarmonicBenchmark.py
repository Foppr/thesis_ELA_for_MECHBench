import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Modified polynomial potential terms with altered degrees
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**2 + 0.7 * x[i]**4 + 0.3 * x[i]**6) * np.exp(-0.15 * x[i]**2)
            
        # Radial harmonic interactions with modified weights
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.4 * np.sin(0.25 * i + 0.15 * r)
            f2 += weight * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i])
            
        # Cross-dimensional coupling with modified interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.9 + 0.3 * np.sin(0.2 * (i + j) + 0.25 * r)
                interaction = x[i]**2 * x[j] + x[i] * x[j]**2
                f3 += coupling_strength * interaction * np.exp(-0.07 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms with modified scaling
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                scale = 1.3 + 0.4 * np.sin(0.35 * i + 0.25 * r)
                penalty = scale * (5.0 - np.abs(x[i]))**3
                f4 += penalty * np.exp(-0.12 * x[i]**2)
                
        # Multi-scale chaotic modulation with modified decay
        f5 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.9 * np.sin(0.55 * i + 0.35 * r) * np.cos(0.45 * i + 0.25 * r)
            f5 += chaos_factor * x[i]**3 * np.exp(-0.1 * x[i]**2)
            
        # Fractal-like cross-dimensional interactions with modified sine modulation
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 0.8 + 0.2 * np.sin(0.3 * (i - j) + 0.35 * r)
                f6 += mod * np.sin(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Time-varying harmonic terms with modified phase shifts
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.sin(0.15 * i + 0.45 * r)
            freq = 2.5 + 2.5 * np.cos(0.15 * i + 0.25 * r)
            f7 += np.sin(freq * x[i] + phase_shift) * np.exp(-0.07 * x[i]**2)
            
        # Enhanced quartic cross-terms with modified coefficients
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 0.6 + 0.4 * np.sin(0.15 * (i + j) + 0.35 * r)
                f8 += time_coeff * x[i]**4 * x[j]**2 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with modified penalties
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 2.2 * (5.0 - np.abs(x[i]))**4
                f9 += penalty * np.exp(-0.18 * x[i]**2)
                
        # Adaptive radial conditioning with modified complexity
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.7 * np.sin(0.25 * i + 0.15 * r)
            freq = 4.0 + 2.0 * np.cos(0.15 * i + 0.08 * r)
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.04 * r**2)
            
        # Cross-dimensional coupling with modified weights
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.3 * np.cos(0.25 * (i - j) + 0.35 * r)
                f11 += weight * x[i]**3 * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11