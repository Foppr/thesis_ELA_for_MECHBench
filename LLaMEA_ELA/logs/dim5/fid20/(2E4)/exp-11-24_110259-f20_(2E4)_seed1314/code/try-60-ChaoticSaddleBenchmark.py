import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal generation with enhanced complexity
        self.fractal_consts = np.random.rand(dim, 4) * 2 - 1
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Create chaotic map components with enhanced fractal basin boundaries
        chaos_terms = []
        for i in range(self.dim):
            # Each dimension has a different chaotic map parameter
            a, b, c, d = self.fractal_consts[i]
            
            # Enhanced logistic-like chaotic map with higher frequency terms
            x_i = x_scaled[i]
            chaos_val = np.sin(np.pi * x_i) * np.cos(np.pi * x_i)
            chaos_val += 0.7 * np.sin(2 * np.pi * x_i) * np.cos(2 * np.pi * x_i)  # Increased coefficient
            chaos_val += 0.4 * np.sin(3 * np.pi * x_i) * np.cos(3 * np.pi * x_i)
            chaos_val += 0.2 * np.sin(4 * np.pi * x_i) * np.cos(4 * np.pi * x_i)  # New higher frequency term
            
            # Enhanced fractal basin boundary effects
            boundary_effect = np.abs(np.sin(np.pi * x_i)) + 0.15 * np.abs(np.sin(2 * np.pi * x_i)) + 0.05 * np.abs(np.sin(3 * np.pi * x_i))  # Added third harmonic
            
            chaos_terms.append(chaos_val * boundary_effect)
        
        # Enhanced ergodic mixing through additional cross-dimensional coupling
        mixing_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced mixing between dimensions with additional interaction terms
                mix_term = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                mix_term += 0.3 * np.sin(2 * x_scaled[i] + x_scaled[j]) * np.cos(2 * x_scaled[i] - x_scaled[j])  # Additional coupling
                mix_term *= np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                mixing_terms.append(mix_term)
        
        # Enhanced fractal basin structure with multi-scale complexity
        basin_complexity = 0.0
        for i in range(self.dim):
            # Multi-fractal scaling with different exponents
            scale_factor = 1.0 / (1.0 + np.exp(-7.0 * x_scaled[i]))  # Increased steepness
            basin_complexity += scale_factor * np.sin(12.0 * x_scaled[i])  # Increased frequency
        
        # Enhanced global structural term with periodic modulation
        global_structure = np.sum(np.sin(0.6 * x_scaled) * np.cos(0.4 * x_scaled))  # Slightly altered frequencies
        global_structure += 0.6 * np.sum(np.sin(2.5 * x_scaled) * np.cos(1.8 * x_scaled))  # Increased coefficient and frequency
        
        # Combine all components with dynamic weighting based on position
        pos_dependent_weight = 1.0 + 0.4 * np.sin(np.sum(x_scaled**2))  # Increased weight variation
        
        result = pos_dependent_weight * (np.sum(chaos_terms) + 0.6 * np.sum(mixing_terms) + 
                                       0.4 * basin_complexity + 0.3 * global_structure)  # Adjusted weights
        
        # Add small noise to ensure non-deterministic behavior at boundaries
        noise = 0.015 * np.random.rand() * np.exp(-np.sum(x_scaled**2))  # Increased noise level
        
        return result + noise