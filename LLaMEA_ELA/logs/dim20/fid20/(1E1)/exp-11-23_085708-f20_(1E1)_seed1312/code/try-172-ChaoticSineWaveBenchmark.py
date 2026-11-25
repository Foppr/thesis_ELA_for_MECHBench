import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Polynomial distortion component
        poly_distort = np.sum(x_scaled**4) * 0.5 + np.sum(x_scaled**3) * 0.3
        
        # Chaotic sine-wave interactions with dynamic frequencies
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(x[i])
                freq_j = 1.0 + 0.5 * np.cos(x[j])
                chaotic_interaction += np.sin(freq_i * x[i] * freq_j * x[j]) * (i + j + 1) * 0.1
                
        # Dynamic gradient modulation with chaotic components
        grad_mod = 1.0
        for i in range(self.dim):
            chaotic_factor = 1.0 + 0.3 * np.sin(x[i] * 2.0 + np.cos(x[i]))
            grad_mod *= chaotic_factor
            
        # Multi-modal sine-wave component with varying amplitudes
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += (np.sin(2 * x[i]) * (1 + 0.5 * np.sin(x[i])) +
                           0.6 * np.cos(3 * x[i]) * (1 + 0.3 * np.cos(x[i])) +
                           0.4 * np.sin(5 * x[i]) * (1 + 0.2 * np.sin(x[i] * 0.5)) +
                           0.2 * np.cos(7 * x[i]) * (1 + 0.1 * np.cos(x[i] * 0.3)))
            
        # Cross-dimensional coupling with exponential weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = np.exp(-0.1 * (i + j))
                cross_coupling += coupling_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
                
        # Periodic boundary effect with chaotic phase shifts
        boundary_effect = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.5) + np.cos(i * 0.3)
            boundary_effect += (np.sin(x[i] * 0.5 + phase_shift) + 
                              0.5 * np.cos(x[i] * 0.7 + phase_shift)) * 0.2
            
        # Combine all terms with dynamic weights
        result = poly_distort + chaotic_interaction + grad_mod * multi_modal + cross_coupling + boundary_effect
        
        # Add a global scaling factor to ensure proper fitness range
        return result * (1.0 + 0.1 * np.abs(np.sum(x_scaled))) + 3.0