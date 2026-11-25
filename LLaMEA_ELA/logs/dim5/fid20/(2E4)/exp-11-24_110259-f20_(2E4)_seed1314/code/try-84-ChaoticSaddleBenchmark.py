import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute enhanced fractal constants with higher dimensional complexity
        self.fractal_consts = np.random.rand(dim, 12) * 4 - 2
        self.delay_coeffs = np.random.rand(dim, 6) * 0.9 + 0.1
        self.coupling_strengths = np.random.rand(dim, dim) * 1.2 + 0.8
        
    def f(self, x):
        # Scale input to [-1, 1] range with enhanced nonlinearity
        x_scaled = np.tanh(x / 5.0)
        
        # Enhanced nested chaotic map components with multi-frequency modulation
        chaos_terms = []
        for i in range(self.dim):
            # Multi-frequency chaotic dynamics with adaptive coupling
            a, b, c, d, e, f, g, h, i, j, k, l = self.fractal_consts[i]
            
            # Complex chaotic map with 8 harmonic components and nonlinear mixing
            x_i = x_scaled[i]
            chaos_val = np.sin(2 * np.pi * x_i) * np.cos(2 * np.pi * x_i)
            chaos_val += 0.8 * np.sin(4 * np.pi * x_i) * np.cos(4 * np.pi * x_i)
            chaos_val += 0.6 * np.sin(6 * np.pi * x_i) * np.cos(6 * np.pi * x_i)
            chaos_val += 0.4 * np.sin(8 * np.pi * x_i) * np.cos(8 * np.pi * x_i)
            chaos_val += 0.25 * np.sin(12 * np.pi * x_i) * np.cos(12 * np.pi * x_i)
            chaos_val += 0.18 * np.sin(16 * np.pi * x_i) * np.cos(16 * np.pi * x_i)
            chaos_val += 0.14 * np.sin(20 * np.pi * x_i) * np.cos(20 * np.pi * x_i)
            chaos_val += 0.1 * np.sin(24 * np.pi * x_i) * np.cos(24 * np.pi * x_i)
            
            # Advanced time-delayed mixing with higher memory depth
            delay_effect = 0.0
            for j in range(min(i, 6)):
                delay_coeff = self.delay_coeffs[i][j]
                delay_effect += delay_coeff * np.sin(x_scaled[max(0, i-j-1)] + x_i) * np.cos(x_scaled[max(0, i-j-1)] - x_i)
            
            # Multi-scale fractal basin boundary effects with enhanced complexity
            boundary_effect = (np.abs(np.sin(2 * np.pi * x_i)) + 0.25 * np.abs(np.sin(4 * np.pi * x_i)) +
                              0.15 * np.abs(np.sin(8 * np.pi * x_i)) + 0.08 * np.abs(np.sin(16 * np.pi * x_i)) +
                              0.04 * np.abs(np.sin(32 * np.pi * x_i)) + 0.02 * np.abs(np.sin(64 * np.pi * x_i)))
            
            chaos_terms.append((chaos_val + delay_effect) * boundary_effect)
        
        # Advanced multi-scale ergodic mixing with cross-dimensional memory
        mixing_terms = []
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling to increase complexity
                # Enhanced mixing with frequency separation and dynamic damping
                mix_term = np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
                mix_term *= np.exp(-0.4 * (x_scaled[i]**2 + x_scaled[j]**2))
                
                # Memory effects with multi-step delayed coupling
                memory_effect = 0.0
                for k in range(min(5, i)):
                    memory_effect += self.coupling_strengths[i][j] * np.sin(x_scaled[i-k-1] + x_scaled[j-k-1])
                
                mix_term *= (1.0 + 0.6 * memory_effect)
                mixing_terms.append(mix_term)
        
        # Enhanced multi-fractal basin structure with nested scaling
        basin_complexity = 0.0
        for i in range(self.dim):
            # Multi-scale fractal structure with varying exponents and nested harmonics
            scale_factor = 1.0 / (1.0 + np.exp(-10.0 * x_scaled[i]))  # Steeper sigmoid
            scale_factor *= (1.0 + 0.6 * np.sin(25.0 * x_scaled[i]))  # Higher frequency
            scale_factor *= (1.0 + 0.4 * np.cos(50.0 * x_scaled[i]))  # Additional harmonic
            
            basin_complexity += scale_factor * np.sin(30.0 * x_scaled[i])  # Increased frequency
        
        # Global structural term with enhanced periodic modulation
        global_structure = np.sum(np.sin(1.0 * x_scaled) * np.cos(0.8 * x_scaled))
        global_structure += 0.8 * np.sum(np.sin(3.5 * x_scaled) * np.cos(3.0 * x_scaled))
        global_structure += 0.6 * np.sum(np.sin(7.0 * x_scaled) * np.cos(6.5 * x_scaled))
        global_structure += 0.4 * np.sum(np.sin(12.0 * x_scaled) * np.cos(11.0 * x_scaled))
        global_structure += 0.3 * np.sum(np.sin(18.0 * x_scaled) * np.cos(17.0 * x_scaled))
        global_structure += 0.2 * np.sum(np.sin(25.0 * x_scaled) * np.cos(24.0 * x_scaled))
        
        # Nested chaotic dynamics with ultra-high frequency components
        nested_dynamics = 0.0
        for i in range(self.dim):
            freq_band_1 = np.sin(20.0 * x_scaled[i])
            freq_band_2 = np.sin(40.0 * x_scaled[i])
            freq_band_3 = np.sin(80.0 * x_scaled[i])
            freq_band_4 = np.sin(160.0 * x_scaled[i])
            freq_band_5 = np.sin(320.0 * x_scaled[i])
            nested_dynamics += (freq_band_1 + 0.8 * freq_band_2 + 0.6 * freq_band_3 + 0.4 * freq_band_4 + 0.2 * freq_band_5)
        
        # Position-dependent adaptive weighting with enhanced nonlinearity
        pos_dependent_weight = 1.0 + 0.7 * np.sin(np.sum(x_scaled**2))
        pos_dependent_weight *= (1.0 + 0.35 * np.cos(np.sum(x_scaled**4)))
        pos_dependent_weight *= (1.0 + 0.4 * np.sin(2 * np.sum(x_scaled**3)))
        
        # Final combination with enhanced weights and reduced noise
        result = pos_dependent_weight * (np.sum(chaos_terms) + 0.8 * np.sum(mixing_terms) + 
                                       0.6 * basin_complexity + 0.5 * global_structure + 
                                       0.4 * nested_dynamics)
        
        # Enhanced noise with better distribution properties
        noise = 0.003 * np.random.rand() * np.exp(-np.sum(x_scaled**2))
        noise += 0.002 * np.random.rand() * np.sin(np.sum(x_scaled))
        noise += 0.001 * np.random.rand() * np.cos(np.sum(x_scaled**3))
        noise += 0.0005 * np.random.rand() * np.sin(2 * np.sum(x_scaled**2))
        
        return result + noise