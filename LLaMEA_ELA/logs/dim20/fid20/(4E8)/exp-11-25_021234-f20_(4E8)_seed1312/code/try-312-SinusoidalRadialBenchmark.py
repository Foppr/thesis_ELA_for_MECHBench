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
            freq = 3.0 + 0.4 * np.sin(0.5 * i)
            amp = 1.5 + 0.3 * np.cos(0.6 * i)
            f1 += amp * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Radial basis function components with adaptive widths and centers
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            center = 2.0 * np.sin(0.7 * i)
            width = 1.0 + 0.15 * np.cos(0.5 * i)
            f2 += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Cross-dimensional coupling with varying interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.7 + 0.25 * np.sin(0.4 * (i + j))
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                f3 += strength * interaction * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                
        # Adaptive conditioning based on radial distance
        f4 = 0.0
        for i in range(self.dim):
            cond_factor = 1.3 + 0.7 * np.sin(0.3 * r + 0.2 * i)
            f4 += cond_factor * x[i]**4
            
        # Multi-scale harmonic interactions with phase modulation
        f5 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.6 * i + 0.3 * r)
            f5 += np.sin(3.0 * x[i] + phase) * np.cos(4.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Boundary repulsion with exponential scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                penalty = 3.0 * dist**3.0 * np.exp(-0.3 * dist)
                f6 += penalty
                
        # Fractal-like self-similarity terms with recursive structure
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.7 + 0.2 * np.sin(0.4 * i + 0.2 * r)
            f7 += scale * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Time-varying coupling with dynamic weights
        f8 = 0.0
        for i in range(self.dim):
            weight = 2.0 + 0.4 * np.cos(0.4 * i + 0.3 * r)
            f8 += weight * x[i]**3 * np.exp(-0.15 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8