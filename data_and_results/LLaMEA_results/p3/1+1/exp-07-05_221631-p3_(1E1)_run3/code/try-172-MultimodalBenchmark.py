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
        # Additional refinement parameters
        self.fractal_strength = 0.8
        self.min_bias = 0.05
        self.stochastic_weight = 0.3
        
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
            
        # Add higher-order cross-dimensional interactions with improved structure
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Improved interaction with non-linear coupling
                interaction = (x_scaled[i]**2) * (x_scaled[j]**3) * np.cos(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                f_val += self.interaction_strength * interaction
                
        # Add fractal-like dimensionality reduction effects with enhanced non-linearity
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += np.sin((i + 1) * 0.7 * x_scaled[i]) * np.cos((i + 1) * 0.4 * x_scaled[i])
        f_val += self.fractal_strength * fractal_effect**3  # Changed from square to cube for more complexity
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += self.stochastic_weight * stochastic_term
        
        # Add a global minimum bias with modified weighting
        f_val += self.min_bias * np.sum(np.abs(x_scaled)**0.5)  # Changed to fractional power for smoother landscape
        
        return f_val