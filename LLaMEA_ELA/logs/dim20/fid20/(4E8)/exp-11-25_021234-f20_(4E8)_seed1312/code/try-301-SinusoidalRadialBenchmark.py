import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation terms with varying frequencies and amplitudes
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 0.3 * np.sin(0.4 * i)
            amp = 1.2 + 0.2 * np.cos(0.5 * i)
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Radial basis function components with adaptive widths and centers
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            center = 1.5 * np.sin(0.6 * i)
            width = 0.9 + 0.1 * np.cos(0.4 * i)
            f2 += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Cross-dimensional coupling with varying interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.6 + 0.2 * np.sin(0.3 * (i + j))
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f3 += strength * interaction * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Adaptive conditioning based on radial distance
        f4 = 0.0
        for i in range(self.dim):
            cond_factor = 1.2 + 0.6 * np.sin(0.25 * r + 0.15 * i)
            f4 += cond_factor * x[i]**4
            
        # Multi-scale harmonic interactions with phase modulation
        f5 = 0.0
        for i in range(self.dim):
            phase = 0.4 * np.sin(0.5 * i + 0.25 * r)
            f5 += np.sin(2.5 * x[i] + phase) * np.cos(3.5 * x[i]) * np.exp(-0.18 * x[i]**2)
            
        # Boundary repulsion with exponential scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                penalty = 2.5 * dist**3.0 * np.exp(-0.25 * dist)
                f6 += penalty
                
        # Fractal-like self-similarity terms with recursive structure
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.6 + 0.15 * np.sin(0.35 * i + 0.15 * r)
            f7 += scale * np.sin(4.5 * x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Time-varying coupling with dynamic weights
        f8 = 0.0
        for i in range(self.dim):
            weight = 1.7 + 0.3 * np.cos(0.35 * i + 0.25 * r)
            f8 += weight * x[i]**3 * np.exp(-0.12 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8