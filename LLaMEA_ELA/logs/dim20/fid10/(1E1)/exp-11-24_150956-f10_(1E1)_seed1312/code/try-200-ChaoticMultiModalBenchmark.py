import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logistic map chaotic component with varying r values
        logistic = np.sum(4.0 * x_scaled * (1.0 - x_scaled))
        
        # Trigonometric coupling with fractal-like behavior
        trig_coupling = np.sum(np.sin(10.0 * x_scaled) * np.cos(8.0 * x_scaled) + 
                             np.sin(15.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                             np.sin(20.0 * x_scaled**3) * np.cos(16.0 * x_scaled**3))
        
        # Multi-scale fractal irregularities
        fractal = np.sum(np.abs(x_scaled)**1.5 + 0.5 * np.abs(x_scaled)**2.5 + 
                        0.2 * np.abs(x_scaled)**3.5)
        
        # Cross-dimensional chaotic interactions
        cross_interaction = np.sum(np.sin(5.0 * (x_scaled[:-1] + x_scaled[1:])) * 
                                 np.cos(3.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                                 np.sin(7.0 * (x_scaled[:-2] + x_scaled[2:])) * 
                                 np.cos(4.0 * (x_scaled[:-2] - x_scaled[2:])))
        
        # Asymmetric saddle points with polynomial distortions
        saddle = np.sum((x_scaled**2 - 0.5)**3 + 0.3 * (x_scaled**3 - 0.7*x_scaled)**2)
        
        # Add noise-like perturbations for increased complexity
        noise = 0.1 * np.random.rand(self.dim) if self.dim > 0 else 0
        
        return 0.4 * logistic + 0.3 * trig_coupling + 0.15 * fractal + 0.1 * cross_interaction + 0.05 * saddle + np.sum(noise)