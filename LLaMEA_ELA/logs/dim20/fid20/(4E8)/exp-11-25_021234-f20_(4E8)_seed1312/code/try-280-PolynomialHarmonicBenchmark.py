import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potential terms with higher degrees and modified coefficients
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**4 + 0.4 * x[i]**6 + 0.15 * x[i]**8) * np.exp(-0.2 * x[i]**2)
            
        # Radial harmonic interactions with dynamic weights and phase shifts
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            weight = 1.5 + 0.3 * np.sin(0.4 * i + 0.2 * r)
            phase = 0.3 * np.cos(0.2 * i + 0.1 * r)
            f2 += weight * np.sin(3.0 * x[i] + phase) * np.cos(2.0 * x[i] + phase)
            
        # Cross-dimensional coupling with adaptive interaction strengths and novel terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 1.0 + 0.4 * np.sin(0.3 * (i + j) + 0.3 * r)
                interaction = x[i]**2 * x[j]**2 + x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
                f3 += coupling_strength * interaction * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms with enhanced penalties and modified scaling
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                scale = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * r)
                penalty = scale * (5.0 - np.abs(x[i]))**3.0
                f4 += penalty * np.exp(-0.15 * x[i]**2)
                
        # Multi-scale chaotic modulation with increased complexity and altered decay
        f5 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.2 + 0.8 * np.sin(0.5 * i + 0.3 * r) * np.cos(0.4 * i + 0.2 * r)
            f5 += chaos_factor * x[i]**5 * np.exp(-0.12 * x[i]**2)
            
        # Fractal-like cross-dimensional interactions with modified sine modulation and additional terms
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                mod = 0.7 + 0.3 * np.sin(0.4 * (i - j) + 0.3 * r)
                f6 += mod * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Time-varying harmonic terms with enhanced phase shifts and frequencies
        f7 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.2 * i + 0.4 * r)
            freq = 3.0 + 1.5 * np.cos(0.2 * i + 0.3 * r)
            f7 += np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] + phase_shift) * np.exp(-0.1 * x[i]**2)
            
        # Enhanced quartic cross-terms with modified coefficients and additional nonlinearity
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                time_coeff = 0.7 + 0.3 * np.sin(0.2 * (i + j) + 0.4 * r)
                f8 += time_coeff * x[i]**2 * x[j]**4 * np.exp(-0.09 * (x[i]**2 + x[j]**2))
                
        # Additional boundary repulsion with stronger penalties and modified structure
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 2.0 * (5.0 - np.abs(x[i]))**4.0
                f9 += penalty * np.exp(-0.2 * x[i]**2)
                
        # Adaptive radial conditioning with enhanced complexity and modified structure
        f10 = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.6 * np.sin(0.3 * i + 0.2 * r)
            freq = 3.5 + 1.8 * np.cos(0.2 * i + 0.1 * r)
            f10 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * r**2)
            
        # Cross-dimensional coupling with updated weights and enhanced interaction terms
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.6 + 0.4 * np.cos(0.3 * (i - j) + 0.4 * r)
                f11 += weight * x[i]**3 * x[j]**2 * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11