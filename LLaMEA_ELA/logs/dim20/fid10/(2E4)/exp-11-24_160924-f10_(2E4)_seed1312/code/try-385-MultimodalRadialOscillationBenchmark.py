import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for enhanced sinusoidal components
        self.sin_freq = np.random.uniform(2.0, 10.0, dim)
        self.sin_amp = np.random.uniform(1.0, 4.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, dim)
        self.rbf_weights = np.random.uniform(-1.5, 1.5, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Additional parameters for enhanced complexity
        self.oscillation_amplitude = np.random.uniform(0.5, 2.0, dim)
        self.oscillation_frequency = np.random.uniform(1.0, 6.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced sinusoidal components with oscillation
        for i in range(self.dim):
            # Base sinusoidal term
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            # Additional oscillation component
            result += self.oscillation_amplitude[i] * np.cos(self.oscillation_frequency[i] * x[i])
            
        # Modified radial basis functions with Gaussian-like behavior
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_sum
            
        # Enhanced polynomial interactions with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.poly_coeffs[i][j] * x[i] * x[j]
                result += interaction
                
        # Add higher-order polynomial terms with different exponents
        for i in range(self.dim):
            result += 0.15 * x[i]**4 - 0.6 * x[i]**3 + 0.3 * x[i]**2 + 0.05 * x[i]
            
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * x[i]**2 * x[j] + 0.03 * x[i] * x[j]**2
                
        # Add a global scaling factor to increase complexity
        result *= (1.0 + 0.1 * np.sum(np.sin(x)))
        
        return result