import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like radial component with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(17 * r**2) + 
                          0.03 * np.cos(13 * r**1.5))
        
        # Chaotic cross-terms with fractal-like interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction with dynamic scaling based on dimension indices
                scale_factor = (i + j + 1) * (0.5 + 0.5 * np.sin(0.1 * (i + j)))
                cross_term += (np.sin(x[i] * x[j] * 2 * scale_factor) + 
                              0.5 * np.cos(x[i] * x[j] * 3 * scale_factor) + 
                              0.3 * np.sin(x[i] * 0.7 * scale_factor) * np.cos(x[j] * 0.9 * scale_factor) +
                              0.2 * np.cos(x[i] * x[j] * 4 * scale_factor) +
                              0.1 * np.sin(x[i]**2 * x[j] * 0.5) * np.cos(x[i] * x[j]**2 * 0.3)) * scale_factor
                
        # Dynamic gradient modulation with fractal characteristics
        grad_mod = 1.0
        for i in range(self.dim):
            # Add chaotic modulation with multiple frequencies and dynamic scaling
            dynamic_scale = 1.0 + 0.5 * np.sin(0.3 * x[i] * (i + 1)) + 
                           0.2 * np.cos(0.7 * x[i] * (i + 1)) + 
                           0.3 * np.sin(1.1 * x[i] * (i + 1)) +
                           0.1 * np.cos(1.5 * x[i] * (i + 1)) + 
                           0.05 * np.sin(2.3 * x[i]**2)
            grad_mod *= dynamic_scale
            
        # Highly multimodal component with nested peaks and fractal structure
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i]**2) +
                           0.03 * np.cos(15 * x[i]**1.5))
            
        # Complex interaction terms with fractal-like structure and nested correlations
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Add nested interaction with dynamic scaling factors
                    scale_factor = (i + j + 1) * (0.8 + 0.2 * np.sin(0.05 * (i + j)))
                    interaction_term += (0.1 * (np.sin(x[i] * x[j] * 0.5 * scale_factor) + 
                                             0.05 * np.cos(x[i] * x[j] * 2 * scale_factor)) * scale_factor +
                                       0.02 * np.sin(x[i]**2 * x[j] * 0.3) * np.cos(x[i] * x[j]**2 * 0.4))
        
        # Add chaotic periodic modulation based on coordinate combinations
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                      0.1 * np.sin(0.2 * coord_sum**2) * np.cos(0.1 * coord_sum**3)
        
        # Add fractal-like scaling factor that depends on the entire coordinate vector
        total_scale = np.sum(np.abs(x)) / self.dim
        fractal_factor = 1.0 + 0.2 * np.sin(total_scale * 10) * np.cos(total_scale * 7)
        
        # Combine all terms with different weights and add a constant offset for global minimum
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod * fractal_factor + 5.0