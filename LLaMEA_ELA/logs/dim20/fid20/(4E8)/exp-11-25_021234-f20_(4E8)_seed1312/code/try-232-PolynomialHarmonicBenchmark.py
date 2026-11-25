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
            # Higher degree polynomial terms with sinusoidal modulation
            degree = 2 + int(3 * np.sin(0.3 * i))
            coeff = 1.0 + 0.5 * np.cos(0.2 * i)
            f1 += coeff * (x[i] ** degree) * np.exp(-0.1 * np.abs(x[i]))
            
        # Radial harmonic interactions with dynamic frequencies
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            for i in range(self.dim):
                freq = 1.0 + 2.0 * np.sin(0.2 * i + 0.1 * r)
                f2 += np.sin(freq * x[i]) / (1.0 + 0.1 * r**2)
                
        # Cross-dimensional coupling with time-varying weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying weight based on radial distance
                weight = 1.0 + 0.5 * np.sin(0.1 * (i + j) + 0.2 * r)
                coupling = weight * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                f3 += coupling
                
        # Boundary attraction terms with varying strengths
        f4 = 0.0
        for i in range(self.dim):
            # Attraction towards the center with exponential decay
            dist_to_boundary = min(np.abs(x[i]) - 4.0, 0.0)
            strength = 2.0 + np.sin(0.3 * i) * np.cos(0.1 * r)
            f4 += strength * dist_to_boundary**2 * np.exp(-0.2 * x[i]**2)
            
        # Multi-scale sinusoidal modulations with different frequencies
        f5 = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 3.0, 4.0]
            for freq in freqs:
                f5 += np.sin(freq * x[i]) * np.exp(-0.03 * x[i]**2)
                
        # Adaptive polynomial terms with dynamic coefficients
        f6 = 0.0
        for i in range(self.dim):
            # Dynamic coefficient based on position and radial distance
            coeff = 1.5 + 0.8 * np.sin(0.2 * i + 0.1 * r) * np.cos(0.1 * x[i])
            f6 += coeff * x[i]**4 * np.exp(-0.02 * x[i]**2)
            
        # Cross-dimensional fractal-like interactions with exponential decay
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with exponentially decaying interaction
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f7 += interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Multi-frequency harmonic terms with complex phase shifts
        f8 = 0.0
        for i in range(self.dim):
            phases = [0.1 * i, 0.2 * i, 0.3 * i]
            for phase in phases:
                freq = 1.0 + np.sin(0.15 * i) * np.cos(0.1 * r)
                f8 += np.sin(freq * x[i] + phase) * np.exp(-0.04 * np.abs(x[i]))
                
        # Additional cubic terms with varying weights
        f9 = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(0.2 * i + 0.1 * r)
            f9 += weight * x[i]**3 * np.exp(-0.06 * x[i]**2)
            
        # Combined boundary and interior repulsion
        f10 = 0.0
        for i in range(self.dim):
            # Strong repulsion near boundaries
            if np.abs(x[i]) > 4.5:
                f10 += 3.0 * np.exp(-0.5 * (np.abs(x[i]) - 4.5)**2)
            else:
                # Mild attraction towards center
                f10 -= 0.5 * x[i]**2 * np.exp(-0.1 * x[i]**2)
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10