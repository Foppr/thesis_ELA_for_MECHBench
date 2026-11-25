import numpy as np

class MultimodalSinusoidalRBF:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for enhanced sinusoidal components
        self.sin_freq = np.random.uniform(2.0, 10.0, dim)
        self.sin_amp = np.random.uniform(0.8, 4.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for modified radial basis functions
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, dim)
        self.rbf_weights = np.random.uniform(-1.5, 1.5, dim)
        # Initialize augmented polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Add higher-order polynomial terms with different exponents
        self.poly_exponents = np.random.uniform(2.0, 6.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced sinusoidal components
        for i in range(self.dim):
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i]) * np.cos(0.5 * x[i])
            
        # Modified radial basis functions
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2)) * (1 + 0.1 * np.sin(x[j]))
            result += self.rbf_weights[i] * rbf_sum
            
        # Augmented polynomial interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.poly_coeffs[i][j] * x[i]**(0.5 + 0.5 * np.sin(x[j])) * x[j]**(0.5 + 0.5 * np.cos(x[i]))
                result += interaction
                
        # Higher-order polynomial terms with varying exponents
        for i in range(self.dim):
            result += 0.15 * x[i]**self.poly_exponents[i] - 0.4 * x[i]**3 + 0.15 * x[i]**2
            
        # Add multi-scale noise term to increase complexity
        noise = np.random.normal(0, 0.08, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.cos(3 * np.pi * x[i]) * np.sin(2 * np.pi * x[i])
            
        return result