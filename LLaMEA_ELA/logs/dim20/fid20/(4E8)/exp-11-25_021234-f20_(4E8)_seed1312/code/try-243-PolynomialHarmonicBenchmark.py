import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Modified polynomial potential terms with adaptive exponents
        f1 = 0.0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.3 * np.sin(0.2 * i + 0.1 * np.sum(x**2))
            f1 += (x[i]**(4 + exp_factor) + 0.6 * x[i]**3 + 0.3 * x[i]**2 + 0.15 * x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Radial harmonic interactions with dynamic frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.15 * i + 0.08 * r + 0.4 * np.sin(r) + 0.2 * np.cos(r))
            f2 += np.cos(freq * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional coupling with time-varying chaotic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.5 + 0.8 * np.sin(0.25 * (i - j) + 0.15 * r + 0.3 * np.cos(r) + 0.2 * np.sin(r))
                f3 += weight * x[i]**2 * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary attraction with adaptive penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                penalty = 1.5 * (np.abs(x[i]) - 4.2)**3 + 0.7 * np.sin(0.6 * x[i])
                f4 += penalty * np.exp(-0.08 * x[i]**2)
                
        # Multi-scale harmonic terms with adaptive amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.2 * np.sin(0.4 * i + 0.3 * r + 0.7 * np.cos(r) + 0.3 * np.sin(r))
            freq = 2.0 + 3.0 * np.cos(0.25 * i + 0.15 * r + 0.5 * np.sin(r) + 0.2 * np.cos(r))
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like cross-terms with adaptive decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f6 += term * np.exp(-0.04 * (x[i]**2 + x[j]**2) + 0.15 * np.sin(r))
                
        # Adaptive coupling with enhanced chaotic weights
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.6 * np.cos(0.2 * (i + j) + 0.25 * r + 0.4 * np.cos(r) + 0.3 * np.sin(r))
                f7 += weight * x[i] * x[j]**3 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Quadratic radial term with enhanced chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            f8 += (x[i]**2) * np.sin(0.7 * r + 0.15 * i + 0.3 * np.cos(r) + 0.2 * np.sin(r)) * np.exp(-0.03 * x[i]**2)
            
        # Multi-frequency sine-wave interactions with enhanced phases
        f9 = 0.0
        for i in range(self.dim):
            freqs = [1.5, 2.5, 3.5, 4.5]
            for freq in freqs:
                f9 += np.sin(freq * x[i] + 0.4 * np.sin(r) + 0.1 * np.cos(r)) * np.exp(-0.07 * x[i]**2)
                
        # Enhanced boundary repulsion with modified chaotic terms
        f10 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.8:
                f10 += np.exp(-0.3 * (np.abs(x[i]) - 4.8)**2) + 0.2 * np.sin(0.5 * x[i])
                
        # Modified cubic cross-terms with enhanced interaction strengths
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.8 + 0.4 * np.sin(0.25 * (i - j) + 0.6 * np.cos(r) + 0.3 * np.sin(r))
                f11 += strength * x[i]**3 * x[j]**2 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic coupling with refined chaotic phase shifts
        f12 = 0.0
        for i in range(self.dim):
            phase = 0.7 * np.cos(0.15 * i + 0.4 * r + 0.5 * np.sin(r) + 0.3 * np.cos(r))
            freq = 2.0 + 3.0 * np.sin(0.25 * i + 0.15 * r + 0.4 * np.cos(r) + 0.3 * np.sin(r))
            f12 += np.sin(freq * x[i] + phase) * np.exp(-0.08 * x[i]**2)
            
        # Enhanced chaotic quartic cross-terms
        f13 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = x[i]**4 * x[j]**2 + x[i]**2 * x[j]**4
                f13 += term * np.exp(-0.04 * (x[i]**2 + x[j]**2) + 0.25 * np.sin(r))
                
        # Enhanced radial harmonic with refined modulation
        f14 = 0.0
        for i in range(self.dim):
            f14 += np.sin(0.4 * r + 0.15 * i + 0.6 * np.cos(r) + 0.3 * np.sin(r)) * x[i]**2
        
        # Additional chaotic coupling with modified weights
        f15 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.7 + 0.5 * np.sin(0.3 * (i - j) + 0.2 * r + 0.4 * np.cos(r))
                f15 += weight * x[i]**2 * x[j]**3 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15