import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and saddle point parameters with improved conditioning
        self.fractal_exp = np.random.rand(dim) * 0.8 + 0.3
        self.saddle_params = np.random.rand(dim) * 1.5 + 0.5
        self.coupling_strength = np.random.rand(dim, dim) * 0.4 + 0.2
        # Add additional chaotic elements for better problem difficulty
        self.chaos_params = np.random.rand(dim) * 0.1 + 0.05
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal-like curvature with chaotic modulation
            fractal_curvature = 0.0
            for j in range(min(10, self.dim)):
                phase = (i * 0.7 + j * 0.3) * np.pi
                fractal_curvature += (np.abs(xi)**(1.0 + self.fractal_exp[i] * np.sin(phase))) * np.cos(xi * (j + 1) * 1.5)
            
            # Improved saddle point dominance with multi-scale forces
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = xi - x_norm[j]
                    saddle_force += self.saddle_params[j] * np.tanh(diff) * np.exp(-0.3 * diff**2)
            
            # Refined dynamic coupling with directional sensitivity
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_strength[i, j] * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
            
            # Enhanced oscillatory behavior with chaotic resonance
            oscillatory = 0.0
            for k in range(1, min(20, self.dim + 10)):
                freq = k * (1.0 + self.chaos_params[i] * np.sin(i * 0.4))
                oscillatory += (1.0 / k**1.3) * np.sin(freq * xi + k * np.cos(i * 0.6))
            
            # Adaptive weighting with improved conditioning
            weight = 1.0 + 0.3 * np.sin(i * 0.9) * np.cos(self.dim * 0.25)
            
            # Enhanced term combining all components with better balance
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory)**2 + 
                   0.15 * np.abs(xi)**3 + 0.08 * xi**4 + 
                   0.05 * np.sin(5 * xi) * np.cos(3 * xi))
            
            result += term
            
        # Improved global scaling with better fractal dimension correction
        global_scale = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 2.8) + \
                      0.15 * np.cos(np.log(self.dim + 1) * 2.2)
        
        return global_scale * result / self.dim