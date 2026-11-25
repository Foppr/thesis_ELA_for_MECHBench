import numpy as np

class AsymmetricMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial terms with varying exponents and coefficients
        f1 = np.sum(0.5 * x_scaled**6 + 0.3 * x_scaled**4 + 0.7 * x_scaled**2)
        
        # Trigonometric components with frequency modulation and phase shifts
        f2 = np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # Radial basis functions with non-uniform centers and widths
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.3 + 0.1 * np.sin(i * 0.5)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Cross-dimensional interaction with asymmetric weights and nonlinear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight_ij = (i + 1) * (j + 1) / (self.dim * (self.dim - 1) / 2)
                f4 += weight_ij * np.sin(x_scaled[i]**3) * np.cos(x_scaled[j]**2)
        
        # Asymmetric saddle structure with modified curvature
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.5 * (x_scaled**3 - 0.2*x_scaled)**2)
        
        # High-frequency oscillation with amplitude modulation
        f6 = np.sum(np.sin(50 * x_scaled) * np.cos(45 * x_scaled) * 
                   np.exp(-0.1 * np.abs(x_scaled)))
        
        # Boundary penalty with variable exponents
        f7 = 0.8 * np.sum((np.abs(x_scaled)**2.5 + 0.3 * np.abs(x_scaled)**1.2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7