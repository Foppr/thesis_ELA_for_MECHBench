import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_norm**2)
        
        # Polynomial chaos with mixed exponents and sign changes
        poly_chaos = np.sum((x_norm**3 - 0.5 * x_norm**5 + 0.2 * x_norm**7) * np.random.choice([-1, 1], size=self.dim))
        
        # Sine waves with dynamic frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1) * 2 * np.pi
        sine_wave = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm) * (1 + 0.1 * x_norm**2))
        
        # Hyperbolic tangent interaction terms
        tanh_interaction = np.sum(np.tanh(x_norm[:-1] * x_norm[1:]) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Multi-scale radial basis functions with dynamic centers
        rbf_sum = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf_sum += np.exp(-10 * (x_norm - centers[i])**2)
        
        # Chaotic component using a modified logistic map
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.sin(100 * x_norm[i] * x_norm[i+1] * np.sin(x_norm[i]))
        
        # Dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * quadratic + 
                0.2 * poly_chaos + 
                0.15 * sine_wave + 
                0.1 * tanh_interaction + 
                0.1 * rbf_sum + 
                0.1 * chaotic * scale_factor + 
                noise)