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
        radial_term = r * (1 + 0.8 * np.sin(5.7 * r) + 0.3 * np.cos(7.3 * r) + 
                          0.1 * np.sin(11.9 * r) + 0.05 * np.cos(13.2 * r))
        
        # Chaotic cross-terms with fractional frequencies and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i, freq_j = 2.3 + i*0.1, 3.7 + j*0.15
                cross_term += (np.sin(x[i] * x[j] * freq_i) + 
                              0.5 * np.cos(x[i] * x[j] * freq_j) + 
                              0.3 * np.sin(x[i] * 0.7 * freq_i) * np.cos(x[j] * 0.9 * freq_j) +
                              0.2 * np.cos(x[i] * x[j] * (freq_i + freq_j)) +
                              0.1 * np.sin(x[i] * x[j] * 0.5 * freq_i * freq_j)) * (i + j + 1)
                
        # Dynamic gradient modulation with fractional harmonics
        grad_mod = 1.0
        for i in range(self.dim):
            grad_mod *= (1 + 0.5 * np.sin(x[i] * 0.3 * (1 + 0.1 * i)) + 
                        0.2 * np.cos(x[i] * 0.7 * (1 + 0.05 * i)) + 
                        0.3 * np.sin(x[i] * 1.1 * (1 + 0.08 * i)) +
                        0.1 * np.cos(x[i] * 1.5 * (1 + 0.03 * i)) +
                        0.05 * np.sin(x[i] * 2.3 * (1 + 0.02 * i)))
            
        # Fractional multimodal component with chaotic peaks
        multi_modal = 0.0
        for i in range(self.dim):
            freqs = [3.1, 6.7, 4.2, 9.5, 8.3]
            multi_modal += (np.sin(freqs[0] * x[i]) + 
                           0.7 * np.sin(freqs[1] * x[i]) + 
                           0.4 * np.cos(freqs[2] * x[i]) + 
                           0.2 * np.sin(freqs[3] * x[i]) +
                           0.1 * np.cos(freqs[4] * x[i]) +
                           0.05 * np.sin(12.7 * x[i]) * np.cos(15.3 * x[i]))
            
        # Complex interaction terms with chaotic phase shifts
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.1 * (i - j) * np.sin(0.5 * (i + j))
                    interaction_term += 0.1 * (np.sin(x[i] * x[j] * 0.5 + phase_shift) + 
                                             0.05 * np.cos(x[i] * x[j] * 2 + phase_shift)) * (i + j + 1)
        
        # Dynamic periodic modulation with chaotic frequency
        coord_sum = np.sum(x)
        freq_mod = 0.5 + 0.3 * np.sin(0.3 * coord_sum) * np.cos(0.2 * coord_sum) + \
                   0.2 * np.sin(0.7 * coord_sum) * np.cos(0.4 * coord_sum)
        periodic_mod = 1.0 + freq_mod
        
        # Add a chaotic twist with a dynamic scaling factor based on all coordinates
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= (1 + 0.1 * np.sin(x[i] * 2.7) * np.cos(x[i] * 1.3))
            
        # Combine all terms with different weights and chaotic scaling
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + chaos_factor + 5.0