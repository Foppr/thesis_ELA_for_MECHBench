import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential terms with varying degrees and chaotic modulation
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**4 + 0.6 * x[i]**3 + 0.25 * x[i]**2 + 0.12 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Radial harmonic interactions with chaotic frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 2.5 * np.sin(0.1 * i + 0.05 * r + 0.3 * np.sin(r))
            f2 += np.cos(freq * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional coupling with chaotic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.2 + 0.4 * np.sin(0.2 * (i - j) + 0.1 * r + 0.4 * np.cos(r))
                f3 += weight * x[i]**2 * x[j] * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction with enhanced penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 1.8 * (np.abs(x[i]) - 4.0)**3 + 0.6 * np.sin(0.5 * x[i])
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale harmonic terms with chaotic amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 1.6 + 0.7 * np.sin(0.3 * i + 0.2 * r + 0.6 * np.cos(r))
            freq = 1.2 + 1.8 * np.cos(0.2 * i + 0.1 * r + 0.4 * np.sin(r))
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Fractal-like cross-terms with chaotic decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f6 += term * np.exp(-0.03 * (x[i]**2 + x[j]**2) + 0.15 * np.sin(r))
                
        # Adaptive coupling with chaotic weights
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.9 + 0.3 * np.cos(0.15 * (i + j) + 0.2 * r + 0.3 * np.cos(r))
                f7 += weight * x[i] * x[j]**3 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Quadratic radial term with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            f8 += (x[i]**2) * np.sin(0.6 * r + 0.1 * i + 0.2 * np.cos(r)) * np.exp(-0.02 * x[i]**2)
            
        # Multi-frequency sine-wave interactions with chaotic phases
        f9 = 0.0
        for i in range(self.dim):
            freqs = [1.2, 2.2, 3.2, 4.2]
            for freq in freqs:
                f9 += np.sin(freq * x[i] + 0.35 * np.sin(r)) * np.exp(-0.06 * x[i]**2)
                
        # Enhanced boundary repulsion with chaotic terms
        f10 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                f10 += np.exp(-0.2 * (np.abs(x[i]) - 4.5)**2) + 0.12 * np.sin(0.4 * x[i])
                
        # Cubic cross-terms with chaotic interaction strengths
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.7 + 0.25 * np.sin(0.2 * (i - j) + 0.5 * np.cos(r))
                f11 += strength * x[i]**3 * x[j]**2 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic coupling with complex chaotic phase shifts
        f12 = 0.0
        for i in range(self.dim):
            phase = 0.6 * np.cos(0.1 * i + 0.3 * r + 0.4 * np.sin(r))
            freq = 1.7 + 2.3 * np.sin(0.2 * i + 0.1 * r + 0.3 * np.cos(r))
            f12 += np.sin(freq * x[i] + phase) * np.exp(-0.07 * x[i]**2)
            
        # Chaotic quartic cross-terms
        f13 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = x[i]**4 * x[j]**2 + x[i]**2 * x[j]**4
                f13 += term * np.exp(-0.03 * (x[i]**2 + x[j]**2) + 0.25 * np.sin(r))
                
        # Enhanced radial harmonic with chaotic modulation
        f14 = 0.0
        for i in range(self.dim):
            f14 += np.sin(0.35 * r + 0.1 * i + 0.5 * np.cos(r)) * x[i]**2
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14