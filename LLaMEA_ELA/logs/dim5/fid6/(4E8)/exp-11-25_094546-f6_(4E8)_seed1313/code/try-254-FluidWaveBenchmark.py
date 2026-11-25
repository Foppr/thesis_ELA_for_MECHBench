import numpy as np

class FluidWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        # Base harmonic component with multi-scale frequency modulation
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Multi-scale harmonic terms with varying frequencies
            harmonic_sum = 0.0
            for k in range(1, 6):
                freq = k * (1.0 + 0.3 * np.sin(i * 0.7 + k))
                amp = 1.0 / (k * (1.0 + 0.2 * np.cos(i * 0.5 + k)))
                harmonic_sum += amp * np.sin(freq * xi)
            
            # Saddle-point corridor modulation
            corridor_mod = 1.0 + 0.4 * np.cos(3.0 * xi + i * 0.3) * np.sin(2.0 * xi - i * 0.4)
            
            # Gradient-flow chaos term with neighbor coupling
            flow_chaos = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling = 0.2 * np.exp(-abs(i - j) * 0.3)
                    flow_chaos += coupling * np.tan(xi + x_norm[j] * 0.5 + 0.1 * np.sin(i + j))
            
            # Multi-scale interference pattern
            interference = 0.0
            for k in range(1, 4):
                phase = k * (i * 0.2 + np.cos(xi * k))
                interference += np.cos(k * xi + phase) * np.exp(-0.5 * (xi - np.sin(k * xi))**2)
            
            # Combine components with dynamic weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.6 + self.dim * 0.2)
            amplitude = 1.0 + 0.25 * np.cos(xi * 3.0 + i * 0.8)
            
            result += weight * amplitude * (harmonic_sum**2 + corridor_mod * interference + 
                                          flow_chaos**2)
        
        # Global scaling with fluid dynamics parameter
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 1.8)
        
        # Add wave propagation modulation
        wave_mod = 1.0 + 0.3 * np.cos(np.sum(x_norm**2) * 2.0 + self.dim * 0.5)
        
        # Final normalization and smoothing
        return global_scale * wave_mod * result / self.dim