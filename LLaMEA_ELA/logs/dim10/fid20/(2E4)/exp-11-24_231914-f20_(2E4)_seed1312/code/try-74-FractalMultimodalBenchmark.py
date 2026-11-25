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
        
        # Add superimposed chaotic field with enhanced nonlinearity
        chaotic_field = 0.0
        for i in range(self.dim):
            chaotic_field += np.sin(15 * x[i]**3) * np.cos(8 * x[i]) * np.exp(-0.3 * np.abs(x[i]))
        
        # Add higher dimensional coupling with exponential decay
        high_dim_coupling = 0.0
        for i in range(self.dim - 3):
            high_dim_coupling += 0.6 * np.sin(3.0 * x[i]) * np.cos(4.0 * x[i+1]) * \
                                np.sin(2.5 * x[i+2]) * np.exp(-0.2 * x[i+3]**2)
        
        # Add fractal-like oscillatory component with varying amplitude
        fractal_osc = 0.0
        for i in range(self.dim):
            fractal_osc += 1.2 * np.sin(5.0 * x[i]) * np.cos(3.0 * x[i]**2) * \
                          np.exp(-0.1 * np.abs(x[i])) * (1 + 0.3 * np.sin(7.0 * x[i]))
        
        # Combine all components with different weights to create complex landscape
        return base + 2.2 * fractal + 1.5 * chaotic + 0.9 * periodic + 0.6 * rugged + \
               0.5 * coupling + 0.4 * global_mod + 1.0 * chaotic_field + 0.7 * high_dim_coupling + 0.8 * fractal_osc