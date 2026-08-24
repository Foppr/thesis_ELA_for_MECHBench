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
        self.chaos_factor = 3.2
        self.oscillation_freq = 4.0
        # Adaptive noise
        self.noise_level = 0.2
        # Interaction strength
        self.interaction_strength = 1.5
        # New ruggedness parameters
        self.ruggedness_factor = 2.1
        self.saddle_strength = 1.2
        self.cross_dim_coupling = 0.9
        # Additional complexity terms
        self.interference_factor = 1.8
        self.fractal_dim = 1.5
        self.adaptive_saddle = 0.8
        
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
            
        # Add higher-order cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                interaction = (x_scaled[i]**4) * (x_scaled[j]**3) * np.cos(0.7 * x_scaled[i] + 0.5 * x_scaled[j])
                f_val += self.interaction_strength * interaction
                
        # Add fractal-like dimensionality reduction effects
        fractal_effect = 0.0
        for i in range(self.dim):
            fractal_effect += np.sin((i + 1) * 0.9 * x_scaled[i]) * np.cos((i + 1) * 0.6 * x_scaled[i])
        f_val += 1.2 * fractal_effect**3
        
        # Add stochastic perturbation with adaptive variance
        noise = np.random.normal(0, self.noise_level, self.dim)
        stochastic_term = np.sum(noise * np.sin(x_scaled))
        f_val += stochastic_term
        
        # Add a global minimum bias
        f_val += 0.08 * np.sum(np.abs(x_scaled))
        
        # Add ruggedness through saddle point contributions
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += self.saddle_strength * np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        f_val += self.ruggedness_factor * saddle_term**3
        
        # Add cross-dimensional coupling effects that create complex interaction landscapes
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += self.cross_dim_coupling * np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.15 * (x_scaled[i] - x_scaled[j])**2)
        f_val += cross_coupling
        
        # Add interference terms
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += self.interference_factor * np.sin(2.0 * x_scaled[i] + 1.5 * x_scaled[j]) * np.cos(1.0 * x_scaled[i] - 0.8 * x_scaled[j])
        f_val += interference
        
        # Add adaptive saddle point effects
        adaptive_saddle_term = 0.0
        for i in range(self.dim):
            adaptive_saddle_term += self.adaptive_saddle * np.sin(1.5 * x_scaled[i]) * np.cos(1.2 * x_scaled[i]) * np.sin(0.5 * x_scaled[i]**2)
        f_val += adaptive_saddle_term
        
        return f_val