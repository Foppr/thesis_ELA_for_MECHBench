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
        
        # Chaotic cross-terms with quantum phase interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum phase interaction terms
                phase_i = np.sin(x[i] * x[j] * 2)
                phase_j = np.cos(x[i] * x[j] * 3)
                quantum_interaction = phase_i * phase_j * np.sin((x[i] + x[j]) * 0.5)
                cross_term += (phase_i + 0.5 * phase_j + 
                              0.3 * np.sin(x[i] * 0.7) * np.cos(x[j] * 0.9) +
                              0.2 * np.cos(x[i] * x[j] * 4) + 
                              quantum_interaction) * (i + j + 1) * np.sin(i * j * 0.1)
                
        # Fractal adaptive gradient modulation with multiple chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3) + 
                        0.2 * np.cos(x[i] * 0.7) + 
                        0.3 * np.sin(x[i] * 1.1) +
                        0.1 * np.cos(x[i] * 1.5) +
                        0.05 * np.sin(x[i] * 2.3) * np.cos(x[i] * 3.7))
            
        # Ultra-multimodal component with fractal frequency scaling
        multi_modal = 0.0
        frequencies = [3, 6, 4, 9, 8, 12, 5, 15, 7, 18]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            multi_modal += (np.sin(frequencies[freq_idx] * x[i]) + 
                           0.7 * np.sin(2 * frequencies[freq_idx] * x[i]) + 
                           0.4 * np.cos(frequencies[freq_idx] * x[i]) + 
                           0.2 * np.sin(3 * frequencies[freq_idx] * x[i]) +
                           0.1 * np.cos(4 * frequencies[freq_idx] * x[i]) +
                           0.05 * np.sin(7 * frequencies[freq_idx] * x[i]))
            
        # Complex interaction terms with fractal scaling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Fractal interaction with varying weights
                    weight = (i + j + 1) * np.sin(i * 0.2) * np.cos(j * 0.3)
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5) + 
                                             0.05 * np.cos(x[i] * x[j] * 2) +
                                             0.02 * np.sin(x[i] * x[j] * 0.3) * np.cos(x[i] * 0.8)) * weight
        
        # Chaotic periodic modulation with fractal phase
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                       0.1 * np.sin(coord_sum * 0.1) * np.cos(coord_sum * 0.2) * np.sin(coord_sum * 0.05)
        
        # Add fractal-like noise component
        noise = 0.05 * np.sum(np.sin(x * 10) * np.cos(x * 7))
        
        # Combine all terms with different weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + noise + 5.0