import numpy as np

class ChaoticRadialEvolutionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize chaotic tent map parameters
        self.tent_r = np.random.uniform(3.5, 3.9, dim)
        self.tent_offset = np.random.uniform(-0.5, 0.5, dim)
        # Initialize radial basis functions with dynamic centers
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 2.5, dim)
        self.rbf_weights = np.random.uniform(-3.0, 3.0, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Memory-dependent evolutionary parameters
        self.memory_strength = np.random.uniform(0.2, 1.0, dim)
        self.evolutionary_decay = np.random.uniform(0.8, 0.99, dim)
        # Dynamic coupling between dimensions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Chaotic modulation parameters
        self.modulation_freq = np.random.uniform(1.0, 8.0, dim)
        self.modulation_amp = np.random.uniform(0.5, 2.0, dim)
        # Fractal-like scaling factors
        self.fractal_scale = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic tent map components
        for i in range(self.dim):
            # Tent map with dynamic parameter
            tent_value = self.tent_r[i] * np.abs(x[i] - self.tent_offset[i])
            if x[i] > 0.5:
                tent_value = 1.0 - tent_value
            result += tent_value
            
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
            memory_term = self.memory_strength[i] * np.sin(x[i] * self.modulation_freq[i])
            result += memory_term * self.evolutionary_decay[i]**(self.dim - i)
            
        # Dynamic coupling between dimensions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_matrix[i][j] * np.sin(x[i] * x[j])
            result += coupling_sum
            
        # Fractal-like scaling with chaotic modulation
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_scale[i] * np.sin(x[i]**3) * np.cos(x[i])
        result += fractal_term
        
        # Add chaotic modulation to the entire function
        chaos_modulation = 0.0
        for i in range(self.dim):
            chaos_modulation += self.modulation_amp[i] * np.sin(self.modulation_freq[i] * x[i]**2)
        result *= (1.0 + 0.3 * chaos_modulation)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.1)
        
        return result