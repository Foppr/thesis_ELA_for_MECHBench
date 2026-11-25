import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize adaptive frequencies for each dimension
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        # Initialize amplitude factors for sinusoidal perturbations
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Initialize cross-dimensional coupling weights
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0.0)
        # Initialize quadratic coefficients
        self.quadratic_coeffs = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute quadratic base term
        quadratic_term = np.sum(self.quadratic_coeffs * x**2)
        
        # Compute sinusoidal perturbations with adaptive frequencies
        sinusoidal_term = 0.0
        for i in range(self.dim):
            # Adaptive frequency modulation based on dimension index
            freq_mod = 1.0 + 0.5 * np.sin(0.5 * np.pi * i / max(1, self.dim - 1))
            sinusoidal_term += self.amplitudes[i] * np.sin(freq_mod * self.frequencies[i] * x[i])
        
        # Compute cross-dimensional coupling terms
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_weights[i, j] * x[i] * x[j]
        
        # Combine all terms with adaptive weighting
        fitness = quadratic_term + 0.5 * sinusoidal_term + 0.3 * coupling_term
        
        # Add a global modulation factor based on the norm of x
        norm_x = np.linalg.norm(x)
        global_modulation = 1.0 + 0.2 * np.sin(2.0 * norm_x)
        
        return fitness * global_modulation