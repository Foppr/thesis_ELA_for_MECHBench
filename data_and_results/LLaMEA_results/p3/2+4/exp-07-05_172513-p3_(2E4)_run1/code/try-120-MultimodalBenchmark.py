import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        sinusoidal = np.sum(np.sin(20 * x_scaled) * np.cos(12 * x_scaled) + 
                           0.5 * np.sin(30 * x_scaled) * np.cos(15 * x_scaled) + 
                           0.3 * np.sin(25 * x_scaled) * np.cos(18 * x_scaled))
        
        # Asymmetric exponential barriers with different decay rates
        barriers = np.sum(2.0 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(6 * np.pi * x_scaled)**2 + 
                         1.5 * np.exp(-5.0 * np.abs(x_scaled)) * np.cos(7 * np.pi * x_scaled)**2 + 
                         0.8 * np.exp(-2.0 * np.abs(x_scaled)) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Cubic and quartic terms to create saddle points and local minima
        polynomial = np.sum(0.5 * x_scaled**3 - 0.8 * x_scaled**4 + 0.3 * x_scaled**5)
        
        # Cross-dimensional coupling with trigonometric functions
        coupling = np.sum(np.sin(10 * x_scaled[:-1]) * np.cos(10 * x_scaled[1:]) * 
                         (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # High-frequency chaotic component
        chaotic = np.sum(np.sin(50 * x_scaled) * np.cos(40 * x_scaled) * 
                        np.exp(-0.5 * x_scaled**2))
        
        # Additional asymmetric polynomial terms for increased ruggedness
        asymmetric = np.sum(0.4 * x_scaled**6 - 0.7 * x_scaled**3 + 0.2 * x_scaled**8)
        
        # Combine all components with different weights
        return 0.3 * quadratic + 1.8 * sinusoidal + barriers + 0.25 * polynomial + 0.15 * coupling + 0.2 * chaotic + 0.1 * asymmetric