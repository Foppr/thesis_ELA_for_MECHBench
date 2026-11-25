import numpy as np

class PolynomialGaussianCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial potential terms with varying degrees
        polynomial_term = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**6) + 0.3 * np.sum(x_scaled**8)
        
        # Gaussian ridge structures along diagonal directions
        gaussian_ridge = 0.0
        for i in range(self.dim):
            # Create ridges along different diagonal directions
            ridge_value = np.sum(x_scaled[:i+1]**2) / (i + 1)
            gaussian_ridge += np.exp(-3.0 * ridge_value) * np.cos(2.0 * np.sum(x_scaled[:i+1]))
        
        # Trigonometric correlation terms between pairs of dimensions
        trig_correlation = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Correlation with varying frequency based on dimension indices
                freq_i = 1.0 + 0.2 * (i + 1)
                freq_j = 1.0 + 0.2 * (j + 1)
                trig_correlation += np.sin(freq_i * x_scaled[i]) * np.cos(freq_j * x_scaled[j])
        
        # Cross-dimensional interaction with exponentially decaying weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.5 * (i + j))
                cross_interaction += weight * (x_scaled[i]**2 + x_scaled[j]**2) * \
                                   np.sin(3.0 * x_scaled[i] * x_scaled[j])
        
        # Multimodal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (np.sin(8.0 * x_scaled[i]) + 
                          0.5 * np.sin(16.0 * x_scaled[i]) + 
                          0.3 * np.sin(24.0 * x_scaled[i]))
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_modulation = (1.0 + 0.5 * np.sin(5.0 * r)) * np.exp(-r**2 / 2.0)
        
        # Combined landscape with carefully balanced weights
        return 1.2 * polynomial_term + 0.9 * gaussian_ridge + 0.7 * trig_correlation + \
               0.8 * cross_interaction + 0.6 * multimodal + 0.5 * radial_modulation + 2.1