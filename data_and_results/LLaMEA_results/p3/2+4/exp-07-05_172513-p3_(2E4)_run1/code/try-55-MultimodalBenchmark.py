import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin term with variable weighting
        quadratic = np.sum(1.5 * x_scaled**2)
        
        # High-frequency chaotic sinusoidal component with exponential modulation
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) * np.exp(-0.5 * np.abs(x_scaled)))
        
        # Multi-scale exponential barrier terms with varying amplitudes and frequencies
        barriers = np.sum(2.5 * np.exp(-3 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**3 + 
                         1.2 * np.exp(-6 * np.abs(x_scaled)) * np.cos(4 * np.pi * x_scaled)**2)
        
        # Higher-order saddle point structure with quintic and sextic terms
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**3 + 0.8 * x_scaled**4 - 0.3 * x_scaled**2 + 0.5 * x_scaled**6)
        
        # Stronger cross-dimensional coupling with trigonometric modulation and increased weight
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(6 * np.pi * x_scaled[1:]) * 1.2)
        
        # Additional noise-like component with irregular frequency modulation
        noise = np.sum(0.5 * np.sin(20 * np.pi * x_scaled + np.sin(10 * np.pi * x_scaled)) * 
                      np.cos(18 * np.pi * x_scaled + np.cos(9 * np.pi * x_scaled)))
        
        # Combined function with adjusted weights for maximum complexity
        return 0.8 * quadratic + 3.0 * chaotic + barriers + 0.4 * saddle + 0.2 * coupling + 0.3 * noise