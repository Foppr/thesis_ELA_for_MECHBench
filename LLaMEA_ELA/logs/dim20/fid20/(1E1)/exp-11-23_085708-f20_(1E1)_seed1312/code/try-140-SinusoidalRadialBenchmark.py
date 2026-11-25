import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like radial component with fractional exponents and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r**(1.7) * (1 + 0.9 * np.sin(8 * r) + 0.4 * np.cos(13 * r) + 
                                0.2 * np.sin(23 * r) + 0.1 * np.cos(31 * r))
        
        # Chaotic cross-terms with fractional frequencies and phase shifts
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = (i + 1) ** 0.7
                freq_j = (j + 1) ** 0.7
                cross_term += (np.sin(x[i] * x[j] * freq_i * freq_j) + 
                              0.6 * np.cos(x[i] * x[j] * freq_i * freq_j * 1.5) + 
                              0.3 * np.sin(x[i] * freq_i) * np.cos(x[j] * freq_j) +
                              0.2 * np.cos(x[i] * x[j] * freq_i * 0.8)) * (i + j + 1) ** 0.5
                
        # Quantum-like gradient modulation with complex phase interference
        grad_mod = 1.0
        for i in range(self.dim):
            phase1 = np.sin(x[i] * 0.4 + 0.1 * np.sin(x[i] * 3))
            phase2 = np.cos(x[i] * 0.6 + 0.15 * np.cos(x[i] * 2.5))
            phase3 = np.sin(x[i] * 1.2 + 0.08 * np.sin(x[i] * 7))
            grad_mod *= (1 + 0.4 * phase1 + 0.3 * phase2 + 0.2 * phase3)
            
        # Multi-modal component with superimposed fractional frequencies
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(2.5 * x[i]) + 
                           0.8 * np.sin(5.2 * x[i]) + 
                           0.5 * np.cos(3.7 * x[i]) + 
                           0.3 * np.sin(8.1 * x[i]) +
                           0.2 * np.cos(6.9 * x[i]) +
                           0.1 * np.sin(12.3 * x[i]))
            
        # Fractal interaction terms with dimension-dependent scaling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    scale_factor = (i + 1) ** 0.3 * (j + 1) ** 0.3
                    interaction_term += 0.15 * (np.sin(x[i] * x[j] * 0.4 * scale_factor) + 
                                             0.08 * np.cos(x[i] * x[j] * 1.8 * scale_factor)) * scale_factor
        
        # Fractal periodic modulation based on coordinate sums with multiple phases
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.4 * np.sin(0.3 * coord_sum) * np.cos(0.2 * coord_sum) * np.sin(0.1 * coord_sum)
        
        # Add a new twist: fractional dimensionality effect with power-law scaling
        dim_factor = self.dim ** 0.6
        fractal_dim_mod = 1.0 + 0.25 * np.sin(0.8 * dim_factor) * np.cos(0.6 * dim_factor)
        
        # Combine all terms with different weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod * fractal_dim_mod + 10.0