import numpy as np

class FractalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for different dimensions
        self.fractal_factors = [1.0 / (2 ** i) for i in range(10)]
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.01 * np.sum(x**2)
        
        # Fractal-like structure using recursive sine modulation
        f2 = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with varying frequency
            freq = 2.0 + 1.5 * np.sin(0.3 * i + np.sum(x) / self.dim)
            scale = 1.0 + 0.5 * np.cos(0.4 * i)
            f2 += scale * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Multi-resolution ruggedness with adaptive penalty
        f3 = 0.0
        for i in range(self.dim):
            # Adaptive scaling based on position
            adapt_scale = 1.0 + 0.3 * np.sin(0.5 * x[i])
            # Rugged component with multiple frequencies
            rugged = np.sum([np.sin((2**j) * x[i]) * (0.8 ** j) for j in range(1, 6)])
            f3 += adapt_scale * rugged * np.exp(-0.05 * np.abs(x[i]))
            
        # Geometric fractal terrain with self-similarity
        f4 = 0.0
        for i in range(self.dim):
            # Self-similar pattern using multiple scales
            pattern = 0.0
            for j, factor in enumerate(self.fractal_factors[:min(5, self.dim)]):
                pattern += factor * np.sin((2**(j+1)) * x[i])
            f4 += pattern * np.exp(-0.2 * x[i]**2)
            
        # Cross-dimensional interaction with chaotic coupling
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                if j < self.dim:
                    # Chaotic coupling strength
                    coupling = 0.5 + 0.3 * np.sin(0.2 * (i + j) + np.sum(x) / self.dim)
                    interaction = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                    f5 += coupling * interaction * np.exp(-0.1 * (x[i] - x[j])**2)
                    
        # Adaptive noise injection with fractal characteristics
        f6 = 0.0
        for i in range(self.dim):
            # Noise amplitude scales with dimensionality
            noise_amp = 0.5 * (1.0 + np.sin(0.3 * i + np.sum(x) / self.dim))
            # Fractal noise pattern
            fractal_noise = np.sum([np.sin((3**j) * x[i]) * (0.6 ** j) for j in range(1, 4)])
            f6 += noise_amp * fractal_noise
            
        # Global scaling with fractal dimensionality effect
        global_scale = 1.5 + 0.5 * np.sin(np.sum(x**2) / (self.dim * 10.0))
        
        return global_scale * (f1 + f2 + f3 + f4 + f5 + f6)