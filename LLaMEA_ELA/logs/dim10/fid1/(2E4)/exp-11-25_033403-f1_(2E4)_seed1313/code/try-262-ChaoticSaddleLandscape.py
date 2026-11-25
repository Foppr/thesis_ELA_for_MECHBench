import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.well_depths = np.random.uniform(1.0, 5.0, dim)
        self.well_positions = np.random.uniform(-4.0, 4.0, dim)
        self.well_widths = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strength = np.random.uniform(0.5, 3.0, (dim, dim))
        self.hyperbolic_params = np.random.uniform(1.0, 4.0, dim)
        self.resonance_freq = np.random.uniform(0.2, 3.0, dim)
        self.stochastic_amplitude = np.random.uniform(0.02, 0.3, dim)
        self.saddle_indices = np.random.choice(dim, size=min(4, dim), replace=False)
        self.scale_factors = np.random.uniform(0.8, 2.5, dim)
        # Add enhanced cubic nonlinearities
        self.cubic_coefficients = np.random.uniform(0.15, 0.6, dim)
        # Add fractal scaling parameters
        self.fractal_exponents = np.random.uniform(1.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add exponential potential wells
        for i in range(self.dim):
            well_potential = self.well_depths[i] * np.exp(-0.5 * ((x[i] - self.well_positions[i]) / self.well_widths[i])**2)
            fitness -= well_potential
            
        # Add enhanced hyperbolic coupling between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.coupling_strength[i, j] * np.tanh(self.hyperbolic_params[i] * x[i]) * np.tanh(self.hyperbolic_params[j] * x[j])
                coupling_terms += coupling
                
        # Add stochastic resonance terms
        stochastic_terms = 0.0
        for i in range(self.dim):
            stochastic = self.stochastic_amplitude[i] * np.sin(self.resonance_freq[i] * x[i] + np.random.uniform(0, 2*np.pi))
            stochastic_terms += stochastic
            
        # Add saddle-point contributions
        saddle_terms = 0.0
        for i in self.saddle_indices:
            saddle_term = x[i]**2 * (x[i]**2 - self.scale_factors[i]**2)
            saddle_terms += saddle_term
            
        # Add enhanced multi-scale fractal-like terms
        fractal_terms = 0.0
        for i in range(self.dim):
            scale_sum = 0.0
            for k in range(1, 8):
                scale = self.scale_factors[i] * (2.0**k)
                scale_sum += np.sin(scale * x[i]) / (k**self.fractal_exponents[i])
            fractal_terms += scale_sum
            
        # Add enhanced cubic nonlinear terms
        cubic_terms = 0.0
        for i in range(self.dim):
            cubic_terms += self.cubic_coefficients[i] * x[i]**3
            
        # Combine all components with adjusted weights
        total = 0.25 * fitness + 0.35 * coupling_terms + 0.15 * stochastic_terms + 0.1 * saddle_terms + 0.1 * fractal_terms + 0.05 * cubic_terms
        
        return total