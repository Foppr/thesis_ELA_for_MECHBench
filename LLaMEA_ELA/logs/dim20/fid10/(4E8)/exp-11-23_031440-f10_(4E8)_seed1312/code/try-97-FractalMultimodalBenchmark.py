import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with chaotic sinusoidal interference
        fractal_term = 0.0
        for i in range(self.dim):
            amplitude = 1.0
            frequency = 2.0
            term = 0.0
            for depth in range(4):  # Increased recursion depth
                # Add chaotic element with small random perturbation
                chaotic_factor = 1.0 + 0.1 * np.sin(i * depth * np.pi / 4)
                term += amplitude * chaotic_factor * np.sin(frequency * x_norm[i])
                amplitude *= 0.4  # Reduced decay rate for more complexity
                frequency *= 2.5  # Increased frequency growth
            fractal_term += term
        
        # Dynamic conditioning with exponential scaling
        dynamic_condition = np.exp(0.5 * self.dim) + 1.0
        
        # Hybrid oscillatory components with varying coupling strengths
        hybrid_terms = 0.0
        for i in range(self.dim):
            # Primary oscillator with variable frequency
            freq_primary = 2 * (i + 1)
            primary = np.sin(freq_primary * x_norm[i])
            
            # Coupled oscillators with different interaction patterns
            if i > 0:
                coupled = np.cos(3 * (x_norm[i] + x_norm[i-1]))
            else:
                coupled = np.cos(3 * (x_norm[i] + x_norm[-1]))
            
            # Add chaotic coupling factor
            coupling_factor = 1.0 + 0.2 * np.sin(i * np.pi / 3)
            hybrid_terms += coupling_factor * primary * coupled
        
        # Multi-scale basin structure with varying curvature and chaos
        basin_term = 0.0
        for i in range(self.dim):
            # Dimension-specific scaling with chaotic variation
            scale_factor = 1.0 + 0.3 * np.sin(i * np.pi / 2) + 0.2 * np.random.rand()
            basin_term += scale_factor * (x_norm[i]**2 + 0.4 * x_norm[i]**4 + 0.1 * x_norm[i]**6)
        
        # Cross-dimensional coupling with chaotic interaction patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic distance-dependent coupling
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.sin(7 * np.pi * dist) * np.exp(-dist**2) * (1.0 + 0.1 * np.sin(i * j))
                cross_term += coupling
        
        # Add chaotic noise component
        noise = 0.15 * np.random.rand() * (1.0 + 0.5 * np.sin(self.dim))
        
        # Combine all terms with optimized weighting for increased difficulty
        result = dynamic_condition * (0.35 * fractal_term + 0.25 * hybrid_terms + 
                                    0.2 * basin_term + 0.2 * cross_term) + noise
        
        return result