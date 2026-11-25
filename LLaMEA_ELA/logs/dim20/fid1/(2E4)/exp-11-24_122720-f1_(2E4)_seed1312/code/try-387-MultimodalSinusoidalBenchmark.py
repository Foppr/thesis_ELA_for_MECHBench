import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths with more diversity
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (15, dim))
        self.rbf_widths = np.random.uniform(0.2, 3.0, (15,))
        # Initialize sinusoidal parameters with higher frequency components and more harmonics
        self.sin_freq = np.random.uniform(1.5, 10.0, dim)
        self.sin_amp = np.random.uniform(0.5, 4.0, dim)
        # Initialize polynomial coefficients for coupling with higher order terms
        self.poly_coeffs = np.random.normal(0.0, 2.0, (dim, 6))
        # Initialize interaction matrix with stronger coupling weights and non-linear terms
        self.interaction_matrix = np.random.uniform(-2.0, 2.0, (dim, dim))
        np.fill_diagonal(self.interaction_matrix, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced Radial basis function component with modified weighting
        rbf_sum = 0
        for i in range(15):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[i, j]
                rbf_term += diff**2
            rbf_sum += np.exp(-0.4 * rbf_term / (self.rbf_widths[i]**2))
        
        # Enhanced sinusoidal component with additional harmonic terms and non-linear modulation
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += self.sin_amp[i] * (np.sin(self.sin_freq[i] * x[i]) + 
                                         0.4 * np.sin(2 * self.sin_freq[i] * x[i]) + 
                                         0.2 * np.sin(3 * self.sin_freq[i] * x[i]) +
                                         0.1 * np.sin(5 * self.sin_freq[i] * x[i]))
        
        # Enhanced polynomial coupling component with higher order terms and cross-terms
        poly_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] + 
                        self.poly_coeffs[i, 1] * x_i + 
                        self.poly_coeffs[i, 2] * x_i**2 + 
                        self.poly_coeffs[i, 3] * x_i**3 +
                        self.poly_coeffs[i, 4] * x_i**4 +
                        self.poly_coeffs[i, 5] * x_i**5)
            poly_sum += poly_term
        
        # Enhanced cross-dimension interaction with polynomial coupling and non-linear terms
        interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_matrix[i, j] * np.sin(x[i]) * x[j] * (x[j]**3 + x[j] + 1)
        
        # Add a new chaotic component to increase complexity
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.pi) * np.cos(x[i] * np.pi / 2) * (x[i]**2 + 1)
        
        # Combine all components with adjusted weights
        result = (1.8 * rbf_sum + 
                 1.7 * sin_sum + 
                 1.2 * poly_sum + 
                 0.9 * interaction +
                 0.5 * chaotic)
        
        return result