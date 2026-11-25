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
            f1 += (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Radial harmonic interactions with time-varying frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.1 * i + 0.05 * r)
            f2 += np.cos(freq * x[i]) * np.exp(-0.03 * x[i]**2)
            
        # Cross-dimensional coupling with dynamic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin(0.2 * (i - j) + 0.1 * r)
                f3 += weight * x[i]**2 * x[j] * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction with polynomial penalties
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalty = 2.0 * (np.abs(x[i]) - 4.0)**3
                f4 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Multi-scale harmonic terms with varying amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.8 * np.sin(0.3 * i + 0.2 * r)
            freq = 1.0 + 2.0 * np.cos(0.2 * i + 0.1 * r)
            f5 += amp * np.sin(freq * x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Fractal-like cross-terms with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f6 += term * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Adaptive coupling with sinusoidal weights
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.4 * np.cos(0.15 * (i + j) + 0.2 * r)
                f7 += weight * x[i] * x[j]**3 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Quadratic radial term with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            f8 += (x[i]**2) * np.sin(0.5 * r + 0.1 * i) * np.exp(-0.02 * x[i]**2)
            
        # Multi-frequency sine-wave interactions
        f9 = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0]
            for freq in freqs:
                f9 += np.sin(freq * x[i]) * np.exp(-0.06 * x[i]**2)
                
        # Enhanced boundary repulsion with exponential terms
        f10 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                f10 += np.exp(-0.2 * (np.abs(x[i]) - 4.5)**2)
                
        # Cubic cross-terms with varying interaction strengths
        f11 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.6 + 0.3 * np.sin(0.2 * (i - j))
                f11 += strength * x[i]**3 * x[j]**2 * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic coupling with complex phase shifts
        f12 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.cos(0.1 * i + 0.3 * r)
            freq = 1.5 + 2.5 * np.sin(0.2 * i + 0.1 * r)
            f12 += np.sin(freq * x[i] + phase) * np.exp(-0.07 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12