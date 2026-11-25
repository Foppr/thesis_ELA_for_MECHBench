import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal chaotic component with dynamic frequency modulation
        f1 = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                   np.exp(-0.5 * np.sum(x_scaled**2)))
        
        # Polynomial coupling with asymmetric exponents and cross-dimensional interactions
        f2 = np.sum(x_scaled**3 + 0.7 * x_scaled[:-2]**3 * x_scaled[2:] + 
                   0.5 * x_scaled[:-1]**2 * x_scaled[1:] + 0.3 * x_scaled**4)
        
        # Radial barrier with logarithmic scaling and chaotic perturbations
        r = np.sqrt(np.sum(x_scaled**2))
        f3 = np.sum(np.log(r + 1) * np.exp(-r**2) * 
                   (1 + 0.2 * np.sin(10 * r) + 0.1 * np.cos(15 * r)))
        
        # Multi-scale oscillatory component with varying amplitude and phase
        f4 = np.sum(np.sin(12 * x_scaled) * np.cos(9 * x_scaled) * 
                   (1 + 0.15 * np.sin(7 * x_scaled)) * 
                   np.exp(-0.3 * np.sum(x_scaled**2)))
        
        # Asymmetric exponential-polynomial interaction with dynamic scaling
        f5 = np.sum(np.exp(-np.abs(x_scaled)**1.8) * (x_scaled**2 + 0.5 * x_scaled**3) * 
                   np.cos(4 * np.pi * x_scaled) + 0.05 * np.sin(20 * x_scaled))
        
        # Combined function with nested minima and complex curvature
        return 1.8 * f1 + 1.2 * f2 + 0.9 * f3 + 0.7 * f4 + 0.5 * f5 + 0.3 * np.sum(x_scaled**6)