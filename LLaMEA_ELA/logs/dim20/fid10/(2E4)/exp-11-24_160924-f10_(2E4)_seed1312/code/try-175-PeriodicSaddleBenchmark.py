import numpy as np

class PeriodicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic modulation frequencies and amplitudes with slight changes
        self.frequencies = [1.5 + 0.3 * np.sin(0.6 * i) for i in range(dim)]
        self.amplitudes = [0.7 + 0.3 * np.cos(0.4 * i) for i in range(dim)]
        # Saddle point locations and weights with perturbations
        self.saddle_centers = [np.random.uniform(-3.5, 3.5) for _ in range(dim)]
        self.saddle_weights = [1.2 + 0.3 * np.sin(0.8 * i) for i in range(dim)]
        
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
            result += weight * (xi - center)**2 * np.sin(0.6 * (xi - center))
            
        # Add rotational coupling with enhanced periodic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = 0.3 * np.sin(0.4 * (i + j) + 0.5)
                rot_xi = x[i] * np.cos(angle) - x[j] * np.sin(angle)
                rot_xj = x[i] * np.sin(angle) + x[j] * np.cos(angle)
                result += 0.15 * np.sin(rot_xi + rot_xj) * np.cos(rot_xi - rot_xj)
                
        # Add multi-scale interference patterns with increased complexity
        for i in range(self.dim):
            xi = x[i]
            # Add multiple harmonic components at different scales
            for k in range(1, 5):
                result += 0.25 * np.sin(k * xi) * np.cos(k * xi)
                
        # Add tunable ruggedness through enhanced chaotic amplitude variations
        for i in range(self.dim):
            xi = x[i]
            chaos_amp = 0.4 + 0.3 * np.sin(12.0 * xi + 0.6 * i)
            result += chaos_amp * np.sin(8.0 * xi) * np.cos(6.0 * xi)
            
        # Add global scaling with dimension-dependent factor
        global_scale = 1.1 + 0.15 * np.sin(0.12 * self.dim)
        result *= global_scale
        
        # Add a new chaotic component to improve fitness score
        chaotic_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_factor = 0.3 + 0.2 * np.sin(15.0 * xi + 0.7 * i)
            chaotic_component += chaotic_factor * np.sin(10.0 * xi) * np.cos(7.0 * xi)
        
        # Combine with existing function to improve landscape characteristics
        result = result + 0.3 * chaotic_component
        
        # Add enhanced nonlinearity and cross-dimensional coupling
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * np.sin(20.0 * xi) * np.cos(15.0 * xi) * (1.0 + 0.2 * np.sin(0.5 * i))
            
        # Add dimensionality-dependent noise to improve robustness
        noise_factor = 0.05 * np.sin(0.3 * self.dim)
        result += noise_factor * np.sum(np.sin(x) * np.cos(x))
        
        return result