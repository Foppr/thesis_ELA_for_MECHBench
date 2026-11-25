import numpy as np

class SaddlePointFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced fractal parameters with quantum scaling
        self.fractal_exp = np.random.rand(dim) * 0.8 + 0.3
        self.saddle_params = np.random.rand(dim) * 3.0 + 1.5
        self.coupling_strength = np.random.rand(dim, dim) * 0.5 + 0.2
        # Quantum-inspired phase terms
        self.quantum_phases = np.random.rand(dim) * 2.0 * np.pi
        # Hyperdimensional interference patterns
        self.interference_patterns = np.random.randn(dim, dim) * 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal-like curvature with quantum phase modulation
            fractal_curvature = 0.0
            for j in range(self.dim):
                if j != i:
                    fractal_curvature += (np.abs(xi)**(1.0 + self.fractal_exp[i] * np.sin(j))) * \
                                       np.cos(xi * (j + 1) * 2.0 + self.quantum_phases[i])
            
            # Saddle point dominance with quantum tunneling effects
            saddle_force = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = xi - x_norm[j]
                    tunneling_effect = np.exp(-0.5 * distance**2) * np.tanh(distance)
                    saddle_force += self.saddle_params[j] * tunneling_effect
            
            # Dynamic coupling with hyperdimensional interference
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    interference = np.sum(self.interference_patterns[i, :] * np.sin(x_norm))
                    coupling += self.coupling_strength[i, j] * np.sin(xi + x_norm[j]) * \
                               np.cos(xi - x_norm[j]) * (1.0 + 0.2 * interference)
            
            # Multi-scale oscillatory behavior with chaotic resonance
            oscillatory = 0.0
            for k in range(1, min(25, self.dim + 10)):
                chaos_factor = np.sin(k * xi + k * np.cos(i * 0.3)) * \
                              np.cos(k * xi * np.sin(i * 0.7))
                oscillatory += (1.0 / k**1.8) * chaos_factor
            
            # Adaptive weighting with quantum correction
            weight = 1.0 + 0.3 * np.sin(i * 0.9 + self.quantum_phases[i]) * \
                    np.cos(self.dim * 0.4 + self.quantum_phases[0])
            
            # Enhanced saddle point dominance with fractal structure
            term = (weight * (fractal_curvature + saddle_force + coupling + oscillatory)**2 + 
                   0.15 * np.abs(xi)**3.5 + 0.08 * xi**5)
            
            result += term
            
        # Global scaling with quantum dimensional correction and chaotic factor
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 4.0) + \
                      0.2 * np.cos(np.log(self.dim + 1) * 3.5) + \
                      0.1 * np.sin(np.log(self.dim + 1) * 2.0)
        
        return global_scale * result / self.dim