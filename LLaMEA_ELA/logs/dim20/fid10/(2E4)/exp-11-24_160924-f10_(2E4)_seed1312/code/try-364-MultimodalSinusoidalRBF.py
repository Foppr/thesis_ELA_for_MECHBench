import numpy as np

class MultimodalSinusoidalRBF:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for sinusoidal components
        self.sin_freq = np.random.uniform(1.0, 8.0, dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, dim)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Sinusoidal components
        for i in range(self.dim):
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            
        # Radial basis functions
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_sum
            
        # Polynomial interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.poly_coeffs[i][j] * x[i] * x[j]
                result += interaction
                
        # Add higher-order polynomial terms
        for i in range(self.dim):
            result += 0.1 * x[i]**4 - 0.5 * x[i]**3 + 0.2 * x[i]**2
            
        # Add noise term to increase complexity
        noise = np.random.normal(0, 0.05, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.cos(2 * np.pi * x[i])
            
        return result