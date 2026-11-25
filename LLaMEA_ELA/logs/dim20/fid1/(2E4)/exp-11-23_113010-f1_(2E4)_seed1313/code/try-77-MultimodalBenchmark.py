import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic phase interaction terms with dynamic modulation
        phase_mod = np.sum(np.sin(2 * np.pi * x_norm * np.exp(-x_norm**2)) * 
                          np.cos(3 * np.pi * x_norm * np.exp(-x_norm**2)))
        
        # Dynamic frequency modulation with exponential scaling
        freq_mod = np.sum(np.sin(np.exp(1.5 * np.abs(x_norm)) * x_norm) * 
                         np.cos(np.exp(2.0 * np.abs(x_norm)) * x_norm))
        
        # Asymmetric ridge structure with polynomial conditioning
        ridge = np.sum((x_norm**3 + 0.5 * x_norm**2 + 0.1 * x_norm)**2)
        
        # Multi-scale harmonic components with varying amplitudes
        harmonics = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                          np.sin(19 * np.pi * x_norm) * np.cos(23 * np.pi * x_norm))
        
        # Cross-dimensional coupling with asymmetric interaction weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + 1) / (j + 1)
                cross_coupling += weight * (x_norm[i]**4 + x_norm[j]**4) * np.sin(5 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Conditionally scaled noise component
        noise = 0.02 * np.random.random() * (1 + np.mean(np.abs(x_norm)))
        
        return 1.5 * phase_mod + 0.8 * freq_mod + 0.6 * ridge + 0.4 * harmonics + 0.7 * cross_coupling + noise