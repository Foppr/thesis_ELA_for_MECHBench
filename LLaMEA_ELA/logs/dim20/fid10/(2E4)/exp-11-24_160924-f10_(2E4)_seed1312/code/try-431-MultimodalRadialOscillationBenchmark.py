import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic sine wave parameters
        self.sine_freq = np.random.uniform(2.0, 6.0, dim)
        self.sine_amp = np.random.uniform(1.0, 3.0, dim)
        # Initialize radial basis functions with dynamic centers
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Memory-dependent evolutionary parameters
        self.memory_strength = np.random.uniform(0.3, 1.2, dim)
        self.evolutionary_decay = np.random.uniform(0.7, 0.98, dim)
        # Dynamic coupling between dimensions
        self.coupling_matrix = np.random.uniform(-0.4, 0.4, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Quaternion-inspired harmonic components
        self.quat_coeffs = np.random.uniform(0.5, 1.5, (dim, 4))
        # Fractal-like scaling factors
        self.fractal_scale = np.random.uniform(0.2, 0.9, dim)
        # Adaptive frequency modulation
        self.modulation_freq = np.random.uniform(0.8, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sine wave components
        for i in range(self.dim):
            sine_value = self.sine_amp[i] * np.sin(self.sine_freq[i] * x[i])
            result += sine_value
            
        # Radial basis functions with dynamic centers
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_sum
            
        # Cross-dimensional polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = self.poly_coeffs[i][j] * x[i] * x[j]
                result += interaction
                
        # Memory-dependent evolutionary terms with decay
        for i in range(self.dim):
            memory_term = self.memory_strength[i] * np.cos(x[i] * self.modulation_freq[i])
            result += memory_term * self.evolutionary_decay[i]**(self.dim - i)
            
        # Dynamic coupling between dimensions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_matrix[i][j] * np.cos(x[i] * x[j])
            result += coupling_sum
            
        # Quaternion-inspired harmonic components
        for i in range(self.dim):
            quat_sum = 0.0
            for k in range(4):
                quat_sum += self.quat_coeffs[i][k] * np.sin((k+1) * x[i])
            result += quat_sum
            
        # Fractal-like scaling with chaotic modulation
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_scale[i] * np.sin(x[i]**4) * np.cos(x[i]**2)
        result += fractal_term
        
        # Add chaotic modulation to the entire function
        chaos_modulation = 0.0
        for i in range(self.dim):
            chaos_modulation += self.sine_amp[i] * np.cos(self.sine_freq[i] * x[i]**3)
        result *= (1.0 + 0.25 * chaos_modulation)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.08)
        
        return result