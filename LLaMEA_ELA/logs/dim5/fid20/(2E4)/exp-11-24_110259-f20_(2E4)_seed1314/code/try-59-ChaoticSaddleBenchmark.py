import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for fractal generation and time-delayed dynamics
        self.fractal_consts = np.random.rand(dim, 6) * 2 - 1
        self.delay_coeffs = np.random.rand(dim, 3) * 0.5 + 0.5
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Create nested chaotic map components with time-delayed ergodic mixing
        chaos_terms = []
        for i in range(self.dim):
            # Each dimension has a different chaotic map parameter
            a, b, c, d, e, f = self.fractal_consts[i]
            
            # Nested logistic-like chaotic maps with time-delayed feedback
            x_i = x_scaled[i]
            chaos_val = np.sin(np.pi * x_i) * np.cos(np.pi * x_i)
            chaos_val += 0.5 * np.sin(2 * np.pi * x_i) * np.cos(2 * np.pi * x_i)
            chaos_val += 0.3 * np.sin(3 * np.pi * x_i) * np.cos(3 * np.pi * x_i)
            chaos_val += 0.1 * np.sin(5 * np.pi * x_i) * np.cos(5 * np.pi * x_i)
            
            # Add time-delayed ergodic mixing effects
            delay_effect = 0.0
            for j in range(min(i, 3)):
                delay_coeff = self.delay_coeffs[i][j]
                delay_effect += delay_coeff * np.sin(x_scaled[max(0, i-j-1)] + x_i)
            
            # Add fractal basin boundary effects with multi-scale complexity
            boundary_effect = np.abs(np.sin(np.pi * x_i)) + 0.1 * np.abs(np.sin(2 * np.pi * x_i))
            boundary_effect += 0.05 * np.abs(np.sin(4 * np.pi * x_i))
            
            chaos_terms.append((chaos_val + delay_effect) * boundary_effect)
        
        # Create multi-scale ergodic mixing through cross-dimensional coupling with memory
        mixing_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Multi-scale mixing with delayed feedback
                mix_term = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                mix_term *= np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                
                # Add time-delayed memory effects
                if i > 0 and j > 0:
                    memory_effect = np.sin(x_scaled[i-1] + x_scaled[j-1])
                    mix_term *= (1.0 + 0.2 * memory_effect)
                    
                mixing_terms.append(mix_term)
        
        # Multi-fractal basin structure with nested scaling
        basin_complexity = 0.0
        for i in range(self.dim):
            # Multi-fractal scaling with different exponents and nested structures
            scale_factor = 1.0 / (1.0 + np.exp(-5.0 * x_scaled[i]))
            scale_factor *= (1.0 + 0.3 * np.sin(10.0 * x_scaled[i]))
            basin_complexity += scale_factor * np.sin(15.0 * x_scaled[i])
            
        # Global structural term with periodic modulation and multi-scale harmonics
        global_structure = np.sum(np.sin(0.5 * x_scaled) * np.cos(0.3 * x_scaled))
        global_structure += 0.5 * np.sum(np.sin(2.0 * x_scaled) * np.cos(1.5 * x_scaled))
        global_structure += 0.2 * np.sum(np.sin(4.0 * x_scaled) * np.cos(3.0 * x_scaled))
        
        # Add nested chaotic dynamics with different frequency bands
        nested_dynamics = 0.0
        for i in range(self.dim):
            freq_band_1 = np.sin(8.0 * x_scaled[i])
            freq_band_2 = np.sin(16.0 * x_scaled[i])
            freq_band_3 = np.sin(32.0 * x_scaled[i])
            nested_dynamics += (freq_band_1 + 0.5 * freq_band_2 + 0.2 * freq_band_3)
        
        # Combine all components with refined dynamic weighting based on position and scale
        pos_dependent_weight = 1.0 + 0.3 * np.sin(np.sum(x_scaled**2))
        pos_dependent_weight *= (1.0 + 0.1 * np.cos(np.sum(x_scaled**4)))
        
        # Add more controlled noise to improve fitness while maintaining chaotic properties
        noise = 0.005 * np.random.rand() * np.exp(-np.sum(x_scaled**2))
        noise += 0.002 * np.random.rand() * np.sin(np.sum(x_scaled))
        
        # Adjust the weighting to reduce overfitting and improve generalization
        result = pos_dependent_weight * (np.sum(chaos_terms) + 0.3 * np.sum(mixing_terms) + 
                                       0.2 * basin_complexity + 0.15 * global_structure + 
                                       0.05 * nested_dynamics)
        
        # Reduce noise magnitude and adjust its influence to improve fitness score
        result += noise
        
        return result