import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with chaotic scaling
        base = 0.1 * np.sum(x**2) + 0.01 * np.random.rand()
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            sin_term += 0.5 * np.sin(5 * x[i]) * np.sin(4 * x[(i + 2) % self.dim])
            sin_term += 0.3 * np.cos(7 * x[i]) * np.cos(6 * x[(i + 3) % self.dim])
        
        # Exponentially decaying cross-dimensional interactions
        exp_interaction = 0.0
        for i in range(self.dim):
            exp_interaction += np.exp(-0.5 * (x[i] - x[(i + 1) % self.dim])**2)
            exp_interaction += 0.2 * np.exp(-0.3 * (x[i] - x[(i + 2) % self.dim])**2)
        
        # Fractal-like structure with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(10 * x[i]) * np.cos(8 * x[(i + 1) % self.dim])
            fractal += 0.1 * np.sin(15 * x[i]) * np.sin(12 * x[(i + 2) % self.dim])
        
        # Chaotic noise component with non-linear transformations
        chaotic_noise = 0.0
        for i in range(self.dim):
            chaotic_noise += np.sin(20 * x[i]) * np.cos(18 * x[(i + 1) % self.dim])
            chaotic_noise += 0.05 * np.tanh(x[i])**2
        
        # Combine all components with adaptive weights
        return 1.0 * base + 1.3 * sin_term + 0.8 * exp_interaction + 1.1 * fractal + 0.7 * chaotic_noise