import numpy as np

class PolynomialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potentials with varying degrees
        f1 = 0.0
        for i in range(self.dim):
            f1 += (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial harmonic interactions with dynamic frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * i + 0.1 * r)
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional coupling with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.4 * np.sin(0.3 * (i + j) + 0.1 * r)
                f3 += weight * x[i]**2 * x[j]**2 * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction with fractal scaling
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                scale = 1.0 + 0.3 * np.sin(0.4 * i + 0.2 * r)
                f4 += scale * dist**2 * np.exp(-0.1 * dist)
                
        # Time-varying weights with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.8 * np.sin(0.5 * i + 0.2 * r + np.pi/4)
            f5 += weight * x[i]**3 * np.exp(-0.04 * x[i]**2)
            
        # Enhanced harmonic interactions with dynamic phase shifts
        f6 = 0.0
        for i in range(self.dim):
            phase = 0.3 * i + 0.1 * r
            f6 += np.sin(x[i] * (1.0 + 0.3 * np.cos(phase))) * np.exp(-0.06 * x[i]**2)
            
        # Quartic cross-terms with adaptive coefficients
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.5 + 0.5 * np.sin(0.2 * (i - j) + 0.1 * r)
                f7 += coeff * x[i]**2 * x[j]**2 * np.sin(x[i] * x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                
        # Adaptive radial conditioning with exponential scaling
        f8 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(0.3 * i + 0.15 * r)
            f8 += scale * np.cos(x[i] * (1.0 + 0.2 * np.sin(0.1 * x[i]))) * np.exp(-0.04 * x[i]**2)
            
        # Multi-scale fractal-like interactions
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 0.7 + 0.3 * np.sin(0.25 * (i - j) + 0.1 * r)
                f9 += scale * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation for complexity
        f10 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.6 * np.sin(0.7 * i + 0.2 * r + np.pi/3)
            f10 += x[i]**4 * np.exp(-0.03 * x[i]**2) * chaos_factor
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10