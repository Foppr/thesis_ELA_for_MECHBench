import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and saddle point parameters with improved distribution
        self.fractal_exp = np.random.rand(dim) * 0.8 + 0.2
        self.saddle_params = np.random.rand(dim) * 1.5 + 0.5
        self.coupling_strength = np.random.rand(dim, dim) * 0.4 + 0.05
        # Add additional chaotic modulation parameters
        self.modulation_freq = np.random.rand(dim) * 3.0 + 1.0
        self.modulation_amp = np.random.rand(dim) * 0.5 + 0.25
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal-like curvature with chaotic modulation
            fractal_curvature = 0.0
            for j in range(min(10, self.dim)):
                phase = (i + j) * np.pi / 4.0
                fractal_curvature += (np.abs(xi)**(1.0 + self.fractal_exp[i] * np.sin(phase))) * \
                                   np.cos(xi * (j + 1) * 3.0 + phase)
            
            # Improved saddle point dominance with asymmetric forces
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = xi - x_norm[j]
                    force = self.saddle_params[j] * np.tanh(diff) * np.exp(-0.25 * diff**2)
                    # Add asymmetric weighting to create more complex saddle structure
                    asym_weight = 1.0 + 0.3 * np.sin(i * 0.7 + j * 0.5)
                    saddle_force += force * asym_weight
            
            # Refined dynamic coupling with phase-locked interactions
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.coupling_strength[i, j] * np.sin(xi + x_norm[j] + i * 0.3)
                    coupling += coupling_term * np.cos(xi - x_norm[j])
            
            # Enhanced oscillatory behavior with multi-frequency components
            oscillatory = 0.0
            for k in range(1, min(20, self.dim + 10)):
                freq_factor = 1.0 + 0.2 * np.sin(k * 0.5)
                oscillatory += (1.0 / k**1.3) * np.sin(freq_factor * k * xi + k * np.cos(i * 0.4))
            
            # Chaotic modulation term for additional complexity
            chaotic_mod = self.modulation_amp[i] * np.sin(self.modulation_freq[i] * xi + 
                                                          np.cos(xi * 2.0) * 0.5)
            
            # Combine terms with improved weighting scheme
            weight = 1.0 + 0.3 * np.sin(i * 0.9) * np.cos(self.dim * 0.4)
            
            # Create enhanced saddle point dominance with refined structure
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory + chaotic_mod)**2 + 
                   0.15 * np.abs(xi)**3 + 0.08 * xi**4)
            
            result += term
            
        # Improved global scaling with better conditioning
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 2.0) + \
                      0.15 * np.cos(np.log(self.dim + 1) * 3.0)
        
        return global_scale * result / self.dim