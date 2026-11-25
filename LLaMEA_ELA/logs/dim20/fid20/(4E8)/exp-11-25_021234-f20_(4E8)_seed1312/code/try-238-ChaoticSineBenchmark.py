import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave potential terms with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(0.3 * i + 0.1 * np.sum(x))
            amp = 1.0 + 0.5 * np.cos(0.2 * i)
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Radial cubic interactions with time-varying coefficients
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            for i in range(self.dim):
                coeff = 1.0 + 0.3 * np.sin(0.1 * i + 0.05 * r)
                f2 += coeff * x[i]**3 / (1.0 + 0.1 * r**2)
                
        # Cross-dimensional coupling with dynamic scaling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 + 0.4 * np.sin(0.2 * (i + j) + 0.1 * r)
                coupling = scale * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                f3 += coupling
                
        # Adaptive chaotic modulation with boundary effects
        f4 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.6 * np.sin(0.25 * i + 0.1 * r + 0.05 * np.sum(x**2))
            dist_to_center = np.abs(x[i])
            f4 += chaos_factor * dist_to_center**2 * np.exp(-0.2 * dist_to_center)
            
        # Multi-scale chaotic sine terms with varying phase shifts
        f5 = 0.0
        for i in range(self.dim):
            phases = [0.1 * i, 0.2 * i, 0.3 * i, 0.4 * i]
            for phase in phases:
                freq = 1.0 + np.sin(0.15 * i) * np.cos(0.1 * r)
                f5 += np.sin(freq * x[i] + phase) * np.exp(-0.03 * np.abs(x[i]))
                
        # Dynamic polynomial terms with chaotic coefficients
        f6 = 0.0
        for i in range(self.dim):
            coeff = 1.5 + 0.8 * np.sin(0.2 * i + 0.1 * r) * np.cos(0.1 * x[i])
            f6 += coeff * x[i]**4 * np.exp(-0.02 * x[i]**2)
            
        # Fractal-like chaotic interactions with exponential decay
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) + np.cos(x[i] + x[j])
                f7 += interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Boundary repulsion with chaotic scaling
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                repulsion = 2.0 * np.exp(-0.5 * (np.abs(x[i]) - 4.0)**2)
                f8 += repulsion
            else:
                attraction = 0.3 * x[i]**2 * np.exp(-0.1 * x[i]**2)
                f8 -= attraction
                
        # Additional chaotic harmonic terms with varying weights
        f9 = 0.0
        for i in range(self.dim):
            weight = 0.5 + 0.5 * np.sin(0.2 * i + 0.1 * r) * np.cos(0.1 * x[i])
            f9 += weight * x[i]**3 * np.exp(-0.06 * x[i]**2)
            
        # Complex cross-dimensional chaotic coupling
        f10 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 1.0 + 0.3 * np.sin(0.1 * (i + j) + 0.2 * r)
                coupling = coeff * x[i]**2 * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                f10 += coupling
                
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10