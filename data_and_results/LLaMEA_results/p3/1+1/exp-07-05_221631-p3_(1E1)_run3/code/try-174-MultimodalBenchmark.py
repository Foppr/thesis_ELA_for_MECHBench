import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for each dimension
        np.random.seed(42)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 7))
        # Dimensional scaling factors
        self.scaling_factors = np.random.uniform(0.3, 4.0, dim)
        # Chaos parameters
        self.chaos_factor = 3.0
        self.oscillation_freq = 4.0
        # Adaptive noise
        self.noise_level = 0.2
        # Interaction strength
        self.interaction_strength = 1.5
        # New fractal-like components
        self.fractal_amplitude = 1.2
        self.fractal_frequency = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply dimensional scaling
        x_scaled = x * self.scaling_factors
        
        # Base polynomial term with chaos
        f_val = np.sum(x_scaled**2)
        
        # Add polynomial chaos expansion terms
        for i in range(self.dim):
            poly_term = np.sum(self.poly_coeffs[i] * np.array([x_scaled[i]**j for j in range(7)]))
            f_val += self.chaos_factor * poly_term * np.sin(self.oscillation_freq * x_scaled[i])
            
        # Add higher-order cross-dimensional interactions with new pattern
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = (x_scaled[i]**4) * (x_scaled[j]**3) * np.cos(0.6 * x_scaled[i] + 0.4 * x_scaled[j])
                f_val += self.interaction_strength * interaction
                
        # Add fractal-like dimensionality reduction effects with new formula
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += self.fractal_amplitude * np.sin(self.fractal_frequency * (i + 1) * x_scaled[i]) * np.cos(self.fractal_frequency * (i + 1) * x_scaled[i])
        f_val += 0.6 * fractal_effect**3
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += stochastic_term
        
        # Add a global minimum bias with enhanced penalty
        f_val += 0.1 * np.sum(np.abs(x_scaled)**1.5)
        
        # Add new multi-modal component with different frequency
        multi_modal = 0.0
        for i in range(self.dim):
            multi_modal += np.sin(2.5 * x_scaled[i]) * np.cos(1.5 * x_scaled[i])
        f_val += 0.3 * multi_modal**2
        
        return f_val