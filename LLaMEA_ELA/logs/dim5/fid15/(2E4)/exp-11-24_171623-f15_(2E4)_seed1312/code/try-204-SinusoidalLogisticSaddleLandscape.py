import numpy as np

class SinusoidalLogisticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaotic behavior
        self.logistic_r = 3.9 + 0.1 * np.random.rand(dim)
        # Precompute sinusoidal radial basis centers and frequencies
        self.centers = np.random.uniform(-1, 1, dim)
        self.frequencies = 2.0 + 3.0 * np.random.rand(dim)
        # Precompute saddle-point coupling weights
        self.saddle_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Precompute chaotic sequence for dynamic conditioning
        self.chaotic_seq = np.array([self._logistic_map(0.5, self.logistic_r[i]) for i in range(dim)])
        
    def _logistic_map(self, x, r):
        return r * x * (1 - x)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal radial basis component with dynamic frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            sin_sum += np.sin(self.frequencies[i] * np.sqrt(dist)) * np.exp(-dist / 2.0)
        
        # Chaotic logistic map component with dynamic scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            x_chaos = self.chaotic_seq[i]
            chaotic_sum += (x_chaos**2 - 0.5) * np.cos(3 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Saddle-point coupling component with cross-dimensional interactions
        saddle_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.saddle_weights[i, j] * (x_norm[i] - x_norm[j])**2
                    saddle_sum += coupling * np.exp(-0.5 * coupling**2)
        
        # Multi-modal harmonic component with varying phases
        harm_sum = 0.0
        for i in range(self.dim):
            phase = np.pi * np.sin(i * np.pi / self.dim)
            harm_sum += np.sin(3 * x_norm[i] + phase) * np.cos(2 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Tunneling pathway component with polynomial barriers
        tunnel_sum = 0.0
        for i in range(self.dim):
            barrier = 1.0 + 0.5 * np.sin(x_norm[i] * 4)
            tunnel_sum += barrier * (x_norm[i]**4 - 0.8 * x_norm[i]**2) * np.exp(-0.2 * x_norm[i]**2)
        
        # Combined landscape with adaptive scaling
        result = 0.3 * sin_sum + 0.25 * chaotic_sum + 0.2 * saddle_sum + 0.15 * harm_sum + 0.1 * tunnel_sum
        
        # Dynamic conditioning factor based on chaotic sequence and input magnitude
        condition_factor = 1.0
        for i in range(self.dim):
            chaos_factor = self.chaotic_seq[i] * (1.0 + 0.2 * np.sin(x_norm[i]))
            condition_factor *= (1.0 + 0.4 * np.abs(x_norm[i]) + 0.1 * x_norm[i]**3 + 0.05 * chaos_factor)
        
        # Final transformation with global scaling and noise modulation
        noise = 0.03 * np.sum(np.cos(x_norm * 5))
        return result * condition_factor + noise + 0.08 * np.sum(x_norm**6)
