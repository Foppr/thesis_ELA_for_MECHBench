import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for scalability
        self.fractal_dims = [2.5, 1.8, 3.3, 2.9, 2.1][:min(dim, 5)]
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Fractal multimodal component with self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Use fractional Brownian motion-like scaling
            scale = self.fractal_dims[i % len(self.fractal_dims)]
            fractal += np.sin(scale * x[i]) * np.cos(scale * x[i]**2) * np.exp(-0.15 * np.abs(x[i]))
        
        # Chaotic gradient field with stronger discontinuities
        chaotic = 0.0
        for i in range(self.dim):
            # Create more pronounced piecewise non-smooth behavior
            if x[i] < 0:
                chaotic += np.sin(12 * x[i]) * np.exp(-0.6 * x[i]**2)
            else:
                chaotic += np.cos(10 * x[i]) * np.exp(-0.4 * x[i]**2)
        
        # Multi-scale periodic interactions with higher frequency components
        periodic = 0.0
        for i in range(self.dim):
            periodic += (1.5 * np.sin(6 * x[i]) * np.cos(4 * x[i]) + 
                        1.0 * np.sin(8 * x[i]) * np.cos(5 * x[i]) + 
                        0.7 * np.sin(10 * x[i]) * np.cos(7 * x[i]))
        
        # Ruggedness through higher-order polynomial interactions
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += (x[i]**3 + x[i+1]**3) * np.exp(-0.25 * (x[i] - x[i+1])**2)
        
        # Asymmetric coupling terms with varying strength
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += 0.7 * np.sin(2.5 * x[i]) * np.cos(3.5 * x[i+1]) * np.exp(-0.15 * x[i+2]**2)
        
        # Global modulation with fractal-like scaling
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.4 * np.sin(4.5 * x[i]) * np.cos(2.5 * x[i]) * np.exp(-0.07 * np.abs(x[i]))
        
        # Combine all components with different weights to create complex landscape
        return base + 1.8 * fractal + 1.0 * chaotic + 0.7 * periodic + 0.5 * rugged + 0.4 * coupling + 0.3 * global_mod