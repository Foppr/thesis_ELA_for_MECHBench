import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial term with varying degrees
        poly_term = np.sum(x_normalized**4 + 0.5 * x_normalized**3 + 0.2 * x_normalized**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2
            amp = 1.0 / (i + 1)
            trig_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Exponential interaction term
        exp_term = np.exp(-np.sum(x_normalized**2) * 0.5) * np.sum(np.exp(x_normalized**2))
        
        # Cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x_normalized[i] * x_normalized[j]) * (i + j + 1)
        
        # Additional noise-like component for increased complexity
        noise = 0.05 * np.sum(np.sin(10 * x_normalized) * np.cos(10 * x_normalized))
        
        # Combine all terms with appropriate weights
        return poly_term + 0.5 * trig_term + 0.3 * exp_term + 0.2 * cross_term + noise