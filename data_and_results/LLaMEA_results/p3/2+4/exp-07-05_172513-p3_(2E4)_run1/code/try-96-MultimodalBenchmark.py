import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced quadratic basin with elliptical contours
        quadratic = np.sum(1.5 * x_scaled**2 + 0.5 * x_scaled**4)
        
        # Multi-frequency chaotic sinusoidal component
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled) + 
                        np.sin(8 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled))
        
        # Increased barrier complexity with higher exponential terms
        barriers = np.sum(3.2 * np.exp(-4.0 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2 + 
                         1.8 * np.exp(-6.5 * np.abs(x_scaled)) * np.cos(8 * np.pi * x_scaled)**2 +
                         0.9 * np.exp(-7.0 * np.abs(x_scaled)) * np.sin(9 * np.pi * x_scaled)**3)
        
        # Complex saddle structure with higher-order polynomial terms
        saddle = np.sum(x_scaled**5 - 2.8 * x_scaled**3 + 1.2 * x_scaled**2 + 0.8 * x_scaled**4 + 0.35 * x_scaled**6)
        
        # Stronger cross-dimensional coupling with trigonometric interaction
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(8 * np.pi * x_scaled[:-1]) * 
                         np.cos(7 * np.pi * x_scaled[1:]) * 1.5)
        
        # Additional high-order polynomial term with irregular coefficients
        high_order = np.sum(0.5 * x_scaled**7 - 0.6 * x_scaled**6 + 0.4 * x_scaled**5)
        
        # Add a global sinusoidal modulation to increase landscape complexity
        modulation = 0.8 * np.sin(3 * np.pi * np.sum(x_scaled**2))
        
        # Combine all components with adjusted weights
        return 0.5 * quadratic + 2.2 * chaotic + barriers + 0.35 * saddle + 0.25 * coupling + 0.15 * high_order + modulation