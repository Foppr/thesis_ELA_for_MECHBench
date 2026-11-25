import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component
        exp_decay = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(2 * np.pi * x))
        
        # Trigonometric oscillation component with varying frequencies
        trig_osc = 0
        for i in range(self.dim):
            freq = 1 + i * 0.5
            trig_osc += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        # Polynomial penalty term to encourage convergence to global minimum
        poly_penalty = np.sum((x**3 - 3 * x**2 + 2 * x)**2)
        
        # Combined function with scaling factors
        return 0.1 * exp_decay + 0.5 * trig_osc + 0.01 * poly_penalty + 10 * self.dim