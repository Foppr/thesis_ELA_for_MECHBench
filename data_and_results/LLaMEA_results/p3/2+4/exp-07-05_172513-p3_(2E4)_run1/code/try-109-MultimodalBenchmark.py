import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Multi-scale sinusoidal components with varying frequencies and amplitudes
        sinusoidal = np.sum(1.5 * np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                           0.8 * np.sin(8 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Asymmetric exponential barrier terms with different decay rates
        barriers = np.sum(2.0 * np.exp(-2.0 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2 + 
                         1.2 * np.exp(-4.0 * np.abs(x_scaled)) * np.cos(5 * np.pi * x_scaled)**2)
        
        # Saddle point structure with asymmetric cubic and quartic terms
        saddle = np.sum(0.8 * x_scaled**4 - 1.5 * x_scaled**2 + 0.6 * x_scaled**3 + 0.1 * x_scaled**5)
        
        # Cross-dimensional coupling with asymmetric interaction weights
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]) * 1.2 + 
                         x_scaled[:-1] * x_scaled[1:] * np.cos(4 * np.pi * x_scaled[1:]) * 0.8)
        
        # High-order polynomial term for increased ruggedness
        high_order = np.sum(0.4 * x_scaled**7 - 0.3 * x_scaled**6 + 0.2 * x_scaled**5)
        
        # Perturbation term with chaotic-like behavior
        perturbation = 0.1 * np.sum(np.sin(12 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.0 * sinusoidal + barriers + 0.3 * saddle + 0.25 * coupling + 0.15 * high_order + perturbation