import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and chaotic modulation
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * 
                         np.sin(7 * np.pi * x_scaled**2) * np.cos(5 * np.pi * x_scaled**3))
        
        # Enhanced exponential barrier terms with increased complexity and chaotic modulation
        barriers = np.sum(3.0 * np.exp(-4 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         1.0 * np.exp(-6 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2 +
                         0.5 * np.exp(-2 * np.abs(x_scaled)) * np.sin(9 * np.pi * x_scaled)**4)
        
        # Saddle point structure with added cubic, quartic, and quintic terms for increased complexity
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**4 + 1.2 * x_scaled**3 - 0.8 * x_scaled**2 + 0.6 * x_scaled**6)
        
        # Modified cross-dimensional coupling with stronger interaction and chaotic modulation
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(6 * np.pi * x_scaled[1:]) * 1.2)
        
        # Additional high-order polynomial term to increase landscape ruggedness with chaotic modulation
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**6 + 0.3 * x_scaled**5)
        
        # Add a chaotic perturbation term to increase landscape complexity
        perturbation = np.sum(0.2 * np.sin(20 * np.pi * x_scaled) * np.cos(17 * np.pi * x_scaled) * 
                             np.sin(13 * np.pi * x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.2 * chaotic + barriers + 0.3 * saddle + 0.2 * coupling + 0.15 * high_order + 0.1 * perturbation