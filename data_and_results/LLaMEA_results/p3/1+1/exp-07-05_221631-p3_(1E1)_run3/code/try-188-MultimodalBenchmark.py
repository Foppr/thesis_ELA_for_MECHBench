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
        self.chaos_factor = 2.8
        self.oscillation_freq = 3.5
        # Adaptive noise
        self.noise_level = 0.12
        # Interaction strength
        self.interaction_strength = 1.5
        # New ruggedness parameters
        self.ruggedness_factor = 2.1
        self.saddle_strength = 1.2
        self.cross_dim_coupling = 0.8
        # Enhanced chaotic coupling
        self.chaotic_coupling = 1.3
        # Adaptive dimensionality scaling
        self.adaptive_scaling = np.random.uniform(0.8, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply dimensional scaling and adaptive scaling
        x_scaled = x * self.scaling_factors * self.adaptive_scaling
        
        # Base polynomial term with chaos
        f_val = np.sum(x_scaled**2)
        
        # Add polynomial chaos expansion terms
        for i in range(self.dim):
            poly_term = np.sum(self.poly_coeffs[i] * np.array([x_scaled[i]**j for j in range(5)]))
            f_val += self.chaos_factor * poly_term * np.sin(self.oscillation_freq * x_scaled[i])
            
        # Add higher-order cross-dimensional interactions with enhanced coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                interaction = (x_scaled[i]**3) * (x_scaled[j]**2) * np.cos(0.5 * x_scaled[i] + 0.3 * x_scaled[j])
                f_val += self.interaction_strength * interaction * np.exp(-0.1 * np.abs(x_scaled[i] - x_scaled[j]))
                
        # Add fractal-like dimensionality reduction effects with chaotic modification
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += np.sin((i + 1) * 0.7 * x_scaled[i]) * np.cos((i + 1) * 0.4 * x_scaled[i])
        f_val += 0.8 * fractal_effect**2 * np.sin(0.5 * np.sum(x_scaled**2))
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += stochastic_term
        
        # Add a global minimum bias
        f_val += 0.05 * np.sum(np.abs(x_scaled))
        
        # Add ruggedness through saddle point contributions with enhanced complexity
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_strength * np.sin(2.0 * x_scaled[i]) * np.cos(1.5 * x_scaled[i]) * np.exp(-0.05 * x_scaled[i]**2)
        f_val += self.ruggedness_factor * saddle_term**2
        
        # Add cross-dimensional coupling effects that create complex interaction landscapes with chaotic influence
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.cross_dim_coupling * np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.1 * (x_scaled[i] - x_scaled[j])**2)
                # Add chaotic modulation to coupling
                coupling *= (1.0 + 0.3 * np.sin(3.0 * x_scaled[i] + 2.0 * x_scaled[j]))
                cross_coupling += coupling
        f_val += cross_coupling
        
        # Add enhanced chaotic coupling between dimensions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_interaction += self.chaotic_coupling * np.sin(x_scaled[i] * x_scaled[j] * 0.5) * np.cos(x_scaled[i] + x_scaled[j])
        f_val += chaotic_interaction * np.exp(-0.1 * np.sum(x_scaled**2))
        
        return f_val