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
        
        # Fractal-like structure using recursive sine modulation with enhanced complexity
        f2 = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with varying frequency and phase
            freq = 2.0 + 2.0 * np.sin(0.3 * i + np.sum(x) / self.dim)
            scale = 1.0 + 0.7 * np.cos(0.4 * i)
            f2 += scale * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Multi-resolution ruggedness with adaptive penalty and enhanced noise
        f3 = 0.0
        for i in range(self.dim):
            # Adaptive scaling based on position with enhanced variation
            adapt_scale = 1.0 + 0.4 * np.sin(0.5 * x[i] + 0.2 * np.sum(x))
            # Rugged component with multiple frequencies and enhanced complexity
            rugged = np.sum([np.sin((2**j) * x[i]) * (0.7 ** j) for j in range(1, 7)])
            f3 += adapt_scale * rugged * np.exp(-0.08 * np.abs(x[i]))
            
        # Geometric fractal terrain with self-similarity and enhanced interaction
        f4 = 0.0
        for i in range(self.dim):
            # Self-similar pattern using multiple scales with enhanced complexity
            pattern = 0.0
            for j, factor in enumerate(self.fractal_factors[:min(6, self.dim)]):
                pattern += factor * np.sin((2**(j+2)) * x[i])
            f4 += pattern * np.exp(-0.15 * x[i]**2)
            
        # Cross-dimensional interaction with enhanced chaotic coupling
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                if j < self.dim:
                    # Enhanced chaotic coupling strength with more complex interaction
                    coupling = 0.6 + 0.4 * np.sin(0.25 * (i + j) + np.sum(x) / self.dim)
                    interaction = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                    # Enhanced interaction with additional nonlinearity
                    interaction += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                    f5 += coupling * interaction * np.exp(-0.12 * (x[i] - x[j])**2)
                    
        # Adaptive noise injection with fractal characteristics and enhanced complexity
        f6 = 0.0
        for i in range(self.dim):
            # Noise amplitude scales with dimensionality and position
            noise_amp = 0.6 * (1.0 + np.sin(0.35 * i + np.sum(x) / self.dim + 0.1 * x[i]))
            # Fractal noise pattern with enhanced complexity
            fractal_noise = np.sum([np.sin((3**j) * x[i]) * (0.5 ** j) for j in range(1, 5)])
            f6 += noise_amp * fractal_noise
            
        # Enhanced global scaling with fractal dimensionality effect and improved fitness
        global_scale = 1.8 + 0.4 * np.sin(np.sum(x**2) / (self.dim * 8.0) + 0.3 * np.sum(x))
        
        return global_scale * (f1 + f2 + f3 + f4 + f5 + f6)