import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic sinusoidal component with higher frequencies and amplitude
        chaotic = np.sum(2.5 * np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Complex exponential barrier terms with multiple peaks and varying amplitudes
        barriers = np.sum(4.0 * np.exp(-5.0 * np.abs(x_scaled)) * np.sin(7 * np.pi * x_scaled)**2 + 
                         1.2 * np.exp(-8.0 * np.abs(x_scaled)) * np.cos(12 * np.pi * x_scaled)**2 +
                         0.5 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(18 * np.pi * x_scaled)**2)
        
        # Saddle point structure with higher-order polynomial terms and mixed signs
        saddle = np.sum(x_scaled**6 - 3.0 * x_scaled**3 + 1.5 * x_scaled**4 - 0.8 * x_scaled**5)
        
        # Stronger cross-dimensional coupling with trigonometric interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(10 * np.pi * x_scaled[:-1]) * 2.0)
        
        # Additional high-order polynomial term with increased ruggedness
        high_order = np.sum(0.7 * x_scaled**8 - 0.9 * x_scaled**6 + 0.4 * x_scaled**5 - 0.2 * x_scaled**4)
        
        # Logistic map component with modified growth parameter for increased chaos
        logistic = np.sum(5.0 * x_scaled * (1 - x_scaled**2))
        
        # Additional multimodal component with multiple local minima
        multimodal = np.sum(1.5 * np.sin(25 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled) + 
                           0.8 * np.sin(30 * np.pi * x_scaled)**2)
        
        # Combine all components with adjusted weights
        return 0.4 * quadratic + 2.8 * chaotic + barriers + 0.4 * saddle + 0.25 * coupling + 0.2 * high_order + 0.15 * logistic + 0.2 * multimodal