import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial terms with variable exponents
        poly_term = np.sum((x_scaled**8 + 0.7 * x_scaled**5 + 0.3 * x_scaled**3 + 0.1 * x_scaled**2))
        
        # Chaotic trigonometric mixture with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) * 
                          np.sin(2 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Adaptive radial basis functions with dynamic centers and widths
        rbf = 0
        for i in range(1, 8):
            center = np.sin(i * x_scaled) * 0.5 + np.cos(i * x_scaled * 0.7) * 0.3
            width = 5.0 + np.sin(i) * 2.0
            rbf += np.exp(-width * np.sum((x_scaled - center)**2))
        
        # Cross-dimensional coupling with exponential interaction weights
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += np.exp(-5 * np.abs(x_scaled[i] - x_scaled[i+1])) * np.sin(3 * np.pi * (x_scaled[i] + x_scaled[i+1]))
        
        # Add a global modulation term based on the sum of all dimensions
        modulation = np.sin(10 * np.sum(x_scaled**2)) * 0.5
        
        # Combine all components with dynamic weights
        return 0.5 * poly_term + 1.5 * trig_term + 0.9 * rbf + 0.3 * cross_term + 0.1 * modulation