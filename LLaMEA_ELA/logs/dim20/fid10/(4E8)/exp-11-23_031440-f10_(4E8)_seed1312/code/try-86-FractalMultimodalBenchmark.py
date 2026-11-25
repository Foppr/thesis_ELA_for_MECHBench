import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component using recursive polynomial expansion
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale polynomial with varying degrees
            poly_degree = int((i % 4) + 2)
            coeff = 1.0 / (i + 1)**1.2
            fractal_term += coeff * np.prod([np.sin((j+1) * np.pi * x_norm[i]) for j in range(poly_degree)])
        
        # Multi-resolution frequency modulation
        freq_mod = 0.0
        for i in range(self.dim):
            # Base frequency with harmonic progression
            base_freq = 2.0 + (i % 3)
            # Modulation factor based on position
            mod_factor = 1.0 + 0.5 * np.sin(4 * np.pi * x_norm[i])
            freq_mod += base_freq * mod_factor * np.cos(base_freq * np.pi * x_norm[i])
        
        # Self-similar basin structure with scaling factors
        basin_term = 0.0
        for i in range(self.dim):
            # Quadratic basin with fractal scaling
            scale = 1.0 / (1.0 + 0.3 * np.abs(x_norm[i]))
            basin_term += scale * x_norm[i]**2
        
        # Chaotic interaction terms using logistic map
        chaos_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Logistic map coupling
                logistic_val = 3.8 * np.abs(x_norm[i]) * (1 - np.abs(x_norm[i]))
                dist = np.abs(x_norm[i] - x_norm[j])
                chaos_interaction += logistic_val * np.exp(-dist**2) * np.sin(5 * dist)
        
        # Multi-modal component with fractal frequency spectrum
        modal_term = 0.0
        for i in range(self.dim):
            # Fractal frequency pattern
            freq = 2.0 + 1.5 * np.sin(np.pi * x_norm[i])
            modal_term += np.sin(freq * np.pi * x_norm[i]) * np.cos(3 * freq * np.pi * x_norm[i])
        
        # Combine all components with dimensionality scaling
        dim_scale = 1.0 + 0.2 * self.dim
        result = dim_scale * (0.7 * fractal_term + 
                             0.5 * freq_mod + 
                             0.3 * basin_term + 
                             0.4 * chaos_interaction + 
                             0.6 * modal_term)
        
        return result