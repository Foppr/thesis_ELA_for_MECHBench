import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for each dimension
        np.random.seed(42)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Dimensional scaling factors
        self.scaling_factors = np.random.uniform(0.5, 3.0, dim)
        # Chaos parameters
        self.chaos_factor = 2.5
        self.oscillation_freq = 3.0
        # Adaptive noise
        self.noise_level = 0.15
        # Interaction strength
        self.interaction_strength = 1.2
        # Additional complexity parameters
        self.fractal_intensity = 0.8
        self.cross_term_power = 2.5
        self.minimum_bias = 0.03
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply dimensional scaling
        x_scaled = x * self.scaling_factors
        
        # Base polynomial term with chaos
        f_val = np.sum(x_scaled**2)
        
        # Add polynomial chaos expansion terms
        for i in range(self.dim):
            poly_term = np.sum(self.poly_coeffs[i] * np.array([x_scaled[i]**j for j in range(5)]))
            f_val += self.chaos_factor * poly_term * np.sin(self.oscillation_freq * x_scaled[i])
            
        # Add higher-order cross-dimensional interactions with modified power
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = (x_scaled[i]**self.cross_term_power) * (x_scaled[j]**(self.cross_term_power/2)) * np.cos(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                f_val += self.interaction_strength * interaction
                
        # Add fractal-like dimensionality reduction effects with enhanced intensity
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += np.sin((i + 1) * 0.7 * x_scaled[i]) * np.cos((i + 1) * 0.4 * x_scaled[i])
        f_val += self.fractal_intensity * fractal_effect**2
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += stochastic_term
        
        # Add a global minimum bias with reduced magnitude
        f_val += self.minimum_bias * np.sum(np.abs(x_scaled))
        
        # Add a secondary multimodal component to increase complexity
        secondary_component = 0.0
        for i in range(self.dim):
            secondary_component += np.sin(2.0 * x_scaled[i]) * np.cos(1.5 * x_scaled[i])
        f_val += 0.3 * secondary_component**2
        
        return f_val