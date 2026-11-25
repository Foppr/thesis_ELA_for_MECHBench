import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic sine components with modified frequencies
        self.sin_freq = np.random.uniform(3.0, 20.0, dim)
        self.sin_amp = np.random.uniform(1.8, 5.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, dim)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Additional chaotic parameters for enhanced complexity
        self.chaos_factor = np.random.uniform(0.5, 1.5, dim)
        self.oscillation_amplitude = np.random.uniform(1.0, 3.0, dim)
        self.oscillation_frequency = np.random.uniform(2.0, 8.0, dim)
        # Quaternion-inspired harmonic components
        self.quat_freq = np.random.uniform(1.5, 4.0, dim)
        self.quat_amp = np.random.uniform(0.8, 2.2, dim)
        # Dynamic coupling parameters
        self.coupling_strength = np.random.uniform(0.3, 1.2, (dim, dim))
        self.adaptive_freq = np.random.uniform(0.8, 2.0, dim)
        
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
            # Quaternion-inspired harmonic components
            result += self.quat_amp[i] * np.sin(self.quat_freq[i] * x[i]**2) * np.cos(self.quat_freq[i] * x[i])
            
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
                
        # Higher-order polynomial terms with increased complexity
        for i in range(self.dim):
            result += 0.3 * x[i]**5 - 0.8 * x[i]**4 + 0.7 * x[i]**3 - 0.2 * x[i]**2 + 0.2 * x[i]
            
        # Cross-dimensional interaction terms with cubic behavior (enhanced)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * x[i]**3 * x[j] + 0.15 * x[i] * x[j]**3  # Increased coefficients
                
        # Dynamic coupling terms between dimensions
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.coupling_strength[i][j] * np.sin(x[i] * x[j]) * np.cos(self.adaptive_freq[i] * x[i])
                    
        # Add quaternion-inspired global scaling factor
        result *= (1.0 + 0.3 * np.sum(np.sin(x**2) * np.cos(x**3)))
        
        # Add Gaussian noise to increase robustness testing
        result += np.random.normal(0, 0.15)
        
        return result