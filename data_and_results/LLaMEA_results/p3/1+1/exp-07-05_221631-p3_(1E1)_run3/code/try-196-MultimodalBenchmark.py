import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for each dimension
        np.random.seed(42)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Dimensional scaling factors - slightly altered
        self.scaling_factors = np.random.uniform(0.6, 3.2, dim)
        # Chaos parameters - slightly altered
        self.chaos_factor = 2.8
        self.oscillation_freq = 3.5
        # Adaptive noise
        self.noise_level = 0.18
        # Interaction strength - slightly altered
        self.interaction_strength = 1.5
        # New ruggedness parameters
        self.ruggedness_factor = 2.1
        self.saddle_strength = 1.1
        self.cross_dim_coupling = 0.8
        # Logistic map component for added chaos
        self.logistic_r = 3.95
        
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
            
        # Add higher-order cross-dimensional interactions with modified exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = (x_scaled[i]**2.5) * (x_scaled[j]**1.8) * np.cos(0.6 * x_scaled[i] + 0.4 * x_scaled[j])
                f_val += self.interaction_strength * interaction
                
        # Add fractal-like dimensionality reduction effects
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += np.sin((i + 1) * 0.8 * x_scaled[i]) * np.cos((i + 1) * 0.5 * x_scaled[i])
        f_val += 0.9 * fractal_effect**2
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += stochastic_term
        
        # Add a global minimum bias
        f_val += 0.06 * np.sum(np.abs(x_scaled))
        
        # Add ruggedness through saddle point contributions with logistic map
        saddle_term = 0.0
        for i in range(self.dim):
            # Introduce logistic map for chaotic saddle contributions
            logistic_val = self.logistic_r * np.sin(x_scaled[i]) * (1 - np.sin(x_scaled[i]))
            saddle_term += self.saddle_strength * np.sin(2.0 * x_scaled[i]) * np.cos(1.5 * x_scaled[i]) * logistic_val
        f_val += self.ruggedness_factor * saddle_term**2
        
        # Add cross-dimensional coupling effects that create complex interaction landscapes
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += self.cross_dim_coupling * np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.15 * (x_scaled[i] - x_scaled[j])**2)
        f_val += cross_coupling
        
        return f_val