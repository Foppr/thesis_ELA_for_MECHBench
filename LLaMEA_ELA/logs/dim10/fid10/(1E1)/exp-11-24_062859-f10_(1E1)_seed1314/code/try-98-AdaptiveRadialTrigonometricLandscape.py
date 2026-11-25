import numpy as np

class AdaptiveRadialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for each dimension
        self.scales = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and scaling
        for i in range(self.dim):
            xi = x[i]
            # Adaptive polynomial with increasing degree
            poly_term = self.scales[i] * (xi**2 + 0.5*xi**4 + 0.1*xi**6)
            result += poly_term
        
        # Trigonometric components with dynamic frequencies
        for i in range(self.dim):
            xi = x[i]
            # Multiple trigonometric terms with increasing frequency
            trig_term = 2.0 * np.sin(3 * xi) + 1.5 * np.cos(5 * xi) + 0.8 * np.sin(7 * xi)
            result += trig_term
        
        # Radial basis function components with adaptive centers and widths
        for i in range(self.dim):
            rb_sum = 0.0
            for j in range(min(3, self.dim)):  # Limited interaction
                center = 2.0 * np.sin(j * np.pi / 4)
                width = 0.5 + 0.3 * np.cos(j * np.pi / 3)
                rb_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
            result += 1.2 * rb_sum
        
        # Cross-dimensional coupling with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = np.sin(2 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
                result += 0.7 * coupling
        
        # Adaptive conditioning based on dimension
        for i in range(self.dim):
            result += 0.3 * self.scales[i] * np.abs(x[i])**1.5
        
        # Noise component to prevent trivial solutions
        noise = 0.02 * np.random.standard_normal()
        result += noise
        
        return result