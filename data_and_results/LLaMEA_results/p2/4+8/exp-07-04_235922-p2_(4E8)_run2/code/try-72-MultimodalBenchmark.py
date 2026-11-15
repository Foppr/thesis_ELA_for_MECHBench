import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        term1 = np.sum(x**2)
        
        # Composite sinusoidal modulations with varying frequencies
        term2 = 0.5 * np.sum(np.sin(5 * x) * np.cos(3 * x) * np.sin(2 * x))
        
        # Adaptive polynomial coupling with dynamic exponents
        term3 = 0.3 * np.sum((x**4 + 0.5 * x**3 + 0.2 * x**2) * np.cos(6 * x))
        
        # Dynamic gradient-based barrier component
        grad_x = np.gradient(x)
        barrier = 0.4 * np.sum(np.exp(-0.5 * grad_x**2) * np.sin(10 * x))
        
        # Nested multimodal structure with chaotic interactions
        nested = 0.25 * np.sum(np.sin(10 * x) * np.cos(7 * x) * np.sin(3 * x) * np.cos(2 * x))
        
        # Multi-scale chaotic component
        chaotic = 0.1 * np.sum(np.sin(15 * x) * np.exp(-0.1 * np.abs(x)) * np.cos(8 * x))
        
        # Asymmetric polynomial interactions
        asym = 0.15 * np.sum(np.abs(x)**3.7 * np.sin(4 * x) * np.cos(3 * x))
        
        # Cross-dimension coupling with exponential decay
        coupling = 0.05 * np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(12 * (x[:-1] + x[1:])))
        
        result = term1 + term2 + term3 + barrier + nested + chaotic + asym + coupling
        
        # Add small random perturbation for increased difficulty
        result += 0.0005 * np.random.random()
        
        return result