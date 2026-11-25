import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Nested radial component with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(17 * r**2) + 
                          0.03 * np.cos(13 * r**1.5))
        
        # Chaotic cross-terms with nested interactions and fractal-like behavior
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction terms
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * np.sin(x[i] * x[j] * 0.5 * (i + j + 1)) *
                              np.cos(x[i] * x[j] * 0.3 * (i + j + 1)) +
                              0.05 * np.sin(10 * x[i] * x[j] * np.sin(i * 0.1)) *
                              np.cos(8 * x[i] * x[j] * np.cos(j * 0.1))) * (i + j + 1)
                
        # Dynamic gradient modulation with chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.08 * np.sin(3 * x[i] * np.sin(i * 0.2)) *
                        np.cos(2 * x[i] * np.cos(i * 0.3)))
            
        # Highly multimodal component with nested frequencies and chaotic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i] * np.sin(i * 0.1)) +
                           0.03 * np.cos(15 * x[i] * np.cos(i * 0.2)))
            
        # Additional complex interaction terms with nested structure
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2) +
                                             0.03 * np.sin(x[i] * x[j] * 0.3 * (i + j)) *
                                             np.cos(x[i] * x[j] * 0.7 * (i + j))) * (i + j + 1)
        
        # Fractal-like periodic modulation based on coordinate sums and powers
        coord_sum = np.sum(x)
        coord_prod = np.prod(x) if len(x) > 0 else 0
        fractal_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) * \
                      (1 + 0.1 * np.sin(2 * coord_prod) * np.cos(1.5 * coord_prod))
        
        # Add chaotic noise component
        noise = 0.01 * np.sum(np.sin(50 * x) * np.cos(30 * x))
        
        # Combine all terms with different weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + fractal_mod + noise + 5.0