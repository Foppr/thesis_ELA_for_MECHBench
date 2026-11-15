import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin with non-uniform weights
        quadratic = np.sum((x_scaled**2) * (1.0 + 0.5 * np.sin(5 * x_scaled)))
        
        # Multi-frequency chaotic sinusoidal component
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) + 
                        0.7 * np.sin(8 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled))
        
        # Increased barrier complexity with multiple exponential terms
        barriers = np.sum(3.0 * np.exp(-4 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         1.5 * np.exp(-6 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2 +
                         0.8 * np.exp(-2 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled)**3)
        
        # Complex saddle point structure with mixed polynomial orders
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**3 + 1.2 * x_scaled**4 + 0.5 * x_scaled**6)
        
        # Stronger cross-dimensional coupling with trigonometric interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(7 * np.pi * x_scaled[1:]) * 1.2)
        
        # High-order polynomial with multiple local minima
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**6 + 0.3 * x_scaled**5)
        
        # Additional chaotic modulation term
        modulation = np.sum(0.4 * np.sin(20 * x_scaled) * np.cos(18 * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.2 * chaotic + barriers + 0.3 * saddle + 0.2 * coupling + 0.15 * high_order + 0.2 * modulation