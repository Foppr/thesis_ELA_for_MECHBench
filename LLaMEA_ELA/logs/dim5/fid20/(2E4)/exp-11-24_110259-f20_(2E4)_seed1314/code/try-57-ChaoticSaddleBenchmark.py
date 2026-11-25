import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal generation
        self.fractal_consts = np.random.rand(dim, 4) * 2 - 1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Create chaotic map components with fractal basin boundaries
        chaos_terms = []
        for i in range(self.dim):
            # Each dimension has a different chaotic map parameter
            a, b, c, d = self.fractal_consts[i]
            
            # Logistic-like chaotic map with fractal basin structure
            x_i = x_scaled[i]
            chaos_val = np.sin(np.pi * x_i) * np.cos(np.pi * x_i)
            chaos_val += 0.5 * np.sin(2 * np.pi * x_i) * np.cos(2 * np.pi * x_i)
            chaos_val += 0.3 * np.sin(3 * np.pi * x_i) * np.cos(3 * np.pi * x_i)
            
            # Add fractal basin boundary effects
            boundary_effect = np.abs(np.sin(np.pi * x_i)) + 0.1 * np.abs(np.sin(2 * np.pi * x_i))
            
            chaos_terms.append(chaos_val * boundary_effect)
        
        # Create ergodic mixing through cross-dimensional coupling
        mixing_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Ergodic mixing between dimensions
                mix_term = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                mix_term *= np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                mixing_terms.append(mix_term)
        
        # Fractal basin structure with multi-scale complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            # Multi-fractal scaling with different exponents
            scale_factor = 1.0 / (1.0 + np.exp(-5.0 * x_scaled[i]))
            basin_complexity += scale_factor * np.sin(10.0 * x_scaled[i])
        
        # Global structural term with periodic modulation
        global_structure = np.sum(np.sin(0.5 * x_scaled) * np.cos(0.3 * x_scaled))
        global_structure += 0.5 * np.sum(np.sin(2.0 * x_scaled) * np.cos(1.5 * x_scaled))
        
        # Combine all components with dynamic weighting based on position
        pos_dependent_weight = 1.0 + 0.3 * np.sin(np.sum(x_scaled**2))
        
        result = pos_dependent_weight * (np.sum(chaos_terms) + 0.5 * np.sum(mixing_terms) + 
                                       0.3 * basin_complexity + 0.2 * global_structure)
        
        # Add small noise to ensure non-deterministic behavior at boundaries
        noise = 0.01 * np.random.rand() * np.exp(-np.sum(x_scaled**2))
        
        return result + noise