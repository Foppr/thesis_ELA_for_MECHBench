import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent gradient component creating deceptive valleys
        tanh_grad = 0.0
        for i in range(self.dim):
            tanh_grad += np.tanh(2.0 * x[i]) * np.sin(0.5 * x[i])
        
        # Sinusoidal corridor structure with varying frequencies
        sin_corridor = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.2 * x[i])
            sin_corridor += np.sin(freq * x[i]) * np.cos(0.3 * x[i])
        
        # Adaptive Gaussian valleys with dynamic centers and widths
        gaussian_valleys = 0.0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.5 * x[i]) + 1.5 * np.cos(0.2 * x[i])
            width = 0.5 + 0.5 * np.abs(np.sin(0.1 * x[i]))
            height = 1.0 + 0.5 * np.cos(0.4 * x[i])
            gaussian_valleys += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Chaotic oscillation component using logistic map
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            chaotic += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x[i])
        
        # Dynamic penalty for boundary avoidance
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 2.0)
            boundary_penalty += 1.0 / (dist_from_boundary + 1e-8) * np.sin(x[i])**2
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = 0.5 + 0.5 * np.sin(0.3 * x[i])
            coupling += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Combined fitness function with dynamic scaling
        return 0.3 * tanh_grad + 0.25 * sin_corridor + 0.2 * gaussian_valleys + 0.15 * chaotic + 0.08 * boundary_penalty + 0.02 * coupling