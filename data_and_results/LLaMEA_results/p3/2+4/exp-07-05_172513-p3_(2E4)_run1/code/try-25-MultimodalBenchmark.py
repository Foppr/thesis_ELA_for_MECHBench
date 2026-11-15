import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial terms with variable exponents and chaotic coefficients
        poly_term = np.sum((x_scaled**9 + 0.6 * x_scaled**6 + 0.4 * x_scaled**4 + 0.2 * x_scaled**3 + 0.05 * x_scaled**2))
        
        # Chaotic trigonometric mixture with varying frequencies, amplitudes, and phase shifts
        trig_term = np.sum(np.sin(8 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                          np.sin(3 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * 
                          np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Adaptive radial basis functions with dynamic centers, widths, and weights
        rbf = 0
        for i in range(1, 10):
            center = np.sin(i * x_scaled * 1.1) * 0.6 + np.cos(i * x_scaled * 0.8) * 0.4
            width = 6.0 + np.sin(i * 1.5) * 3.0
            weight = 0.5 + np.cos(i * 0.7) * 0.3
            rbf += weight * np.exp(-width * np.sum((x_scaled - center)**2))
        
        # Cross-dimensional coupling with exponential interaction weights and dynamic coupling strengths
        cross_term = 0
        for i in range(self.dim - 1):
            coupling_strength = 1.0 + 0.5 * np.sin(i * 0.5)
            cross_term += coupling_strength * np.exp(-4 * np.abs(x_scaled[i] - x_scaled[i+1])) * np.sin(4 * np.pi * (x_scaled[i] + x_scaled[i+1]))
        
        # Novel entropy-based modulation term to introduce information-theoretic complexity
        entropy_modulation = 0
        for i in range(self.dim):
            prob = np.abs(x_scaled[i]) / (np.sum(np.abs(x_scaled)) + 1e-8)
            entropy_modulation += prob * np.log(prob + 1e-8)
        
        # Combine all components with dynamic weights and add a global scaling factor
        return 0.6 * poly_term + 1.8 * trig_term + 1.2 * rbf + 0.4 * cross_term + 0.2 * entropy_modulation