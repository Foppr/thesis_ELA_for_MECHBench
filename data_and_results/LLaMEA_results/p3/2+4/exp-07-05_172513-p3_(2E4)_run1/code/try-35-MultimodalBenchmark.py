import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # High-frequency chaotic sinusoidal component with multiple harmonics
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) * np.sin(8 * np.pi * x_scaled))
        
        # Enhanced exponential barrier terms with modified weights and additional sine modulation
        barriers = np.sum(2.0 * np.exp(-6 * np.abs(x_scaled)) * (np.sin(5 * np.pi * x_scaled)**2 + 0.5 * np.cos(3 * np.pi * x_scaled)**2))
        
        # Complex saddle point structure with higher-order polynomial terms
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Stronger cross-dimensional coupling with trigonometric modulation
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * np.cos(6 * np.pi * x_scaled[1:]))
        
        # Additional noise-like term to increase landscape ruggedness
        noise = 0.5 * np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(18 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.3 * quadratic + 3.0 * chaotic + barriers + 0.5 * saddle + 0.2 * coupling + 0.1 * noise