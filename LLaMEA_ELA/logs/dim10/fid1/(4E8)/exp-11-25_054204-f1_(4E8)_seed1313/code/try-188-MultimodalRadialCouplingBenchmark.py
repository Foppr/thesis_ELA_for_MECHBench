import numpy as np

class MultimodalRadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights and coupling coefficients with enhanced chaos
        self.radial_weights = np.exp(-np.arange(dim) / (dim + 1))
        self.coupling_coeffs = np.sin(np.linspace(0, np.pi, dim)) * 0.5 + 0.5
        # Add chaotic modulation for increased complexity
        self.chaotic_mod = np.random.uniform(0.8, 1.2, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial component with fractal-like behavior
        radial_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(4.0 * x) * self.chaotic_mod)
        
        # Sinusoidal oscillations with chaotic frequency modulation
        sin_term = np.sum(np.sin(2.5 * x) * np.cos(1.8 * x) * np.exp(-0.15 * x**2) * self.chaotic_mod)
        
        # Cross-dimensional coupling with fractal coupling strength
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += self.coupling_coeffs[i] * np.sin(x[i] + x[i+1]) * np.cos(x[i] * x[i+1])
        coupling_term = 0.4 * coupling
        
        # Enhanced multimodal component with multiple local minima and saddle points
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x[i]**4 - 12 * x[i]**2 + 8 * x[i]) * np.cos(0.7 * x[i]) * self.chaotic_mod[i]
        multimodal_term = 0.3 * multimodal
        
        # RBF component with chaotic width variation
        rbf = 0.0
        for i in range(self.dim):
            width1 = 0.4 + i * 0.08 * self.chaotic_mod[i]
            width2 = 0.3 + i * 0.05 * self.chaotic_mod[i]
            rbf += np.exp(-0.5 * ((x[i] - 1.0)**2) / width1) + \
                   np.exp(-0.5 * ((x[i] + 1.0)**2) / width2)
        rbf_term = 0.5 * rbf
        
        # Saddle point structure with enhanced chaotic polynomial terms
        saddle = 0.0
        for i in range(self.dim):
            saddle += x[i]**3 * np.sin(2.2 * x[i]) + x[i]**2 * np.cos(1.7 * x[i]) * self.chaotic_mod[i]
        saddle_term = 0.2 * saddle
        
        # Fractal-like conditioning term
        fractal_cond = 0.0
        for i in range(self.dim):
            fractal_cond += (x[i]**5 - 8 * x[i]**3 + 12 * x[i]) * np.sin(0.3 * x[i])
        fractal_term = 0.15 * fractal_cond
        
        # Combined function with enhanced dimensionality scaling and chaos
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.05 * np.sum(self.chaotic_mod)
        
        return scale_factor * (radial_term + sin_term + coupling_term + multimodal_term + rbf_term + saddle_term + fractal_term)