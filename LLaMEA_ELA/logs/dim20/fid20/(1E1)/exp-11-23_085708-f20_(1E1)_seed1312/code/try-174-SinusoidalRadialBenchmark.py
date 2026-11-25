import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Enhanced radial component with chaotic frequency modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = r * (1 + 0.8 * np.sin(5 * r) + 0.3 * np.cos(7 * r) + 
                          0.1 * np.sin(11 * r) + 0.05 * np.cos(13 * r) + 
                          0.02 * np.sin(17 * r))
        
        # Chaotic cross-terms with fractional frequencies and dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(i * 0.7)
                freq_j = 1.0 + 0.3 * np.cos(j * 0.9)
                cross_term += (np.sin(x[i] * x[j] * freq_i) + 
                              0.5 * np.cos(x[i] * x[j] * freq_j) + 
                              0.3 * np.sin(x[i] * 0.7 * freq_i) * np.cos(x[j] * 0.9 * freq_j) +
                              0.2 * np.cos(x[i] * x[j] * (freq_i + freq_j)) +
                              0.1 * np.sin(x[i] * x[j] * 0.3 * freq_i * freq_j)) * (i + j + 1)
                
        # Dynamic amplitude modulation with fractional powers
        grad_mod = 1.0
        for i in range(self.dim):
            amp_factor = 1.0 + 0.5 * np.sin(x[i] * 0.3) + 0.2 * np.cos(x[i] * 0.7) + 0.3 * np.sin(x[i] * 1.1)
            grad_mod *= (1 + amp_factor * (np.abs(x[i]) ** 0.7) * np.cos(x[i] * 1.5))
            
        # Highly multimodal component with fractional frequencies and dynamic scaling
        multi_modal = 0.0
        for i in range(self.dim):
            freqs = [3, 6, 4, 9, 8, 12, 5, 10]
            scales = [1.0, 0.7, 0.4, 0.2, 0.1, 0.05, 0.3, 0.15]
            for freq, scale in zip(freqs, scales):
                multi_modal += scale * np.sin(freq * x[i] + 0.1 * i) + \
                              scale * 0.7 * np.cos(freq * x[i] + 0.2 * i)
            
        # Complex interaction terms with fractional exponents and dynamic coefficients
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coeff = (i + j + 1) * (0.1 + 0.05 * np.sin(i * 0.5) * np.cos(j * 0.3))
                    interaction_term += coeff * (np.sin(x[i] * x[j] * 0.5) ** 1.2 + 
                                              0.05 * np.cos(x[i] * x[j] * 2) ** 0.8) * \
                                      (np.abs(x[i]) ** 0.3 + np.abs(x[j]) ** 0.4)
        
        # Extremely chaotic periodic modulation with multiple interacting frequencies
        coord_sum = np.sum(x)
        periodic_mod = 1.0 + 0.3 * np.sin(0.5 * coord_sum) * np.cos(0.3 * coord_sum) + \
                      0.15 * np.sin(0.8 * coord_sum) * np.cos(0.6 * coord_sum) + \
                      0.1 * np.cos(1.2 * coord_sum) * np.sin(0.9 * coord_sum)
        
        # Add a chaotic twist with a dynamic scaling factor based on all coordinates
        chaos_factor = 1.0
        for i in range(self.dim):
            chaos_factor *= (1 + 0.2 * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5))
            
        # Combine all terms with dynamic weights
        return radial_term + cross_term + grad_mod * multi_modal + interaction_term + periodic_mod + chaos_factor + 5.0