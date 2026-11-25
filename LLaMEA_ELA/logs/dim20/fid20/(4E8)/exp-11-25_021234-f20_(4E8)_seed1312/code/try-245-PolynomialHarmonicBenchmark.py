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
            degree = 2 + int(3 * np.sin(0.2 * i))
            f1 += x[i]**degree
            
        # Radial harmonic interactions with dynamic frequencies
        r = np.sqrt(np.sum(x**2))
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.1 * i + 0.05 * r)
            f2 += np.sin(freq * x[i]) * np.exp(-0.1 * r**2)
            
        # Cross-dimensional coupling with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.1 * (i + j) + 0.2 * r)
                f3 += weight * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Boundary attraction terms with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                f4 += dist**2 * np.exp(-0.5 * dist)
                
        # Multi-scale polynomial interactions with varying coefficients
        f5 = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.8 * np.sin(0.3 * i + 0.1 * r)
            f5 += coeff * x[i]**4 * np.exp(-0.03 * x[i]**2)
            
        # Fractal-like harmonic coupling with recursive structure
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 + 0.5 * np.sin(0.2 * (i - j))
                f6 += scale * np.cos(x[i] + x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                
        # Adaptive quartic terms with radial conditioning
        f7 = 0.0
        for i in range(self.dim):
            coeff = 1.5 + 0.5 * np.cos(0.15 * i + 0.1 * r)
            f7 += coeff * x[i]**4 * np.exp(-0.02 * r**2)
            
        # Mixed trigonometric and polynomial cross-terms
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += np.sin(x[i] * x[j]) * x[i]**2 * x[j]**2 * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Enhanced boundary repulsion with polynomial penalties
        f9 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                penalty = 3.0 * (5.0 - np.abs(x[i]))**3
                f9 += penalty * np.exp(-0.1 * x[i]**2)
                
        # Dynamic harmonic modulation with time-varying amplitudes
        f10 = 0.0
        for i in range(self.dim):
            amp = 2.0 + 1.0 * np.sin(0.2 * i + 0.3 * r + 0.5 * np.random.uniform(-1, 1))
            freq = 1.0 + 1.5 * np.cos(0.1 * i + 0.2 * np.random.uniform(-1, 1))
            f10 += amp * np.sin(freq * x[i]) * np.exp(-0.08 * x[i]**2)
            
        # Combined polynomial and harmonic terms with adaptive weights
        f11 = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.6 * np.sin(0.25 * i + 0.1 * r)
            f11 += weight * x[i]**3 * np.cos(x[i]) * np.exp(-0.04 * x[i]**2)
            
        # Cross-dimensional quartic interactions with dynamic coupling
        f12 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_weight = 0.8 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * r)
                f12 += dynamic_weight * x[i]**3 * x[j]**3 * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Additional chaotic modulation for increased complexity
        f13 = 0.0
        for i in range(self.dim):
            chaos_factor = 0.3 * np.sin(0.5 * i + 0.1 * r + np.pi/4)
            f13 += x[i]**2 * np.exp(-0.01 * x[i]**2) * chaos_factor
            
        # Hybrid coupling with sine and cosine components
        f14 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_term = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                f14 += hybrid_term * x[i]**2 * x[j]**2 * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14