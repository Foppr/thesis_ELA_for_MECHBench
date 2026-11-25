import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree and nonlinearity
        polynomial = np.sum(x**2) + 0.15 * np.sum(x**4) + 0.02 * np.sum(x**6) + 0.005 * np.sum(x**8)
        
        # Multi-frequency sinusoidal oscillations with adaptive modulation
        freq1 = np.sin(7.0 * x)
        freq2 = np.sin(4.0 * x)
        freq3 = np.sin(2.0 * x)
        adaptive_modulation = np.prod(np.sin(0.3 * x) + 1.5) + 1.0
        
        sinusoidal = (np.sum(freq1) + np.sum(freq2) + np.sum(freq3)) * np.exp(-0.2 * np.sum(x**2)) * adaptive_modulation
        
        # Complex cross-dimensional interactions with coupling strength
        cross_terms = 0.7 * np.sum(x[:-1] * x[1:]) + 0.3 * np.sum(x**2 * x[::-1]**2) + 0.1 * np.sum(np.abs(x[:-2] - x[2:]))
        
        # Grid of shifted local minima with enhanced cosine modulation
        shifted_x = x + 0.7
        grid_minima = np.sum(np.cos(3.0 * shifted_x) * np.exp(-0.05 * np.sum(x**2)))
        
        # Additional nonlinear interaction term with trigonometric coupling
        nonlinear_interaction = 0.08 * np.sum(np.sin(0.4 * x) * np.cos(0.6 * x) * np.sin(0.8 * x))
        
        # Novel cross-dimensional interaction with exponential decay
        cross_dim_interaction = np.exp(-0.1 * np.sum((x - np.mean(x))**2)) * np.sum(x**3)
        
        return polynomial + sinusoidal + cross_terms + grid_minima + nonlinear_interaction + cross_dim_interaction