import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying exponents
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with different frequencies and amplitudes
        sinusoidal = 2.0 * np.sum(np.sin(3.0 * x)) + 1.5 * np.sum(np.sin(7.0 * x)**2) + 0.5 * np.sum(np.cos(5.0 * x))
        
        # Asymmetric cross-terms to increase complexity and reduce algorithm bias
        cross_terms = 0.3 * np.sum(x[:-1] * x[1:]**3) + 0.2 * np.sum(x[:-2] * x[2:]**2)
        
        # Additional nonlinearity with exponential and logarithmic-like behavior
        nonlinear = 0.1 * np.sum(np.exp(0.5 * x**2) - 1.0) + 0.2 * np.sum(np.sin(9.0 * x) * np.cos(4.0 * x))
        
        # Introduce a conditioning factor to make the landscape more challenging
        condition_factor = 1.0 + 0.1 * np.sum(np.abs(x)**3)
        
        return (polynomial + sinusoidal + cross_terms + nonlinear) * condition_factor