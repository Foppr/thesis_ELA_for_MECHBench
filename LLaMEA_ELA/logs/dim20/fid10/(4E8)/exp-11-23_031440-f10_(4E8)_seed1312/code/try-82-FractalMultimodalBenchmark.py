import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure using recursive sine waves
        fractal_term = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with diminishing amplitude
            amplitude = 1.0
            frequency = 2.0
            term = 0.0
            for depth in range(3):  # 3 levels of recursion
                term += amplitude * np.sin(frequency * x_norm[i])
                amplitude *= 0.5
                frequency *= 2
            fractal_term += term
        
        # Logarithmic conditioning that scales with dimensionality
        log_condition = 1.0 + 2.0 * np.log(1.0 + self.dim)
        
        # Hybrid oscillatory terms with different frequencies and coupling
        hybrid_terms = 0.0
        for i in range(self.dim):
            # Primary oscillator
            primary = np.sin(2 * np.pi * x_norm[i])
            # Coupled secondary oscillator
            if i > 0:
                coupled = np.cos(3 * np.pi * (x_norm[i] + x_norm[i-1]))
            else:
                coupled = np.cos(3 * np.pi * x_norm[-1])
            
            # Combined hybrid term
            hybrid_terms += primary * coupled
        
        # Multi-scale basin structure with varying curvature
        basin_term = 0.0
        for i in range(self.dim):
            # Different scaling factors for different dimensions
            scale_factor = 1.0 + 0.5 * np.sin(i)
            basin_term += scale_factor * (x_norm[i]**2 + 0.3 * x_norm[i]**4)
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with distance-dependent scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.sin(5 * np.pi * dist) * np.exp(-dist**2)
                cross_term += coupling
        
        # Add noise component for increased complexity
        noise = 0.1 * np.random.rand()
        
        # Combine all terms with proper weighting
        result = log_condition * (0.4 * fractal_term + 0.3 * hybrid_terms + 
                                0.2 * basin_term + 0.1 * cross_term) + noise
        
        return result