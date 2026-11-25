import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Chaotic oscillator with phase coupling
            oscillator = np.sin(xi * 10.0) + 0.5 * np.sin(3.0 * xi) + 0.3 * np.sin(7.0 * xi)
            
            # Adaptive energy barrier with dimension-dependent scaling
            barrier_height = 1.0 + 0.8 * np.sin(self.dim * 0.3 + i * 0.4) * np.cos(i * 0.2)
            
            # Dynamic coupling strength based on neighbor positions
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Dynamic coupling with phase modulation
                    coupling_strength = 1.0 / (1.0 + distance**2) * np.cos(i * 0.5 + j * 0.3)
                    coupling += coupling_strength * np.sin(xi + x_norm[j] + 0.7 * np.sin(i + j))
            
            # Multi-scale modulation with chaotic frequency
            modulation = 1.0
            for k in range(1, 5):
                freq = 2 ** k + 0.1 * np.sin(i * 0.3 + k * 0.2)
                modulation *= (1.0 + 0.4 * np.sin(freq * xi + k * 0.1))
            
            # Add to result with dynamic weighting
            weight = 1.0 + 0.6 * np.sin(i * 0.3) * np.cos(self.dim * 0.2 + i * 0.1)
            
            # Apply chaotic amplification factor
            chaos_amp = 1.0 + 0.5 * np.sin(np.sum(x_norm**3) + i * 0.4)
            
            result += weight * chaos_amp * (barrier_height * oscillator**2 + 0.3 * coupling)**2
            
        # Global chaotic scaling with dynamic dimensionality correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 5.0)
        
        # Add chaotic hyper-modulation based on all dimensions
        hyper_modulation = 1.0 + 0.4 * np.sin(np.sum(np.abs(x_norm)**3) * 2.0 + self.dim * 0.2)
        
        return global_scale * hyper_modulation * result / self.dim