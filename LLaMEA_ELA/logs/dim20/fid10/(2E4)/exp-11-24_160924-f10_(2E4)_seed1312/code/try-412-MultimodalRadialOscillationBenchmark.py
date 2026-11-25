import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic sine components with modified frequencies
        self.sin_freq = np.random.uniform(5.0, 25.0, dim)
        self.sin_amp = np.random.uniform(2.5, 6.0, dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.rbf_widths = np.random.uniform(0.4, 3.0, dim)
        self.rbf_weights = np.random.uniform(-2.5, 2.5, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Additional chaotic parameters for enhanced complexity
        self.chaos_factor = np.random.uniform(0.6, 2.0, dim)
        self.oscillation_amplitude = np.random.uniform(1.2, 4.0, dim)
        self.oscillation_frequency = np.random.uniform(3.0, 12.0, dim)
        # Hyper-chaotic coupling terms
        self.hyper_chaos_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.frequency_modulation = np.random.uniform(0.8, 1.8, dim)
        self.cubic_interaction_strength = np.random.uniform(0.3, 0.8, dim)
        # Quaternion-inspired harmonic components
        self.quaternion_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Adaptive frequency modulation parameters
        self.adaptive_freq = np.random.uniform(0.5, 2.5, dim)
        # Dynamic coupling coefficients
        self.dynamic_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        
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
            # Frequency modulation term
            result += 0.5 * np.sin(self.frequency_modulation[i] * x[i]**2)
            
        # Quaternion-inspired harmonic components
        for i in range(self.dim):
            quaternion_term = 0.0
            for j in range(4):
                quaternion_term += self.quaternion_coeffs[i][j] * np.sin((j+1) * x[i])
            result += quaternion_term
            
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
                result += 0.25 * x[i]**3 * x[j] + 0.2 * x[i] * x[j]**3  # Increased coefficients
                
        # Hyper-chaotic coupling terms between dimensions
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.hyper_chaos_coeffs[i][j] * np.sin(x[i]) * np.cos(x[j])
                    
        # Dynamic coupling between dimensions
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += self.dynamic_coupling[i][j] * np.tan(x[i]) * np.log(np.abs(x[j]) + 1)
                    
        # Cubic interaction strength modulation
        for i in range(self.dim):
            result += self.cubic_interaction_strength[i] * x[i]**6
            
        # Adaptive frequency modulation component
        for i in range(self.dim):
            result += 0.15 * np.sin(self.adaptive_freq[i] * x[i]**4)
            
        # Add chaotic global scaling factor with dynamic component
        result *= (1.0 + 0.35 * np.sum(np.sin(x**2)) + 0.15 * np.sum(np.cos(x**3)))
        
        # Add Gaussian noise to increase robustness testing
        result += np.random.normal(0, 0.15)
        
        return result