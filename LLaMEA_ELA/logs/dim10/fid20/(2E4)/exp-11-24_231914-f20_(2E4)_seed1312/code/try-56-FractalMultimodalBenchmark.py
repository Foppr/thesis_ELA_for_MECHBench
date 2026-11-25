import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for scalability
        self.fractal_dims = [2.3, 1.7, 3.1, 2.8, 1.9][:min(dim, 5)]
        
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
            fractal += np.sin(scale * x[i]) * np.cos(scale * x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Chaotic gradient field with discontinuities
        chaotic = 0.0
        for i in range(self.dim):
            # Create piecewise non-smooth behavior
            if x[i] < 0:
                chaotic += np.sin(10 * x[i]) * np.exp(-0.5 * x[i]**2)
            else:
                chaotic += np.cos(8 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Multi-scale periodic interactions
        periodic = 0.0
        for i in range(self.dim):
            periodic += (1.2 * np.sin(5 * x[i]) * np.cos(3 * x[i]) + 
                        0.8 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 
                        0.5 * np.sin(9 * x[i]) * np.cos(6 * x[i]))
        
        # Ruggedness through higher-order polynomial interactions
        rugged = 0.0
        for i in range(self.dim - 1):
            rugged += (x[i]**3 + x[i+1]**3) * np.exp(-0.2 * (x[i] - x[i+1])**2)
        
        # Asymmetric coupling terms with varying strength
        coupling = 0.0
        for i in range(self.dim - 2):
            coupling += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[i+1]) * np.exp(-0.1 * x[i+2]**2)
        
        # Global modulation with fractal-like scaling
        global_mod = 0.0
        for i in range(self.dim):
            global_mod += 0.3 * np.sin(4 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.05 * np.abs(x[i]))
        
        # Combine all components with different weights to create complex landscape
        return base + 1.5 * fractal + 0.8 * chaotic + 0.6 * periodic + 0.4 * rugged + 0.3 * coupling + 0.2 * global_mod