import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5]
        x = x / 5.0
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Fractal-like multimodal structure with nested harmonics
        fractal_term = 0.0
        for i in range(self.dim):
            # Nested harmonic potentials with fractal scaling
            scale = 2 ** (i % 3)
            freq = 2 ** (i // 2 + 1)
            fractal_term += np.sin(freq * x[i] * scale) * np.cos(freq * x[i] * scale) * np.exp(-i / self.dim)
        
        # Exponential decay minima with varying depths
        decay_term = 0.0
        for i in range(self.dim):
            # Create exponentially decaying minima
            depth = np.exp(-i / self.dim) * 0.5
            decay_term += depth * (np.sin(x[i]) + np.cos(x[i]))**2
        
        # Dynamic frequency modulation with chaotic behavior
        mod_term = 0.0
        for i in range(self.dim):
            # Chaotic modulation using logistic map-like dynamics
            freq_mod = 5 + 3 * np.sin(x[i] * 2) + 1.5 * np.cos(x[i] * 3)
            mod_term += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]) * np.exp(-i / self.dim)
        
        # Spiral attractor components
        spiral_term = 0.0
        for i in range(self.dim):
            # Create spiral-like structure in the landscape
            spiral_term += (x[i] * np.cos(i))**2 + (x[i] * np.sin(i))**2
        
        # Memory-dependent fitness evaluation with history effect
        memory_term = 0.0
        for i in range(self.dim):
            # Add dependency on previous dimensions
            if i > 0:
                memory_term += 0.1 * x[i] * x[i-1] * np.exp(-i / self.dim)
        
        # Combine all components
        result += 0.2 * fractal_term + 0.3 * decay_term + 0.2 * mod_term + 0.1 * spiral_term + 0.2 * memory_term
        
        return result