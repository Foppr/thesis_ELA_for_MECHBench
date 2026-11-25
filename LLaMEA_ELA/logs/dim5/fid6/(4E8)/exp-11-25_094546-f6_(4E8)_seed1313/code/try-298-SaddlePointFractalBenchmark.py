import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and saddle point parameters with enhanced complexity
        self.fractal_exp = np.random.rand(dim) * 1.2 + 0.5
        self.saddle_params = np.random.rand(dim) * 2.0 + 0.8
        self.coupling_strength = np.random.rand(dim, dim) * 0.6 + 0.3
        # Add chaotic resonance coupling for increased complexity
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.sin((i - j) * 0.8 + np.pi/4) * 0.5 + 0.7
        # Add hyperdimensional phase shifts and interference patterns
        self.phase_shifts = np.random.rand(dim) * np.pi * 2
        self.interference_params = np.random.rand(dim) * 0.8 + 0.2
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal-like curvature with chaotic resonance terms
            fractal_curvature = 0.0
            for j in range(min(15, self.dim)):
                if j < self.dim:
                    exponent = 1.0 + self.fractal_exp[j] * np.sin(xi * (j + 1) * 0.8 + self.phase_shifts[j])
                    fractal_curvature += (np.abs(xi)**exponent) * np.cos(xi * (j + 1) * 2.0)
            
            # Saddle point dominance with chaotic resonance and interference
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = xi - x_norm[j]
                    # Add chaotic resonance component
                    resonance = np.sin(diff * 3.0 + self.interference_params[i]) * 0.2
                    saddle_force += (self.saddle_params[j] * np.tanh(diff) * np.exp(-0.3 * diff**2) + resonance)
            
            # Enhanced dynamic coupling with hyperdimensional interference
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    # Add hyperdimensional interference term
                    coupling += 0.1 * np.sin((xi + x_norm[j]) * (i + j + 1)) * self.interference_params[j]
            
            # Multi-scale oscillatory behavior with chaotic frequency modulation
            oscillatory = 0.0
            for k in range(1, min(25, self.dim + 15)):
                freq = k * (1.0 + 0.2 * np.sin(i * 0.4 + self.interference_params[i]))
                # Add chaotic modulation to frequency
                freq_mod = 1.0 + 0.1 * np.sin(k * 0.3 + self.phase_shifts[i])
                oscillatory += (1.0 / k**1.5) * np.sin(freq * xi * freq_mod + k * np.cos(i * 0.5))
            
            # Add hyperdimensional fractal interference pattern
            interference = 0.0
            for k in range(1, min(10, self.dim)):
                interference += (self.interference_params[i] * np.sin(xi * (k + 1) * 0.5) * 
                               np.cos(xi * (k + 1) * 0.3) * np.exp(-0.1 * k))
            
            # Combine terms with adaptive weighting based on dimension and interference
            weight = 1.0 + 0.4 * np.sin(i * 0.7) * np.cos(self.dim * 0.3) + self.interference_params[i] * 0.2
            
            # Create enhanced saddle point dominance with fractal-like structure and chaos
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory + interference)**2 + 
                   0.2 * np.abs(xi)**3 + 0.1 * xi**4 + 0.05 * np.sin(xi * 10))
            
            result += term
            
        # Global scaling with enhanced fractal dimension correction and chaotic modulation
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 3.0) + \
                      0.2 * np.cos(np.log(self.dim + 1) * 2.0) + \
                      0.15 * np.sin(self.dim * 0.5)
        
        return global_scale * result / self.dim