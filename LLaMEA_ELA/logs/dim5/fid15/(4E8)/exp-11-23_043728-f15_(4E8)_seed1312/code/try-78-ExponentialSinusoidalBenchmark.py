import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential decay and sinusoidal components
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 1.5
        self.delta = 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Exponential decay component
        exp_decay = np.sum(self.alpha * np.exp(-self.beta * np.abs(x_norm)))
        
        # Sinusoidal modulation component
        sin_mod = np.sum(np.sin(self.gamma * x_norm) * np.cos(self.delta * x_norm))
        
        # Gradient-based attraction fields
        grad_attraction = np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Multi-modal structure with multiple local minima
        modal_structure = 0.0
        for i in range(self.dim):
            modal_structure += (x_norm[i]**2 - 4 * np.cos(0.5 * x_norm[i]))**2
        
        # Combine all components with adaptive weighting
        total_energy = exp_decay + 0.3 * sin_mod + 0.2 * grad_attraction + 0.5 * modal_structure
        
        # Add small noise to create ruggedness
        noise = 0.005 * np.random.rand()
        
        return total_energy + noise