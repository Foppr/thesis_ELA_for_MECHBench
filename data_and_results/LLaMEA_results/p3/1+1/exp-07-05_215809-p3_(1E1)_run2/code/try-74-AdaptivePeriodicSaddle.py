import numpy as np

class AdaptivePeriodicSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base periodic sinusoidal components with varying frequencies and amplitudes
        f = 0.0
        for i in range(self.dim):
            f += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.sin(5 * x_norm[i])
            
        # Asymmetric saddle points with dimension-dependent weights
        for i in range(self.dim):
            # Quadratic and cubic terms with directional bias
            bias = 0.3 * np.sin(i * 0.5) + 0.2 * np.cos(i * 0.7)
            f += (x[i]**2 + bias * x[i] + 0.1 * x[i]**3) * np.tanh(x[i])
            
        # Multi-scale periodicity with adaptive frequency modulation
        for i in range(self.dim):
            for j in range(1, min(4, self.dim - i + 1)):
                freq_mod = 1.0 + 0.2 * np.sin(i * 0.3 + j * 0.5)
                f += 0.2 * np.sin(freq_mod * x[i] + j * np.pi/4) * np.cos(freq_mod * x[i] + j * np.pi/3)
                
        # Adaptive noise component that increases with dimensionality
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(11 * x_norm[i]) * np.cos(13 * x_norm[i]) * np.sin(17 * x_norm[i])
        f += noise * (1.0 + 0.1 * self.dim)
        
        # Saddle point enhancement with exponential decay and directional sensitivity
        for i in range(self.dim):
            f += 0.15 * np.exp(-0.5 * x[i]**2) * np.sin(7 * x[i]) * np.cos(9 * x[i])
            
        # Asymmetric hill-climbing with increasing difficulty towards center
        for i in range(self.dim):
            center_diff = np.abs(x[i] - np.sin(i * 0.4))
            f += 0.2 * center_diff**2 * np.exp(-center_diff)
            
        # Dimensional coupling with non-linear interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * np.sin(x[i] * x[j])
                f += 0.1 * interaction * (1.0 + 0.05 * (i + j))
                
        # Fractal-like structure with recursive periodic components
        for i in range(self.dim):
            f += 0.05 * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i]) * np.sin(29 * x_norm[i]) * np.cos(31 * x_norm[i])
            
        # Adaptive scaling based on proximity to critical points
        critical_points = np.array([np.sin(i * 0.3) for i in range(self.dim)])
        dist = np.sum((x - critical_points)**2)
        scale = 1.0 + 0.3 * np.exp(-dist / 2.0)
        f *= scale
        
        # Additional multi-modal structure with irregular peaks
        for i in range(self.dim):
            f += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i]) + 0.05 * np.sin(35 * x[i])
            
        return f