import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave components with tent map modulation and enhanced nonlinearity
        f1 = 0.0
        for i in range(self.dim):
            freq = 4.0 + 1.2 * np.sin(0.8 * i + 0.4 * np.sin(0.6 * i))
            amp = 2.0 + 0.5 * np.cos(0.7 * i + 0.3 * np.cos(0.5 * i))
            phase = 0.6 * np.sin(0.9 * i + 0.5 * np.tan(0.4 * i))
            f1 += amp * np.sin(freq * x[i] + phase) * np.exp(-0.2 * x[i]**2)
            
        # Dynamic radial basis functions with chaotic centers, widths and increased complexity
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            center = 2.5 * np.sin(0.8 * i + 0.4 * np.cos(0.6 * r))
            width = 1.3 + 0.3 * np.cos(0.7 * i + 0.5 * np.sin(0.4 * r))
            f2 += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + 0.2 * np.sin(0.5 * r))
            
        # Adaptive cross-dimensional couplings with chaotic interaction strengths and higher-order terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 1.0 + 0.4 * np.sin(0.5 * (i + j) + 0.3 * np.cos(0.4 * r))
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                f3 += strength * interaction * (1.0 + 0.1 * np.sin(0.3 * r))
                
        # Time-varying conditioning with chaotic modulation and higher-order polynomial terms
        f4 = 0.0
        for i in range(self.dim):
            cond_factor = 2.0 + 1.0 * np.sin(0.4 * r + 0.3 * np.cos(0.5 * i))
            f4 += cond_factor * x[i]**5
            
        # Multi-scale fractal-like oscillations with recursive harmonic structure and enhanced complexity
        f5 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(0.7 * i + 0.5 * np.cos(0.6 * r))
            phase = 0.4 * np.sin(0.8 * i + 0.3 * np.tan(0.5 * r))
            f5 += scale * np.sin(6.0 * x[i] + phase) * np.cos(5.0 * x[i]) * np.exp(-0.25 * x[i]**2)
            
        # Boundary repulsion with chaotic exponential scaling and increased penalty
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                dist = np.abs(x[i]) - 4.0
                penalty = 4.0 * dist**4.0 * np.exp(-0.4 * dist)
                f6 += penalty
                
        # Chaotic self-similarity terms with dynamic scaling factors and enhanced complexity
        f7 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.9 * i + 0.4 * np.cos(0.7 * r))
            f7 += scale * np.sin(7.0 * x[i]) * np.cos(4.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Dynamic coupling with time-varying weights and chaotic modulation, increased nonlinearity
        f8 = 0.0
        for i in range(self.dim):
            weight = 2.5 + 0.6 * np.cos(0.6 * i + 0.4 * np.sin(0.5 * r))
            f8 += weight * x[i]**3.5 * np.exp(-0.2 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8