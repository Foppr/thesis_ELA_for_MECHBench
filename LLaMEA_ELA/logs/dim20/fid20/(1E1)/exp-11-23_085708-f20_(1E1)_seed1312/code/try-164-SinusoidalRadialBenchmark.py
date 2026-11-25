import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Enhanced radial component with fractional frequencies and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(13 * r**1.5) +
                          0.02 * np.cos(17 * r**0.7))
        
        # Chaotic cross-terms with fractional interactions and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional interaction terms with chaotic phase shifts
                frac_interaction = (np.sin(x[i] * x[j] * 2**0.5) + 
                                  0.5 * np.cos(x[i] * x[j] * 3**0.5) + 
                                  0.3 * np.sin(x[i] * 0.7**0.3) * np.cos(x[j] * 0.9**0.7) +
                                  0.2 * np.cos(x[i] * x[j] * 4**0.8) +
                                  0.1 * np.sin(x[i]**0.5 * x[j]**0.3))
                # Dynamic weight based on dimension indices and chaotic function
                weight = (i + j + 1) * (1 + 0.1 * np.sin(i * j * 0.1) + 
                                       0.05 * np.cos(i + j * 0.07))
                cross_term += frac_interaction * weight
                
        # Multi-frequency adaptive gradient modulation with fractal-like components
        grad_mod = 1.0
        for i in range(self.dim):
            # Add fractional and chaotic components to gradient modulation
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3**0.7) + 
                        0.2 * np.cos(x[i] * 0.7**1.3) + 
                        0.3 * np.sin(x[i] * 1.1**0.5) +
                        0.1 * np.cos(x[i] * 1.5**0.8) +
                        0.05 * np.sin(x[i]**1.7) * np.cos(x[i]**0.3))
            
        # Highly multimodal component with fractional frequencies and chaotic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]**1.3) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]**0.7) +
                           0.1 * np.cos(8 * x[i]**1.5) +
                           0.05 * np.sin(12 * x[i] * np.sin(x[i])) +
                           0.03 * np.cos(15 * x[i] * np.cos(x[i])))
            
        # Complex interaction terms with fractal-like behavior and dynamic scaling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal-like interaction with dynamic scaling factors
                    scale_factor = (1 + 0.05 * np.sin(i * 0.1) * np.cos(j * 0.07))
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5**0.3) + 
                                             0.05 * np.cos(x[i] * x[j] * 2**0.9)) * scale_factor * (i + j + 1)
        
        # Dynamic phase shift modulation based on coordinate sum and fractal structure
        coord_sum = np.sum(x)
        phase_shift = 0.3 * np.sin(0.5 * coord_sum * np.cos(coord_sum))
        periodic_mod = 1.0 + phase_shift
        
        # Add a new chaotic twist: fractal dimension-based modulation
        fractal_dim_mod = 1.0 + 0.2 * np.sin(r * 10) * np.cos(r * 7) * np.sin(r * 3)
        
        # Combine all terms with different weights and add chaotic offset
        return (radial_term + cross_term + grad_mod * multi_modal + 
                interaction_term + periodic_mod * fractal_dim_mod + 5.0 + 
                0.1 * np.sin(coord_sum * 100))