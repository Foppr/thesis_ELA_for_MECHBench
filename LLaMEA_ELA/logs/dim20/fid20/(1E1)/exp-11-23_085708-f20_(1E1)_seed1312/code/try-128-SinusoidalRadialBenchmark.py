import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Nested radial component with chaotic sine-wave modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(17 * r**2) + 
                          0.03 * np.cos(13 * r**1.5))
        
        # Chaotic cross-terms with nested interactions and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * np.sin(x[i] * x[j] * 0.5) * np.cos(x[i] * 0.3) *
                              np.sin(x[j] * 0.7)) * (i + j + 1) * np.sin(0.1 * (i + j))
                
        # Dynamic gradient modulation with chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.05 * np.sin(x[i] * 2.3) * np.cos(x[i] * 3.7))
            
        # Highly multimodal component with nested frequencies and chaotic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i]**2) +
                           0.03 * np.cos(15 * x[i]**1.5))
            
        # Nested interaction terms with chaotic modulation and higher-order components
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += (0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2)) * 
                                       (i + j + 1) * np.sin(0.02 * (i * j + i + j)))
        
        # Chaotic periodic modulation based on coordinate sums and products
        coord_sum = np.sum(x)
        coord_prod = np.prod(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                      0.2 * np.sin(0.7 * coord_prod) * np.cos(0.4 * coord_prod) + \
                      0.1 * np.sin(0.9 * coord_sum * coord_prod)
        
        # Add a chaotic twist with fractal-like component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.02 * np.sin(50 * x[i]) * np.cos(30 * x[i])
            
        # Combine all terms with different weights and chaotic scaling factors
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + fractal_component + 5.0