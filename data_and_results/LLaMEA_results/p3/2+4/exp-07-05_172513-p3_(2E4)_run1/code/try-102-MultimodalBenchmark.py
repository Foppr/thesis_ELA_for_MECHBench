import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with higher frequencies
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with increased complexity and new quartic component
        barriers = np.sum(2.5 * np.exp(-3.5 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2 + 
                         0.6 * np.exp(-5.5 * np.abs(x_scaled)) * np.cos(6 * np.pi * x_scaled)**2 +
                         0.8 * np.exp(-2.0 * np.abs(x_scaled)) * x_scaled**4)
        
        # Saddle point structure with added cubic and quartic terms for increased complexity
        saddle = np.sum(x_scaled**4 - 2.2 * x_scaled**2 + 0.9 * x_scaled**3 + 0.25 * x_scaled**5)
        
        # Modified cross-dimensional coupling with stronger interaction and new frequency
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8.0 * np.pi * x_scaled[:-1]) * 1.5)
        
        # Additional high-order polynomial term to increase landscape ruggedness
        high_order = np.sum(0.35 * x_scaled**6 - 0.45 * x_scaled**5)
        
        # Add a small perturbation to the chaotic term to increase complexity
        perturbation = 0.05 * np.sum(np.sin(18 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.45 * quadratic + 2.1 * chaotic + barriers + 0.28 * saddle + 0.22 * coupling + 0.12 * high_order + perturbation