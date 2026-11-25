import numpy as np

class PeriodicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic modulation frequencies and amplitudes
        self.frequencies = [2.0 + 0.5 * np.sin(0.7 * i + 1.2) for i in range(dim)]
        self.amplitudes = [1.0 + 0.4 * np.cos(0.5 * i + 0.8) for i in range(dim)]
        # Saddle point locations with increased randomness and dimensionality coupling
        self.saddle_centers = [np.random.uniform(-4.0, 4.0) for _ in range(dim)]
        self.saddle_weights = [1.5 + 0.5 * np.sin(0.9 * i + 0.3) for i in range(dim)]
        # Additional chaotic interference terms
        self.interference_freqs = [1.8 + 0.6 * np.cos(0.6 * i + 0.4) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add enhanced periodic sinusoidal components with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            result += amp * np.sin(freq * xi) * np.cos(freq * xi)
            
        # Add saddle-point structures with enhanced nonlinearity and coupling
        for i in range(self.dim):
            xi = x[i]
            center = self.saddle_centers[i]
            weight = self.saddle_weights[i]
            result += weight * (xi - center)**3 * np.sin(0.7 * (xi - center))
            
        # Add rotational coupling with chaotic angle variations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = 0.4 * np.sin(0.5 * (i + j) + 0.6 * np.cos(0.3 * i))
                rot_xi = x[i] * np.cos(angle) - x[j] * np.sin(angle)
                rot_xj = x[i] * np.sin(angle) + x[j] * np.cos(angle)
                result += 0.2 * np.sin(rot_xi + rot_xj) * np.cos(rot_xi - rot_xj)
                
        # Add multi-scale chaotic interference patterns
        for i in range(self.dim):
            xi = x[i]
            for k in range(1, 7):
                freq = self.interference_freqs[i] * (1.0 + 0.2 * np.sin(k * xi))
                result += 0.3 * np.sin(freq * xi) * np.cos(freq * xi)
                
        # Add enhanced chaotic amplitude variations with stochastic perturbations
        for i in range(self.dim):
            xi = x[i]
            chaos_amp = 0.5 + 0.4 * np.sin(15.0 * xi + 0.7 * i + 2.0 * np.cos(3.0 * xi))
            result += chaos_amp * np.sin(9.0 * xi) * np.cos(7.0 * xi)
            
        # Add adaptive ridge structures with exponential decay
        for i in range(self.dim):
            xi = x[i]
            ridge_height = 0.8 + 0.3 * np.sin(2.0 * xi)
            result += ridge_height * np.exp(-0.5 * (xi - 1.0)**2) * np.sin(3.0 * xi)
            
        # Add global scaling with enhanced dimensionality dependence
        global_scale = 1.2 + 0.2 * np.sin(0.15 * self.dim + 0.5)
        result *= global_scale
        
        # Add improved fitness landscape characteristics to reduce bias
        # Introduce more varied and complex local minima patterns
        for i in range(self.dim):
            xi = x[i]
            # Add additional periodic modulation with varying frequencies
            result += 0.1 * np.sin(5.0 * xi + 2.0 * np.cos(2.0 * xi)) * np.cos(3.0 * xi)
            
        # Add cross-dimensional interaction terms to improve conditioning
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling to avoid over-complication
                result += 0.05 * (x[i]**2 + x[j]**2) * np.sin(0.3 * (x[i] - x[j]))
                
        return result