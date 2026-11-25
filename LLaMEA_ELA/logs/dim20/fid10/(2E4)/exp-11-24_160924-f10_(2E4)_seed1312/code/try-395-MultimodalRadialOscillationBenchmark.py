import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic sine components with refined ranges
        self.sin_freq = np.random.uniform(4.0, 12.0, dim)
        self.sin_amp = np.random.uniform(2.0, 4.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for radial basis functions with enhanced diversity
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, dim)
        self.rbf_weights = np.random.uniform(-1.5, 1.5, dim)
        # Initialize polynomial interaction coefficients with higher-order terms
        self.poly_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Additional chaotic parameters for enhanced complexity and fractal characteristics
        self.chaos_factor = np.random.uniform(0.2, 1.2, dim)
        self.oscillation_amplitude = np.random.uniform(0.5, 2.5, dim)
        self.oscillation_frequency = np.random.uniform(1.5, 7.0, dim)
        # Fractal-like self-similarity parameters
        self.fractal_scale = np.random.uniform(0.1, 0.8, dim)
        self.fractal_exponent = np.random.uniform(0.3, 0.7, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sinusoidal components with enhanced irregularity
        for i in range(self.dim):
            # Base chaotic sine term
            result += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            # Additional chaotic oscillation component
            result += self.oscillation_amplitude[i] * np.cos(self.oscillation_frequency[i] * x[i])
            # Chaos injection for irregularity
            result += self.chaos_factor[i] * np.sin(x[i]**3)
            # Fractal-like self-similarity component
            result += self.fractal_scale[i] * np.sin(1.0 / (1.0 + np.exp(-x[i])) - 0.5) ** self.fractal_exponent[i]
            
        # Modified radial basis functions with enhanced non-linearity
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_sum
            
        # Enhanced polynomial interactions with cross-dimensional terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.poly_coeffs[i][j] * x[i] * x[j]
                result += interaction
                
        # Higher-order polynomial terms with increased complexity and better conditioning
        for i in range(self.dim):
            result += 0.15 * x[i]**5 - 0.6 * x[i]**4 + 0.4 * x[i]**3 - 0.15 * x[i]**2 + 0.08 * x[i]
            
        # Cross-dimensional interaction terms with cubic behavior and improved scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.06 * x[i]**3 * x[j] + 0.05 * x[i] * x[j]**3
                
        # Add chaotic global scaling factor with enhanced non-linearity
        result *= (1.0 + 0.15 * np.sum(np.sin(x**2)))
        
        # Add fractal-like complexity term for improved multimodality
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(x[i] * np.pi / 2.0) ** 3
        result += 0.1 * fractal_term
        
        return result