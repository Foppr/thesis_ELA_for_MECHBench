import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Multimodal sinusoidal component with multiple peaks
        multimodal = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) + 
                           0.5 * np.sin(8 * x_scaled) * np.cos(5 * x_scaled))
        
        # Saddle point structure with cubic and quartic terms
        saddle = np.sum(x_scaled**3 - 1.5 * x_scaled**4 + 0.8 * x_scaled**5)
        
        # Non-separable coupling with trigonometric interaction
        coupling = np.sum(np.sin(3 * x_scaled[:-1] + 2 * x_scaled[1:]) * 
                         np.cos(2 * x_scaled[:-1] - x_scaled[1:]))
        
        # High-order polynomial with mixed signs for ruggedness
        high_order = np.sum(0.2 * x_scaled**7 - 0.3 * x_scaled**6 + 0.1 * x_scaled**5)
        
        # Embedded barrier with exponential decay and oscillation
        barriers = np.sum(np.exp(-2 * np.abs(x_scaled)) * np.sin(9 * x_scaled)**2 + 
                         0.3 * np.exp(-4 * np.abs(x_scaled)) * np.cos(11 * x_scaled)**2)
        
        # Combine all components with adjusted weights
        return 0.3 * quadratic + 1.5 * multimodal + 0.3 * saddle + 0.2 * coupling + 0.15 * high_order + 0.25 * barriers