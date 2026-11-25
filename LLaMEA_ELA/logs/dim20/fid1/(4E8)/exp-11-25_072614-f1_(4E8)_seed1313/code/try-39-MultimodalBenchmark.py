import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial terms with higher degree components
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(5.0 * x)) + 0.5 * np.sum(np.sin(10.0 * x)) + 0.1 * np.sum(np.sin(15.0 * x))
        
        # Chaotic perturbations using logistic map-like behavior
        chaos = 0.05 * np.sum(np.sin(x * np.pi * (1 + np.sin(x))))
        
        # Interference patterns from multiple sinusoidal components with modified interaction
        interference = 0.3 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x)) + 0.2 * np.sum(np.sin(4.0 * x) * np.cos(7.0 * x))
        
        # Additional multimodal component with exponential modulation
        exp_modulation = 0.1 * np.sum(np.exp(-0.5 * x**2) * np.sin(8.0 * x))
        
        # Gradient complexity enhancement with cross-terms
        gradient_complexity = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]))
        
        # Combined function with global minimum at origin and enhanced multimodality
        return polynomial + sinusoidal + chaos + interference + exp_modulation + gradient_complexity + 0.05 * np.sum(x**8)