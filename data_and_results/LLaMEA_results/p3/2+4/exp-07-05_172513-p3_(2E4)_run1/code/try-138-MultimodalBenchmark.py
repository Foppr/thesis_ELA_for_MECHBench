import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Coupled oscillatory components with varying coupling strengths
        oscillatory = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled) + 
                            0.5 * np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Adaptive penalty terms with dynamic scaling based on dimensionality
        penalties = np.sum(3.0 * np.exp(-4.0 * np.abs(x_scaled)) * np.sin(6 * np.pi * x_scaled)**2 + 
                          2.0 * np.exp(-5.0 * np.abs(x_scaled)) * np.cos(9 * np.pi * x_scaled)**2)
        
        # Saddle point structure with enhanced nonlinearity and interaction
        saddle = np.sum(x_scaled**5 - 2.5 * x_scaled**3 + 1.2 * x_scaled**4 + 0.3 * x_scaled**6)
        
        # Cross-dimensional coupling with directional modulation
        coupling = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(10 * np.pi * x_scaled[:-1]) * 
                         np.cos(5 * np.pi * x_scaled[1:]) * 1.5)
        
        # High-order polynomial with mixed interaction terms
        high_order = np.sum(0.6 * x_scaled**8 - 0.7 * x_scaled**5 + 0.3 * x_scaled**4 + 0.2 * x_scaled**7)
        
        # Modified logistic map with higher chaos degree and non-uniform scaling
        logistic = np.sum(3.8 * x_scaled * (1 - x_scaled**2) + 0.2 * x_scaled**3 * (1 - x_scaled**2))
        
        # Gradient flow modulation to introduce directional complexity
        gradient_mod = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) * 
                             (x_scaled**2 + 0.5))
        
        # Combine all components with optimized weights
        return 0.8 * quadratic + 2.5 * oscillatory + penalties + 0.6 * saddle + 0.4 * coupling + 0.3 * high_order + 0.25 * logistic + 0.15 * gradient_mod