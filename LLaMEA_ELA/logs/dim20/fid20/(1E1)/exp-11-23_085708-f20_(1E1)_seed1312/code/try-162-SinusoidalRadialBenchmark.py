import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Enhanced radial component with chaotic modulation and fractional frequencies
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(13 * r**1.5) +
                          0.03 * np.cos(9 * r**0.7))
        
        # Chaotic cross-terms with fractional interactions and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * np.sin(x[i]**1.3 * x[j]**0.8) *
                              np.cos(x[i]**0.6 * x[j]**1.4)) * (i + j + 1)**0.5
                
        # Dynamic gradient modulation with fractional frequencies and chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.05 * np.sin(x[i]**1.7) * np.cos(x[i]**0.9))
            
        # Highly multimodal component with fractional harmonics and chaotic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i]**1.3) +
                           0.03 * np.cos(15 * x[i]**0.7))
            
        # Complex interaction terms with fractional exponents and chaotic modulation
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2) +
                                             0.02 * np.sin(x[i]**1.2 * x[j]**0.8) *
                                             np.cos(x[i]**0.9 * x[j]**1.1)) * (i + j + 1)**0.7
        
        # Dynamic basin modulation with chaotic periodic components
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                       0.08 * np.sin(0.7 * coord_sum**1.3) * np.cos(0.4 * coord_sum**0.8)
        
        # Add a chaotic twist with fractional dimensionality scaling
        dim_scaling = (self.dim / 10.0)**1.5
        
        # Combine all terms with different weights and chaotic scaling factors
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + dim_scaling + 5.0