import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with chaotic centers
        rbf_sum = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(self.chaotic_sequence[i] * np.pi)  # Chaotic center positioning
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / (1.0 + 0.1 * self.chaotic_sequence[i]))**2)
        
        # Sinusoidal oscillation with dynamic frequency modulation
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.abs(np.sin(self.chaotic_sequence[i] * 2.0))  # Dynamic frequency
            sin_sum += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Cross-dimensional interaction with chaotic coupling weights
        cross_term = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(self.chaotic_sequence[i] * 3.0)  # Chaotic coupling
            cross_term += weight * (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Polynomial chaos with fractal-like behavior
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += (x[i]**5) * np.cos(2.0 * x[i]) * (1.0 + 0.2 * self.chaotic_sequence[i])
        
        # Sigmoidal modulation with chaotic scaling
        sig_sum = 0.0
        for i in range(self.dim):
            sig_sum += (1.0 / (1.0 + np.exp(-x[i]))) * np.sin(3.0 * x[i] + self.chaotic_sequence[i])
        
        # Logarithmic chaotic component
        log_sum = 0.0
        for i in range(self.dim):
            log_sum += np.log(1.0 + np.abs(x[i])) * np.cos(2.5 * x[i])
        
        # Fractal-like coupling with multiple interaction terms
        fractal_term = 0.0
        for i in range(self.dim - 2):
            fractal_term += np.sin(x[i] * x[i+1] * x[i+2]) * (1.0 + 0.1 * self.chaotic_sequence[i])
        
        # Combined function with dimensionality-dependent scaling
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Additional multimodal component
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.exp(-x[i]**2 / 10.0)
        
        # Final function value with refined weights
        return scale_factor * (0.8 * rbf_sum + 0.6 * sin_sum + 0.5 * cross_term + 
                              0.4 * poly_sum + 0.3 * sig_sum + 0.2 * log_sum + 
                              0.3 * fractal_term + 0.4 * multi_modal)