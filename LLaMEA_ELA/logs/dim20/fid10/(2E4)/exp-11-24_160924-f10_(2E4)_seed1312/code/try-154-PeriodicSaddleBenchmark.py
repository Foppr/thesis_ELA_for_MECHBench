import numpy as np

class PeriodicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic modulation frequencies and amplitudes
        self.frequencies = [1.0 + 0.5 * np.sin(0.5 * i) for i in range(dim)]
        self.amplitudes = [0.5 + 0.5 * np.cos(0.3 * i) for i in range(dim)]
        # Saddle point locations and weights
        self.saddle_centers = [np.random.uniform(-4.0, 4.0) for _ in range(dim)]
        self.saddle_weights = [1.0 + 0.5 * np.sin(0.7 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            result += amp * np.sin(freq * xi) * np.cos(freq * xi)
            
        # Add saddle-point structures with configurable weights
        for i in range(self.dim):
            xi = x[i]
            center = self.saddle_centers[i]
            weight = self.saddle_weights[i]
            result += weight * (xi - center)**2 * np.sin(0.5 * (xi - center))
            
        # Add rotational coupling with periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = 0.2 * np.sin(0.3 * (i + j))
                rot_xi = x[i] * np.cos(angle) - x[j] * np.sin(angle)
                rot_xj = x[i] * np.sin(angle) + x[j] * np.cos(angle)
                result += 0.1 * np.sin(rot_xi + rot_xj) * np.cos(rot_xi - rot_xj)
                
        # Add multi-scale interference patterns
        for i in range(self.dim):
            xi = x[i]
            # Add multiple harmonic components at different scales
            for k in range(1, 4):
                result += 0.2 * np.sin(k * xi) * np.cos(k * xi)
                
        # Add tunable ruggedness through chaotic amplitude variations
        for i in range(self.dim):
            xi = x[i]
            chaos_amp = 0.3 + 0.4 * np.sin(10.0 * xi + 0.5 * i)
            result += chaos_amp * np.sin(7.0 * xi) * np.cos(5.0 * xi)
            
        # Add global scaling with dimension-dependent factor
        global_scale = 1.0 + 0.2 * np.sin(0.1 * self.dim)
        result *= global_scale
        
        return result