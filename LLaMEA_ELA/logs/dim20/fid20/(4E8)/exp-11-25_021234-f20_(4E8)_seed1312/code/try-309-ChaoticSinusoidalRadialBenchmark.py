import numpy as np

class ChaoticSinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave components with tent map modulation
        f1 = 0.0
        for i in range(self.dim):
            chaos_factor = 1.0 + 0.3 * np.sin(2.0 * np.pi * np.mod(i * 0.618, 1.0))
            freq = 3.0 + 0.5 * np.sin(0.7 * i) * chaos_factor
            amp = 1.5 + 0.4 * np.cos(0.8 * i) * chaos_factor
            phase = 0.5 * np.sin(0.9 * i + 0.3 * np.sum(x))
            f1 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.15 * x[i]**2)
            
        # Adaptive radial basis with chaotic center placement
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * i + 0.2 * r) * np.cos(0.3 * i)
            width = 1.0 + 0.2 * np.sin(0.6 * i + 0.1 * r)
            f2 += np.exp(-0.5 * ((x[i] - center) / width)**2)
            
        # Dynamic cross-dimensional coupling with chaotic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.8 + 0.4 * np.sin(0.5 * (i + j) + 0.2 * r)
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                f3 += weight * interaction
                
        # Fractal-like conditioning with recursive harmonic scaling
        f4 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.4 * i + 0.1 * r) * np.cos(0.3 * r)
            f4 += scale * x[i]**6 * np.exp(-0.2 * x[i]**2)
            
        # Time-varying harmonic modulation with chaotic phase shifts
        f5 = 0.0
        for i in range(self.dim):
            phase = 0.8 * np.sin(0.6 * i + 0.4 * r) * np.cos(0.3 * i)
            f5 += np.sin(3.0 * x[i] + phase) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Boundary repulsion with chaotic scaling
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.2:
                dist = np.abs(x[i]) - 4.2
                penalty = 3.0 * dist**2.5 * np.exp(-0.3 * dist)
                f6 += penalty
                
        # Multi-scale chaotic self-similarity terms
        f7 = 0.0
        for i in range(self.dim):
            scale = 0.8 + 0.3 * np.sin(0.5 * i + 0.2 * r) * np.cos(0.4 * r)
            f7 += scale * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Dynamic coupling with adaptive weights and chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            weight = 2.0 + 0.5 * np.sin(0.7 * i + 0.3 * r) * np.cos(0.2 * r)
            f8 += weight * x[i]**4 * np.exp(-0.15 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8