import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic map parameters and coupling matrices
        self.chebyshev_coeffs = np.random.rand(dim, 6) * 2 - 1
        self.coupling_matrix = np.random.rand(dim, dim) * 0.8 + 0.2
        self.harmonic_freqs = np.random.rand(dim) * 12 + 3
        self.spatial_weights = np.random.rand(dim) * 3 + 1
        # Chaotic map parameters
        self.r_values = np.random.rand(dim) * 3.8 + 0.2
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chebyshev polynomial chaos expansion terms with chaotic coupling
        chebyshev_terms = []
        for i in range(self.dim):
            # Chebyshev basis functions
            coeffs = self.chebyshev_coeffs[i]
            T2 = 2 * x_scaled[i]**2 - 1
            T3 = 4 * x_scaled[i]**3 - 3 * x_scaled[i]
            T4 = 8 * x_scaled[i]**4 - 8 * x_scaled[i]**2 + 1
            T5 = 16 * x_scaled[i]**5 - 20 * x_scaled[i]**3 + 5 * x_scaled[i]
            T6 = 32 * x_scaled[i]**6 - 48 * x_scaled[i]**4 + 18 * x_scaled[i]**2 - 1
            
            cheby_val = (coeffs[0] * T2 + 
                        coeffs[1] * T3 + 
                        coeffs[2] * T4 + 
                        coeffs[3] * T5 + 
                        coeffs[4] * T6 + 
                        coeffs[5])
            
            # Chaotic coupling effects
            coupling_effect = 0.0
            for j in range(self.dim):
                coupling_strength = self.coupling_matrix[i][j]
                # Apply chaotic map dynamics
                r = self.r_values[j]
                chaotic_val = np.sin(r * x_scaled[j] * (1 - x_scaled[j]))
                coupling_effect += coupling_strength * chaotic_val
            
            chebyshev_terms.append(cheby_val + coupling_effect * self.spatial_weights[i])
        
        # Multi-scale harmonic interference with chaotic modulation
        interference_terms = []
        for i in range(self.dim):
            freq = self.harmonic_freqs[i]
            # Apply chaotic modulation to frequencies
            mod_freq = freq * (1.0 + 0.3 * np.sin(self.r_values[i] * x_scaled[i]))
            
            interference = np.sin(mod_freq * x_scaled[i]) * np.cos(mod_freq * x_scaled[i])
            
            # Multi-scale harmonic mixing with chaotic weights
            mix_term = 0.0
            for k in range(1, 6):
                weight = 1.0 / (k**1.5) * (1.0 + 0.2 * np.sin(self.r_values[i] * k))
                mix_term += weight * np.sin(k * mod_freq * x_scaled[i]) * np.cos(k * mod_freq * x_scaled[i])
            
            interference_terms.append(interference + 0.4 * mix_term)
        
        # Nested chaotic coupling with varying strengths
        nested_coupling = []
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, self.dim):
                strength = self.coupling_matrix[i][j] * 0.5
                # Apply chaotic transformation to coupling
                chaotic_coupling = np.sin(self.r_values[i] * x_scaled[i]) * np.cos(self.r_values[j] * x_scaled[j])
                coupling_sum += strength * chaotic_coupling * np.sin(x_scaled[i] + x_scaled[j])
            nested_coupling.append(coupling_sum)
        
        # Adaptive spatial modulation with chaotic interference
        spatial_modulation = 0.0
        for i in range(self.dim):
            # Apply chaotic transformation to weights
            chaotic_weight = self.spatial_weights[i] * (1.0 + 0.2 * np.sin(self.r_values[i] * x_scaled[i]))
            
            spatial_term = np.sin(chaotic_weight * x_scaled[i])
            spatial_term += 0.4 * np.sin(2 * chaotic_weight * x_scaled[i])
            spatial_term += 0.15 * np.sin(4 * chaotic_weight * x_scaled[i])
            spatial_modulation += spatial_term
        
        # Global structure with chaotic polynomial components
        global_structure = (np.sum(np.sin(x_scaled) * np.cos(x_scaled)) + 
                          0.7 * np.sum(np.sin(2 * x_scaled) * np.cos(2 * x_scaled)) +
                          0.3 * np.sum(np.sin(4 * x_scaled) * np.cos(4 * x_scaled)) +
                          0.15 * np.sum(np.sin(8 * x_scaled) * np.cos(8 * x_scaled)))
        
        # Chaotic weighting based on position
        pos_weight = 1.0 + 0.5 * np.sin(np.sum(x_scaled**2))
        pos_weight *= (1.0 + 0.3 * np.cos(np.sum(x_scaled**4)))
        # Add chaotic modulation to weight
        chaotic_mod = 1.0 + 0.2 * np.sin(self.r_values[0] * np.sum(x_scaled))
        pos_weight *= chaotic_mod
        
        # Combine all components with chaotic scaling
        result = (pos_weight * (np.sum(chebyshev_terms) + 0.8 * np.sum(interference_terms) + 
                               0.6 * np.sum(nested_coupling) + 0.4 * spatial_modulation + 
                               0.3 * global_structure))
        
        # Add chaotic noise for robustness
        noise = 0.01 * np.random.rand() * (1.0 + 0.3 * np.sin(np.sum(x_scaled**2)))
        return result + noise