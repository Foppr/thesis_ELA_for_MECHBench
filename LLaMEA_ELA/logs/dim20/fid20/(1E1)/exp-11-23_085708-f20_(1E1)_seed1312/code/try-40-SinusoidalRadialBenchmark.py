import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Enhanced radial component with higher frequency sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r))
        
        # Enhanced cross-terms with multiple frequencies and interaction weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9)) * (i + j + 1)
                
        # Enhanced adaptive gradient modulation with multiple sine components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1))
            
        # Enhanced multimodal component with multiple peaks and frequencies
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]))
            
        # Additional interaction terms between all dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += 0.1 * np.sin(x[i] * x[j] * 0.5) * (i + j + 1)
        
        # Combine all terms with different weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + 5.0