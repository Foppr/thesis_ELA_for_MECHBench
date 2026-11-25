import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like discontinuous components with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scaled_x = x[i] / (1.0 + 0.1 * np.abs(x[i]))
            fractal += np.sin(10.0 * scaled_x) * np.cos(7.0 * scaled_x) * \
                       np.exp(-0.5 * (scaled_x - np.sin(scaled_x))**2)
        
        # Dynamic harmonic oscillation with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + x[i] * 0.1)
            amp = 1.0 + 0.3 * np.cos(0.5 * i + x[i] * 0.2)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Multi-scale ridge structure with varying curvature
        ridge = 0.0
        for i in range(self.dim - 1):
            dx = x[i+1] - x[i]
            ridge += 0.5 * (dx**2 + 0.1 * np.abs(dx)) * \
                     (1.0 + 0.2 * np.sin(3.0 * x[i]))
        
        # Chaotic gradient component with adaptive coupling
        chaotic_grad = 0.0
        for i in range(self.dim):
            coupling = np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3)
            chaotic_grad += coupling * (x[i]**3 - 2.0 * x[i]**2 + x[i])
        
        # Logarithmic barrier with multi-scale conditioning
        log_barrier = 0.0
        for i in range(self.dim):
            dist_to_boundary = min(5.0 - np.abs(x[i]), 1e-6)
            log_barrier += np.log(dist_to_boundary) * (1.0 + 0.1 * np.sin(i))
        
        # Combined function with dynamic weighting
        total = 0.3 * fractal + 0.4 * harmonic + 0.2 * ridge + 0.1 * chaotic_grad + log_barrier
        
        return total