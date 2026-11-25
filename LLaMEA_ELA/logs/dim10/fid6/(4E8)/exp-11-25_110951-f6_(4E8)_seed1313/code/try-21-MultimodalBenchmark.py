import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with modified scaling
        term1 = np.sum(x_normalized**2)
        
        # Enhanced sinusoidal components with chaotic frequency interactions
        term2 = 0.3 * np.sum(np.sin(5 * np.pi * x_normalized) + 
                            0.7 * np.sin(11 * np.pi * x_normalized) + 
                            0.4 * np.sin(17 * np.pi * x_normalized))
        
        # Higher-order polynomial term to create sharper optima
        term3 = 0.05 * np.sum(x_normalized**8)
        
        # Cross-term coupling with trigonometric interactions
        cross_term = 0.2 * np.sum(np.sin(4 * np.pi * x_normalized) * 
                                np.cos(6 * np.pi * x_normalized))
        
        # Dynamic penalty regions based on cluster proximity
        penalty = 0.1 * np.sum(np.abs(x_normalized) > 0.8) * np.sum(np.sin(13 * np.pi * x_normalized)**2)
        
        # Additional chaotic sinusoidal component with varying amplitude and phase
        term4 = 0.25 * np.sum(np.sin(19 * np.pi * x_normalized**3) + 
                             0.3 * np.sin(23 * np.pi * x_normalized**4))
        
        # Combine all terms to create a challenging landscape
        return term1 + term2 + term3 + cross_term + penalty + term4