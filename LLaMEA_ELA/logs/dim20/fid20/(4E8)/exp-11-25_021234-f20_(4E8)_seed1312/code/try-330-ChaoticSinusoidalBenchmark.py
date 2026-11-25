import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave components with tent map modulation
        f1 = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.7 * np.sin(0.6 * i + 0.2 * np.sin(0.4 * i))
            amp = 1.5 + 0.3 * np.cos(0.5 * i + 0.1 * np.cos(0.3 * i))
            phase = 0.4 * np.sin(0.7 * i + 0.3 * np.tan(0.2 * i))
            f1 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
            
        # Dynamic radial basis functions with chaotic centers and widths
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            center = 1.8 * np.sin(0.6 * i + 0.2 * np.cos(0.4 * r))
            width = 1.0 + 0.15 * np.cos(0.5 * i + 0.3 * np.sin(0.2 * r))
            f2 += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Adaptive cross-dimensional couplings with chaotic interaction strengths
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.7 + 0.25 * np.sin(0.3 * (i + j) + 0.15 * np.cos(0.2 * r))
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
                f3 += strength * interaction
                
        # Time-varying conditioning with chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            cond_factor = 1.3 + 0.6 * np.sin(0.2 * r + 0.15 * np.cos(0.3 * i))
            f4 += cond_factor * x[i]**4
            
        # Multi-scale fractal-like oscillations with recursive harmonic structure
        f5 = 0.0
        for i in range(self.dim):
            scale = 0.7 + 0.25 * np.sin(0.5 * i + 0.3 * np.cos(0.4 * r))
            phase = 0.2 * np.sin(0.6 * i + 0.15 * np.tan(0.3 * r))
            f5 += scale * np.sin(4.0 * x[i] + phase) * np.cos(3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Boundary repulsion with chaotic exponential scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                penalty = 2.5 * dist**3.0 * np.exp(-0.25 * dist)
                f6 += penalty
                
        # Chaotic self-similarity terms with dynamic scaling factors
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.8 + 0.2 * np.sin(0.7 * i + 0.25 * np.cos(0.5 * r))
            f7 += scale * np.sin(5.0 * x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Dynamic coupling with time-varying weights and chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            weight = 1.8 + 0.4 * np.cos(0.4 * i + 0.2 * np.sin(0.3 * r))
            f8 += weight * x[i]**3 * np.exp(-0.1 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8