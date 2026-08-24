import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial terms with variable exponents and dynamic coefficients
        poly_term = np.sum(0.8 * x_scaled**9 + 0.6 * x_scaled**6 + 0.4 * x_scaled**4 + 0.2 * x_scaled**3)
        
        # Chaotic trigonometric mixture with time-varying frequencies and amplitudes
        trig_term = np.sum(np.sin(9 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                          np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                          np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Adaptive radial basis functions with dynamic centers, widths, and weights
        rbf = 0
        for i in range(1, 10):
            center = np.sin(i * x_scaled * 1.2) * 0.6 + np.cos(i * x_scaled * 0.8) * 0.4
            width = 4.0 + np.sin(i * 1.5) * 3.0
            weight = 0.5 + np.cos(i * 0.7) * 0.3
            rbf += weight * np.exp(-width * np.sum((x_scaled - center)**2))
        
        # Cross-dimensional coupling with multi-scale interaction weights
        cross_term = 0
        for i in range(self.dim - 1):
            for j in range(1, 4):
                cross_term += np.exp(-3 * np.abs(x_scaled[i] - x_scaled[i+j])) * np.sin(2 * np.pi * (x_scaled[i] + x_scaled[i+j]) * j)
        
        # Novel hybrid energy term combining exponential and polynomial interactions
        hybrid_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                hybrid_term += np.exp(-dist**2) * (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(5 * np.pi * (x_scaled[i] + x_scaled[j]))
        
        # Global modulation with dynamic phase and amplitude
        modulation = np.sin(12 * np.sum(x_scaled**2)) * np.cos(8 * np.sum(x_scaled)) * 0.6
        
        # Combine all components with optimized weights
        return 0.7 * poly_term + 1.8 * trig_term + 1.1 * rbf + 0.5 * cross_term + 0.4 * hybrid_term + 0.2 * modulation