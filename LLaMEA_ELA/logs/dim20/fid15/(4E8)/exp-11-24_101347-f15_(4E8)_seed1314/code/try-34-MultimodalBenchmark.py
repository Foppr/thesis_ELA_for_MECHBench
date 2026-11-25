import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with multiple peaks and exponential decay
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.05 * r) * np.sin(5.0 * r) * np.cos(2.0 * r)
        
        # Enhanced trigonometric coupling with chaotic behavior
        trig_coupling = np.prod(np.sin(3.0 * x + np.sin(x)) + 1.5)
        
        # Additional cross-dimensional polynomial terms
        poly_perturb = 0.02 * np.sum(x**4) + 0.005 * np.sum(x**8)
        
        # Chaotic multimodal term with multiple local minima
        multi_term = np.sum(np.sin(7.0 * x) * np.cos(9.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Add a dynamic conditioning factor that varies with position
        condition_factor = 1.0 + 0.5 * np.sin(0.5 * r)
        
        return condition_factor * (radial + trig_coupling + poly_perturb + multi_term)