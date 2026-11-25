import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractional dimensional scaling with chaotic sine interactions
        r = np.sqrt(np.sum(x_scaled**2))
        fractional_r = r ** 1.7
        radial_term = fractional_r * (1 + 0.9 * np.sin(8 * r) + 0.4 * np.cos(12 * r) + 0.2 * np.sin(15 * r))
        
        # Chaotic cross-terms with fractional exponents and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i]**1.3 * x[j]**1.7 * 3) + 
                              0.6 * np.cos(x[i]**0.8 * x[j]**1.2 * 4) + 
                              0.4 * np.sin(x[i] * 0.5) * np.cos(x[j] * 0.7) +
                              0.3 * np.cos(x[i]**1.5 * x[j]**0.9 * 5)) * (i + j + 1)**0.7
                
        # Dynamic gradient modulation with chaotic sine components and time-varying weights
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.6 * np.sin(x[i] * 0.4 + 0.2 * np.sin(3 * x[i])) + 
                        0.3 * np.cos(x[i] * 0.8 + 0.1 * np.cos(5 * x[i])) + 
                        0.4 * np.sin(x[i] * 1.2 + 0.15 * np.sin(7 * x[i])) +
                        0.2 * np.cos(x[i] * 1.8 + 0.1 * np.cos(9 * x[i])))
            
        # Highly multimodal component with chaotic frequency modulation
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(4 * x[i]) + 
                           0.8 * np.sin(7 * x[i]) + 
                           0.5 * np.cos(5 * x[i]) + 
                           0.3 * np.sin(10 * x[i]) +
                           0.2 * np.cos(9 * x[i]) +
                           0.1 * np.sin(13 * x[i]))
            
        # Additional chaotic interaction terms with fractional exponents
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.15 * (np.sin(x[i]**1.2 * x[j]**0.8 * 0.7) + 
                                             0.08 * np.cos(x[i]**0.9 * x[j]**1.1 * 3)) * (i + j + 1)**0.5
        
        # Chaotic periodic modulation based on sum of coordinates with fractional exponent
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.4 * np.sin(0.6 * coord_sum + 0.2 * np.sin(4 * coord_sum)) * np.cos(0.4 * coord_sum + 0.1 * np.cos(6 * coord_sum))
        
        # Add chaotic noise component
        noise = 0.05 * np.random.rand()
        
        # Combine all terms with different weights and chaotic scaling factors
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + noise + 7.0