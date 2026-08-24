import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-1, 1] for internal computations
        x_norm = x / 5.0
        
        # Base quadratic term
        base = np.sum(x_norm**2)
        
        # Add multiple sinusoidal components with different frequencies and phases
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)  # Varying frequencies
            phase = i * np.pi / 4
            sin_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        
        # Introduce chaotic behavior using a tent map
        chaotic = 0.0
        for i in range(self.dim):
            xi = (x[i] / 5.0) % 1.0
            if xi < 0.5:
                chaotic += 10 * xi
            else:
                chaotic += 10 * (1 - xi)
        
        # Create multiple nested global minima with varying depths
        minima = []
        for i in range(8):
            loc = np.array([(j % 2) * 2 - 1 for j in range(self.dim)]) * (i + 1) * 0.5
            minima.append(loc)
        
        # Penalty for being far from global minima
        penalty = 0.0
        for i, loc in enumerate(minima):
            dist = np.sum((x - loc)**2)
            penalty += np.exp(-dist / (2.0 * (i + 1)**2)) * (i + 1) * 0.1
        
        # Add a fractional Brownian motion-like component
        fbm = 0.0
        for i in range(self.dim):
            fbm += np.sin(20 * x[i]) * np.cos(10 * x[i]) * (1.0 / (1.0 + np.abs(x[i])))
        
        # Combine all components
        result = base + 0.5 * sin_term + 0.1 * chaotic + penalty + 0.05 * fbm
        
        # Add a complex interference pattern
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        result += 0.02 * interference
        
        return result