import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with enhanced frequency modulation and amplitude scaling
        f2 = 0.8 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm))
        
        # Add higher-order polynomial terms with increased weights for greater landscape complexity
        f3 = 0.25 * np.sum(x_norm**8)
        
        # Introduce cross-terms with stronger non-linear coupling and modified exponents
        f4 = 0.35 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * x_norm**4)
        
        # Additional polynomial cross-terms with varying exponents and increased coefficients
        f5 = 0.12 * np.sum(x_norm**5 * np.sin(7 * np.pi * x_norm))
        
        # Shifted and modulated sinusoidal component with enhanced parameters to create additional local optima
        f6 = 0.35 * np.sum(np.sin(6 * np.pi * (x_norm + 0.2)) * np.cos(8 * np.pi * (x_norm - 0.15)) * np.tan(4 * np.pi * x_norm))
        
        # New quintic cross-term with enhanced frequency modulation and coupling
        f7 = 0.2 * np.sum(x_norm**5 * np.cos(4 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Non-linear interaction term with increased weights and complex coupling
        f8 = 0.25 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * (x_norm**3 + 0.2))
        
        # Add exponential decay modulation to increase landscape complexity
        f9 = 0.15 * np.sum(np.exp(-x_norm**2) * np.sin(5 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Add a new sixth-order polynomial term with enhanced non-linearity
        f10 = 0.18 * np.sum(x_norm**6 * np.sin(4 * np.pi * x_norm))
        
        # Combine all components with adjusted weights for optimal multimodality
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result