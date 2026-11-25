import numpy as np

class SaddleFractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum-like parameters for interference patterns
        self.quantum_params = np.random.rand(dim) * 2.0 + 1.0
        self.fractal_exp = np.random.rand(dim) * 0.6 + 0.2
        self.saddle_strength = np.random.rand(dim) * 0.8 + 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Quantum-like interference terms with phase modulation
            quantum_interference = np.sin(xi * self.quantum_params[i]) * np.cos(xi * self.quantum_params[i] * 1.3) + \
                                 0.4 * np.sin(xi * self.quantum_params[i] * 2.7) * np.cos(xi * self.quantum_params[i] * 0.8)
            
            # Fractal-induced gradient modulation with saddle-point characteristics
            fractal_mod = 1.0 + 0.5 * np.sin(xi * 10.0)**2 * np.cos(xi * 5.0)**2
            
            # Saddle-point dominant curvature with variable dominance
            saddle_curvature = (1.0 + self.saddle_strength[i] * np.sin(xi * 7.0)**2) * \
                              (1.0 + 0.3 * np.cos(xi * 12.0)**2)
            
            # Multi-modal potential with asymmetric basins
            multimodal = (0.5 * np.sin(xi * 2.0)**4 + 0.3 * np.cos(xi * 6.0)**3 + 
                         0.2 * np.sin(xi * 10.0)**2 + 0.1 * np.cos(xi * 15.0)**4)
            
            # Cross-dimensional coupling with fractal interference
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling += (1.0 / (1.0 + np.abs(xi - x_norm[j])**1.5)) * \
                               np.sin(xi * x_norm[j] * 0.5 + 0.2 * np.sin(i + j) + 0.1 * np.cos(i * j))
            
            # Combine all terms with adaptive weighting
            weight = 1.0 + 0.4 * np.sin(i * 0.5) * np.cos(self.dim * 0.2)
            result += weight * (saddle_curvature * fractal_mod * (multimodal + quantum_interference) + 
                               0.3 * coupling)**2
            
        # Global scaling with quantum correction factors
        global_scale = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 3.7) + \
                      0.1 * np.cos(np.log(self.dim + 1) * 2.8)
        
        return global_scale * result / self.dim