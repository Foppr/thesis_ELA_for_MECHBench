import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.8, (15,))
        # Initialize sinusoidal parameters with higher frequency components
        self.sin_freq = np.random.uniform(2.0, 8.0, dim)
        self.sin_amp = np.random.uniform(0.8, 2.5, dim)
        # Initialize polynomial coefficients for coupling with higher order terms
        self.poly_coeffs = np.random.normal(0.0, 1.5, (dim, 5))
        # Initialize interaction matrix with stronger coupling
        self.interaction_matrix = np.random.uniform(-1.5, 1.5, (dim, dim))
        np.fill_diagonal(self.interaction_matrix, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced Radial basis function component with more centers
        rbf_sum = 0
        for i in range(15):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[i, j]
                rbf_term += diff**2
            rbf_sum += np.exp(-0.5 * rbf_term / (self.rbf_widths[i]**2))
        
        # Enhanced Sinusoidal component with higher amplitude and frequency
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i])
        
        # Enhanced Polynomial coupling component with higher order terms
        poly_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] + 
                        self.poly_coeffs[i, 1] * x_i + 
                        self.poly_coeffs[i, 2] * x_i**2 + 
                        self.poly_coeffs[i, 3] * x_i**3 +
                        self.poly_coeffs[i, 4] * x_i**4)
            poly_sum += poly_term
        
        # Enhanced Cross-dimension interaction with sinusoidal coupling and quadratic terms
        interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_matrix[i, j] * np.sin(x[i]) * x[j]**2
        
        # Add a new component: Gaussian peaks with varying heights
        gaussian_peaks = 0
        peak_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        peak_heights = np.random.uniform(1.0, 3.0, (5,))
        for i in range(5):
            peak_term = 0
            for j in range(self.dim):
                diff = x[j] - peak_centers[i, j]
                peak_term += diff**2
            gaussian_peaks += peak_heights[i] * np.exp(-0.5 * peak_term / 4.0)
        
        # Combine all components with adjusted weights
        result = (2.0 * rbf_sum + 
                 1.5 * sin_sum + 
                 1.0 * poly_sum + 
                 0.8 * interaction +
                 0.5 * gaussian_peaks)
        
        return result