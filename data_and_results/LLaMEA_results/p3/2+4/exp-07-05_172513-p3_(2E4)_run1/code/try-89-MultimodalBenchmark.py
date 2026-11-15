import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin with adaptive weighting
        quadratic = np.sum(1.5 * x_scaled**2 + 0.5 * x_scaled**4)
        
        # Multi-frequency chaotic sinusoidal component
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) + 
                        np.sin(8 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Increased barrier complexity with multiple exponential terms
        barriers = np.sum(3.2 * np.exp(-4.0 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         1.8 * np.exp(-6.5 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2 +
                         0.9 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(3 * np.pi * x_scaled)**3)
        
        # Complex saddle structure with higher-order terms
        saddle = np.sum(x_scaled**5 - 2.8 * x_scaled**3 + 1.2 * x_scaled**4 + 0.35 * x_scaled**6)
        
        # Stronger cross-dimensional coupling with trigonometric interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(7 * np.pi * x_scaled[1:]) * 1.5)
        
        # Additional high-order polynomial with irregular coefficients
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**6 + 0.25 * x_scaled**5)
        
        # Add a global perturbation term for increased ruggedness
        perturbation = 0.8 * np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.6 * quadratic + 2.3 * chaotic + barriers + 0.35 * saddle + 0.25 * coupling + 0.15 * high_order + 0.2 * perturbation