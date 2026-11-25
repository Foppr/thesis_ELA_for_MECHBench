import numpy as np

class FractalChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute delay indices for chaotic oscillations
        self.delay_indices = np.arange(1, min(6, dim + 1))
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal basin components with varying scales
        fractal_sum = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.2 * i)
            base = 0.5 + 0.3 * np.cos(0.3 * i)
            fractal_sum += scale * np.exp(-0.5 * ((x[i] - base) / (0.5 + 0.1 * i))**4)
            
        # Time-delayed chaotic oscillations
        chaotic_osc = 0.0
        for i in range(self.dim):
            delayed_term = 0.0
            for d in self.delay_indices:
                if i >= d:
                    delayed_term += np.sin(x[i - d] + 0.1 * x[i])
            chaotic_osc += np.sin(2.0 * x[i] + 0.5 * delayed_term) * np.cos(1.5 * x[i])
            
        # Multi-scale Gaussian mixture with adaptive weights
        gaussian_sum = 0.0
        centers = np.linspace(-4, 4, 9)
        for i in range(self.dim):
            for j, center in enumerate(centers):
                weight = 0.1 + 0.2 * np.sin(0.3 * (i + j))
                sigma = 0.5 + 0.3 * np.cos(0.2 * j)
                gaussian_sum += weight * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
                
        # Memory-dependent conditioning with dynamic exponents
        memory_cond = 0.0
        for i in range(self.dim):
            exponent = 2.0 + 0.5 * np.sin(0.4 * x[i])
            coeff = 1.0 + 0.3 * np.cos(0.3 * i)
            memory_cond += coeff * (x[i]**exponent)
            
        # Cross-dimensional coupling with fractal-like interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                fractal_factor = 1.0 + 0.2 * np.sin(0.1 * (i + j))
                cross_coupling += fractal_factor * interaction
                
        # Transient dynamics with damping factor
        transient = 0.0
        for i in range(self.dim):
            damping = 0.8 + 0.1 * np.sin(0.2 * x[i])
            transient += damping * np.sin(3.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        return fractal_sum + chaotic_osc + gaussian_sum + memory_cond + cross_coupling + transient