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
        chaotic = np.sum(2.5 * np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) + 
                        1.8 * np.sin(25 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled))
        
        # Complex exponential barrier terms with multiple components
        barriers = np.sum(4.0 * np.exp(-5.0 * np.abs(x_scaled)) * np.sin(7 * np.pi * x_scaled)**2 + 
                         1.5 * np.exp(-7.0 * np.abs(x_scaled)) * np.cos(11 * np.pi * x_scaled)**2 +
                         0.9 * np.exp(-3.0 * np.abs(x_scaled)) * np.sin(9 * np.pi * x_scaled)**3)
        
        # Enhanced saddle point structure with higher-order polynomial terms
        saddle = np.sum(x_scaled**6 - 3.0 * x_scaled**2 + 1.5 * x_scaled**4 + 0.5 * x_scaled**7 + 0.2 * x_scaled**8)
        
        # Stronger cross-dimensional coupling with trigonometric interactions
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(12 * np.pi * x_scaled[:-1]) * 
                         np.cos(10 * np.pi * x_scaled[1:]) * 2.0)
        
        # Additional high-order polynomial term with increased ruggedness
        high_order = np.sum(0.7 * x_scaled**8 - 0.8 * x_scaled**6 + 0.3 * x_scaled**5 + 0.1 * x_scaled**9)
        
        # Add a modified logistic map component with higher chaos
        logistic = np.sum(5.0 * x_scaled * (1 - x_scaled**2) + 0.5 * x_scaled**3)
        
        # Add a multi-modal Gaussian component for additional local optima
        gaussian = np.sum(2.0 * np.exp(-2.0 * (x_scaled - 0.5)**2) + 1.5 * np.exp(-1.5 * (x_scaled + 0.3)**2))
        
        # Combine all components with adjusted weights
        return 0.6 * quadratic + 3.0 * chaotic + barriers + 0.4 * saddle + 0.3 * coupling + 0.2 * high_order + 0.15 * logistic + 0.25 * gaussian