import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree and additional complexity
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6) + 0.001 * np.sum(x**8)
        
        # Sinusoidal oscillations with multiple frequencies, grid-based modulation, and phase shifts
        freq1 = np.sin(5.0 * x + np.pi/4)
        freq2 = np.sin(3.0 * x + np.pi/3)
        freq3 = np.sin(7.0 * x + np.pi/6)
        grid_modulation = np.prod(np.sin(0.5 * x) + 1.0) + 1.0
        
        sinusoidal = (np.sum(freq1) + np.sum(freq2) + np.sum(freq3)) * np.exp(-0.1 * np.sum(x**2)) * grid_modulation
        
        # Cross-term interactions with additional coupling and non-linear transformations
        cross_terms = np.sum(x[:-1] * x[1:]) * 0.5 + 0.1 * np.sum(x**2 * x[::-1]**2) + 0.05 * np.sum(np.sin(x) * np.cos(x[::-1]))
        
        # Add a grid of local minima using cosine modulation with additional harmonic components
        grid_minima = np.sum(np.cos(2.0 * x) * np.exp(-0.05 * np.sum(x**2))) + 0.5 * np.sum(np.cos(4.0 * x) * np.exp(-0.02 * np.sum(x**2)))
        
        # Introduce a novel exponential decay term with radial basis function components
        rbf_terms = np.sum(np.exp(-0.5 * (x - 1)**2)) + np.sum(np.exp(-0.5 * (x + 1)**2))
        
        # Add a stochastic-like perturbation component for increased complexity
        noise = 0.01 * np.random.rand()
        
        return polynomial + sinusoidal + cross_terms + grid_minima + rbf_terms + noise