import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractal-like radial component with chaotic sine-wave modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.sin(17 * r**2) + 
                          0.03 * np.cos(13 * r**1.5))
        
        # Chaotic cross-terms with quantum-like interference patterns
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (np.sin(x[i] * x[j] * 2) + 
                              0.5 * np.cos(x[i] * x[j] * 3) + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) +
                              0.1 * np.sin(x[i] * x[j] * 0.5) * np.sin((x[i] + x[j]) * 0.3) +
                              0.05 * np.cos(x[i] * x[j] * 6)) * (i + j + 1) * np.sin(0.1 * (i + j))
                
        # Quantum-inspired gradient modulation with fractal frequency components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.08 * np.sin(x[i] * 2.3) * np.cos(x[i] * 3.7) +
                        0.04 * np.cos(x[i] * 0.9) * np.sin(x[i] * 1.8))
            
        # Highly multimodal component with fractal peak distribution
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(3 * x[i]) + 
                           0.7 * np.sin(6 * x[i]) + 
                           0.4 * np.cos(4 * x[i]) + 
                           0.2 * np.sin(9 * x[i]) +
                           0.1 * np.cos(8 * x[i]) +
                           0.05 * np.sin(12 * x[i]) * np.cos(5 * x[i]) +
                           0.03 * np.cos(15 * x[i]) * np.sin(7 * x[i]))
            
        # Fractal interaction terms with chaotic coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_term += (0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2)) * 
                                       (i + j + 1) * np.sin(0.05 * (i * j + i + j)))
        
        # Chaotic periodic modulation based on coordinate sum with fractal scaling
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                      0.1 * np.sin(0.7 * coord_sum**2) * np.cos(0.4 * coord_sum**1.5)
        
        # Fractal coupling between all dimensions with chaotic weights
        fractal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_coupling += (np.sin(x[i] * x[j] * 0.2) + 
                                   0.3 * np.cos(x[i] * x[j] * 0.8)) * \
                                  (i + j + 1) * np.sin(0.01 * i * j)
        
        # Add a chaotic twist: fractal-like noise component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += 0.02 * np.sin(x[i] * 13.0) * np.cos(x[i] * 7.0) * \
                             np.sin(0.1 * x[i]**2) * np.cos(0.05 * x[i]**3)
        
        # Combine all terms with different weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + \
               periodic_mod + fractal_coupling + noise_component + 5.0