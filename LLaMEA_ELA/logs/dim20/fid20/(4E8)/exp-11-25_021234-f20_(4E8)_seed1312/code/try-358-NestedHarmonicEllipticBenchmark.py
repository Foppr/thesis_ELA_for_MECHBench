import numpy as np

class NestedHarmonicEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested harmonic oscillations with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 2.0 * np.cos(0.3 * i)
            f1 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Adaptive elliptic conditioning with dynamic eccentricity
        f2 = 0.0
        for i in range(self.dim):
            eccentricity = 0.5 + 1.5 * np.sin(0.4 * i)
            f2 += (x[i]**2) / (1.0 + eccentricity * np.cos(0.3 * x[i])**2)
            
        # Chaotic phase modulation with logistic map dynamics
        f3 = 0.0
        for i in range(self.dim):
            r = 3.5 + 0.5 * np.sin(0.6 * i)
            phase_mod = r * np.sin(x[i]) * (1 - np.sin(x[i])**2)
            f3 += np.cos(phase_mod) * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional coupling with nested interaction terms
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 1.0 + 0.8 * np.sin(0.3 * (i + j))
                    coupling = coupling_strength * np.sin(x[i] * x[j])
                    coupling_sum += coupling
            f4 += coupling_sum * np.exp(-0.05 * x[i]**2)
            
        # Multi-scale harmonic nesting with recursive structure
        f5 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(0.7 * i)
            f5 += scale_factor * np.sin(np.pi * x[i] / (1.0 + 0.4 * np.sum(x**2)))**3
            
        # Boundary-sensitive harmonic interactions
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_amp = 1.5 + 0.5 * np.cos(0.5 * i)
                f6 += boundary_amp * np.exp(-0.2 * (np.abs(x[i]) - 4.0)**2)
                
        # Resonant elliptic components with time-varying parameters
        f7 = 0.0
        for i in range(self.dim):
            freq_mod = 1.5 + 2.0 * np.sin(0.4 * i)
            eccentricity_mod = 0.3 + 1.2 * np.cos(0.3 * i)
            f7 += (x[i]**2) / (1.0 + eccentricity_mod * np.sin(freq_mod * x[i])**2)
            
        # Adaptive polynomial interactions with nested structure
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.8 + 0.4 * np.cos(0.5 * (i - j))
                interaction = x[i]**2 * x[j]**3
                f8 += coeff * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Fractal-like harmonic nesting with recursive frequency modulation
        f9 = 0.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.7 * np.sin(0.8 * i + 0.3 * np.sum(x**2))
            f9 += np.sin(freq_factor * x[i]) * np.cos(freq_factor * x[i])
            
        # Multi-modal chaotic oscillations with elliptic coupling
        f10 = 0.0
        for i in range(self.dim):
            r = 3.8 + 0.2 * np.cos(0.4 * i)
            chaotic_term = r * np.sin(x[i]) * (1 - np.sin(x[i])**2)
            f10 += chaotic_term * np.exp(-0.1 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10