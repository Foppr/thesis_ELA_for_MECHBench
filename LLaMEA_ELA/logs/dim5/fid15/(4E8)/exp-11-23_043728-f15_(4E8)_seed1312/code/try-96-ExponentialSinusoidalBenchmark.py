import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential-sinusoidal structure
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 1.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create exponential-sinusoidal energy landscape
        exp_term = np.exp(self.alpha * np.sum(np.abs(x_norm)**self.beta))
        
        # Add sinusoidal interference patterns with quantum-like behavior
        sin_pattern = np.sum(np.sin(self.gamma * x_norm) * np.cos(self.gamma * x_norm**2))
        
        # Introduce fractal-like self-similarity through recursive scaling
        fractal_term = 0.0
        for i in range(1, min(5, self.dim + 1)):
            if i < self.dim:
                fractal_term += np.sin(2**(i) * x_norm[i-1]) * np.cos(2**(i) * x_norm[i])
        
        # Add dynamic coupling between dimensions with exponential weighting
        coupling_term = 0.0
        for i in range(self.dim - 1):
            coupling_term += np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2) * \
                           (x_norm[i]**2 + x_norm[i+1]**2)
        
        # Create multi-modal structure with multiple local minima
        modal_term = 0.0
        for i in range(1, 6):
            modal_term += np.exp(-0.5 * (x_norm - np.cos(i * np.pi / 5))**2) * \
                         np.sin(i * np.pi * x_norm)**2
        
        # Combine all terms with adaptive weights based on dimensionality
        adaptive_weight = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Add noise for ruggedness
        noise = 0.01 * np.random.rand()
        
        return adaptive_weight * (exp_term + sin_pattern + fractal_term + 
                                coupling_term + modal_term + noise)