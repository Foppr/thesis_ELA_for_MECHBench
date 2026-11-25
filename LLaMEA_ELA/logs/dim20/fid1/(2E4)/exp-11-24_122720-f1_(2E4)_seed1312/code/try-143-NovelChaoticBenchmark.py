import numpy as np

class NovelChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_strength = 0.8
        self.gaussian_width = 2.0
        self.polynomial_weight = 1.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quartic polynomial potential with varying coefficients and dimensionality influence
        poly_sum = 0
        for i in range(self.dim):
            coeff = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
            poly_sum += coeff * (x[i] ** 4) * (1 + 0.2 * np.cos(i))
            
        # Gaussian radial basis function component with dynamic centers and widths
        rbf_sum = 0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 1))
            width = self.gaussian_width * (1 + 0.1 * np.cos(i))
            distance = (x[i] - center) ** 2
            rbf_sum += np.exp(-distance / (2 * width ** 2))
            
        # Sine-based chaotic mapping with dynamic frequency modulation and phase shifting
        chaotic_sum = 0
        for i in range(self.dim):
            freq_mod = 3.0 + 1.5 * np.sin(i * np.pi / (self.dim + 3))
            phase_shift = 0.5 * np.cos(i * np.pi / (self.dim + 4))
            chaotic_val = np.sin(freq_mod * x[i] + phase_shift) + 0.7 * np.sin(2 * freq_mod * x[i] + phase_shift)
            chaotic_sum += chaotic_val ** 2
            
        # Adaptive coupling between dimensions with multiple interaction types
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling scope
                interaction1 = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                interaction2 = (x[i] - x[j]) ** 2 * np.exp(-0.5 * (x[i] + x[j]) ** 2)
                interaction3 = np.tanh(x[i] * x[j]) * np.sin(0.5 * (x[i]**2 + x[j]**2))
                coupling_sum += self.coupling_strength * (interaction1 + interaction2 + interaction3) ** 2
                
        # Multi-frequency sinusoidal modulation with dynamic scaling and adaptive phase
        mod_sum = 0
        for i in range(self.dim):
            freq_factor = 2.0 + 1.2 * np.sin(i * np.pi / (self.dim + 5))
            scale_factor = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 6))
            phase_factor = 0.3 * np.sin(i * np.pi / (self.dim + 7))
            mod_val = scale_factor * (np.sin(freq_factor * x[i] + phase_factor) + 
                                    0.5 * np.cos(2 * freq_factor * x[i] + phase_factor) +
                                    0.3 * np.sin(3 * freq_factor * x[i] + phase_factor))
            mod_sum += mod_val ** 2
            
        # Dimensionality-dependent scaling and conditioning
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weighting
        total = (self.polynomial_weight * poly_sum + 
                0.8 * rbf_sum + 
                1.2 * chaotic_sum + 
                0.6 * coupling_sum + 
                0.9 * mod_sum) * dim_factor
        
        # Add small constant to prevent flat regions and ensure global minimum
        return total + 0.1 * self.dim