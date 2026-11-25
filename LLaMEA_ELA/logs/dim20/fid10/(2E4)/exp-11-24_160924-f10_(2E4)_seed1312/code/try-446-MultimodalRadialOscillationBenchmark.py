import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Enhanced chaotic sine wave parameters with hyperbolic scaling
        self.sin_r = np.random.uniform(2.0, 10.0, dim)
        self.sin_phase = np.random.uniform(0, 2*np.pi, dim)
        # Modified radial basis functions with time-varying centers and weights
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, dim))
        self.rbf_widths = np.random.uniform(0.2, 3.0, dim)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, dim)
        # Cross-dimensional polynomial interactions with higher-order terms
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim, dim))
        # Memory-dependent evolutionary parameters with hyperbolic tangent modulation
        self.memory_strength = np.random.uniform(0.1, 2.5, dim)
        self.evolutionary_decay = np.random.uniform(0.5, 0.999, dim)
        # Dynamic coupling with adaptive weights and chaotic modulation
        self.coupling_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Quaternion-inspired harmonic components with hyperbolic functions
        self.harmonic_freq = np.random.uniform(0.5, 12.0, dim)
        self.harmonic_amp = np.random.uniform(0.1, 3.0, dim)
        # Fractal-like scaling factors with adaptive exponents
        self.fractal_scale = np.random.uniform(0.05, 1.5, dim)
        self.fractal_exp = np.random.uniform(1.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sine wave components with hyperbolic scaling
        for i in range(self.dim):
            sin_value = self.sin_r[i] * np.sinh(x[i] + self.sin_phase[i])
            result += sin_value
            
        # Radial basis functions with dynamic centers and time-varying weights
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                distance = (x[j] - self.rbf_centers[i][j])**2
                rbf_sum += np.exp(-distance / (2 * self.rbf_widths[i]**2))
            result += self.rbf_weights[i] * rbf_sum
            
        # Cross-dimensional polynomial interactions with third-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    interaction = self.poly_coeffs[i][j][k] * x[i]**2 * x[j] * x[k]
                    result += interaction
                    
        # Add cubic polynomial terms with hyperbolic tangent modulation
        for i in range(self.dim):
            result += 0.3 * np.tanh(x[i]**3)
            
        # Memory-dependent evolutionary terms with hyperbolic decay
        for i in range(self.dim):
            memory_term = self.memory_strength[i] * np.tanh(x[i] * self.harmonic_freq[i])
            result += memory_term * self.evolutionary_decay[i]**(self.dim - i)
            
        # Dynamic coupling between dimensions with chaotic modulation
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_matrix[i][j] * np.tanh(x[i] * x[j])
            result += coupling_sum
            
        # Quaternion-inspired harmonic components with hyperbolic modulation
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += self.harmonic_amp[i] * np.sinh(x[i]**2) * np.cosh(x[i]**3)
        result += harmonic_term
        
        # Fractal-like scaling with chaotic modulation and adaptive exponents
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += self.fractal_scale[i] * np.sinh(x[i]**self.fractal_exp[i]) * np.cosh(x[i]**2)
        result += fractal_term
        
        # Add hyperbolic tangent modulation to the entire function
        chaos_modulation = 0.0
        for i in range(self.dim):
            chaos_modulation += self.harmonic_amp[i] * np.tanh(self.harmonic_freq[i] * x[i]**3)
        result *= (1.0 + 0.3 * chaos_modulation)
        
        # Add small random noise for robustness
        result += np.random.normal(0, 0.15)
        
        return result