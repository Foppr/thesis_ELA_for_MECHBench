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
            
            # Enhanced logistic-like chaotic maps with improved ergodic properties
            x_i = x_scaled[i]
            chaos_val = np.sin(np.pi * x_i) * np.cos(np.pi * x_i)
            chaos_val += 0.6 * np.sin(2 * np.pi * x_i) * np.cos(2 * np.pi * x_i)  # Increased weight
            chaos_val += 0.25 * np.sin(3 * np.pi * x_i) * np.cos(3 * np.pi * x_i)  # Reduced weight
            chaos_val += 0.15 * np.sin(5 * np.pi * x_i) * np.cos(5 * np.pi * x_i)  # Increased weight
            
            # Improved time-delayed ergodic mixing effects with better coupling
            delay_effect = 0.0
            for j in range(min(i, 3)):
                delay_coeff = self.delay_coeffs[i][j]
                delay_effect += delay_coeff * np.sin(x_scaled[max(0, i-j-1)] + x_i)
            
            # Enhanced fractal basin boundary effects with more diverse scaling
            boundary_effect = np.abs(np.sin(np.pi * x_i)) + 0.15 * np.abs(np.sin(2 * np.pi * x_i))  # Increased weight
            boundary_effect += 0.07 * np.abs(np.sin(4 * np.pi * x_i))  # Increased weight
            boundary_effect += 0.03 * np.abs(np.sin(8 * np.pi * x_i))  # Increased weight
            
            chaos_terms.append((chaos_val + delay_effect) * boundary_effect)
        
        # Improved multi-scale ergodic mixing through cross-dimensional coupling with memory
        mixing_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced mixing with better frequency separation and damping
                mix_term = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                mix_term *= np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                
                # Add time-delayed memory effects with improved scaling
                if i > 0 and j > 0:
                    memory_effect = np.sin(x_scaled[i-1] + x_scaled[j-1])
                    mix_term *= (1.0 + 0.4 * memory_effect)  # Increased weight
                    
                mixing_terms.append(mix_term)
        
        # Enhanced multi-fractal basin structure with better nested scaling
        basin_complexity = 0.0
        for i in range(self.dim):
            # Improved multi-fractal scaling with different exponents and nested structures
            scale_factor = 1.0 / (1.0 + np.exp(-6.0 * x_scaled[i]))  # Increased steepness
            scale_factor *= (1.0 + 0.4 * np.sin(12.0 * x_scaled[i]))  # Increased frequency
            basin_complexity += scale_factor * np.sin(18.0 * x_scaled[i])  # Increased frequency
            
        # Enhanced global structural term with periodic modulation and multi-scale harmonics
        global_structure = np.sum(np.sin(0.6 * x_scaled) * np.cos(0.4 * x_scaled))  # Increased frequencies
        global_structure += 0.6 * np.sum(np.sin(2.5 * x_scaled) * np.cos(2.0 * x_scaled))  # Increased weights and frequencies
        global_structure += 0.25 * np.sum(np.sin(4.5 * x_scaled) * np.cos(3.5 * x_scaled))  # Increased weights and frequencies
        global_structure += 0.15 * np.sum(np.sin(8.5 * x_scaled) * np.cos(6.5 * x_scaled))  # Increased weights and frequencies
        
        # Enhanced nested chaotic dynamics with better frequency band separation
        nested_dynamics = 0.0
        for i in range(self.dim):
            freq_band_1 = np.sin(9.0 * x_scaled[i])  # Increased frequency
            freq_band_2 = np.sin(18.0 * x_scaled[i])  # Increased frequency
            freq_band_3 = np.sin(36.0 * x_scaled[i])  # Increased frequency
            nested_dynamics += (freq_band_1 + 0.6 * freq_band_2 + 0.3 * freq_band_3)  # Increased weights
        
        # Improved combination with better weighting and reduced bias
        pos_dependent_weight = 1.0 + 0.4 * np.sin(np.sum(x_scaled**2))  # Increased weight
        pos_dependent_weight *= (1.0 + 0.2 * np.cos(np.sum(x_scaled**4)))  # Increased weight
        
        result = pos_dependent_weight * (np.sum(chaos_terms) + 0.6 * np.sum(mixing_terms) + 
                                       0.4 * basin_complexity + 0.3 * global_structure + 
                                       0.2 * nested_dynamics)
        
        # Reduced noise level to decrease systematic bias while maintaining chaotic behavior
        noise = 0.003 * np.random.rand() * np.exp(-np.sum(x_scaled**2))  # Decreased noise
        noise += 0.001 * np.random.rand() * np.sin(np.sum(x_scaled))  # Decreased noise
        
        return result + noise