import numpy as np

class NovelChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.coupling_strength = 0.85
        self.gaussian_width = 1.6
        self.polynomial_weight = 1.2
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quartic polynomial potential with varying coefficients and dimensionality influence
        poly_sum = 0
        for i in range(self.dim):
            coeff = 1.1 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
            poly_sum += coeff * (x[i] ** 4) * (1 + 0.12 * np.cos(i * 0.6))
            
        # Gaussian radial basis function component with dynamic centers and widths
        rbf_sum = 0
        for i in range(self.dim):
            center = 1.8 * np.sin(i * np.pi / (self.dim + 3))
            width = self.gaussian_width * (1 + 0.1 * np.cos(i * 0.7))
            distance = (x[i] - center) ** 2
            rbf_sum += np.exp(-distance / (2 * width ** 2))
            
        # Sine-based chaotic mapping with dynamic frequency modulation and phase shifting
        chaotic_sum = 0
        for i in range(self.dim):
            freq_mod = 2.3 + 1.6 * np.sin(i * np.pi / (self.dim + 3))
            phase_shift = 0.5 * np.cos(i * np.pi / (self.dim + 4))
            chaotic_val = np.sin(freq_mod * x[i] + phase_shift) + 0.7 * np.sin(2 * freq_mod * x[i] + phase_shift)
            chaotic_sum += chaotic_val ** 2
            
        # Enhanced adaptive coupling between dimensions with multiple interaction types
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling scope for better conditioning
                interaction1 = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                interaction2 = (x[i] - x[j]) ** 2 * np.exp(-0.25 * (x[i] + x[j]) ** 2)
                interaction3 = np.tanh(x[i] * x[j]) * np.sin(0.35 * (x[i]**2 + x[j]**2))
                coupling_sum += self.coupling_strength * (interaction1 + interaction2 + interaction3) ** 2
                
        # Multi-frequency sinusoidal modulation with dynamic scaling and adaptive phase
        mod_sum = 0
        for i in range(self.dim):
            freq_factor = 1.6 + 1.3 * np.sin(i * np.pi / (self.dim + 5))
            scale_factor = 1.0 + 0.35 * np.cos(i * np.pi / (self.dim + 6))
            phase_factor = 0.2 * np.sin(i * np.pi / (self.dim + 7))
            mod_val = scale_factor * (np.sin(freq_factor * x[i] + phase_factor) + 
                                    0.55 * np.cos(2 * freq_factor * x[i] + phase_factor) +
                                    0.35 * np.sin(3 * freq_factor * x[i] + phase_factor))
            mod_sum += mod_val ** 2
            
        # Additional higher-order interaction terms for increased complexity
        high_order_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+3, self.dim)):
                    high_order_sum += (x[i] * x[j] * x[k]) ** 2 * np.exp(-0.1 * (x[i]**2 + x[j]**2 + x[k]**2))
        
        # Enhanced dimensionality-dependent scaling and conditioning
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weighting
        total = (self.polynomial_weight * poly_sum + 
                0.85 * rbf_sum + 
                1.25 * chaotic_sum + 
                0.65 * coupling_sum + 
                0.95 * mod_sum + 
                0.3 * high_order_sum) * dim_factor
        
        # Add small constant to prevent flat regions and ensure global minimum
        return total + 0.07 * self.dim