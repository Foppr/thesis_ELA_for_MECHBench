import numpy as np

class PolynomialGaussianLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced polynomial potential terms with higher degree and nonlinearity
        for i in range(self.dim):
            poly_term = (x[i]**5 + 0.7 * x[i]**4 + 0.3 * x[i]**3 + 0.15 * x[i]**2 + 0.05 * x[i])
            result += 0.3 * poly_term**2
        
        # Modified Gaussian ridge structures with dynamic widths and heights
        for i in range(self.dim):
            ridge_sum = 0.0
            for j in range(1, 7):  # Increased number of components
                width = 0.3 + 0.1 * j
                height = 1.0 / (j**1.5 * (j + 1))
                ridge_sum += height * np.exp(-0.5 * ((x[i] - j) / width)**2)
            result += 0.4 * ridge_sum**2
        
        # Enhanced cross-dimensional coupling with nonlinear interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**3 + x[j]**3) * np.cos(0.3 * (x[i] - x[j]))
                result += 0.2 * coupling**2
        
        # Improved noise injection with spatial correlation
        noise_scale = 0.08 + 0.03 * np.sin(self.dim * 0.5)
        for i in range(self.dim):
            noise = np.random.normal(0, noise_scale) if np.random.rand() < 0.4 else 0
            result += 0.1 * (x[i] + noise)**3
        
        # Dynamic conditioning based on local curvature and gradient
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(5*x[i]**4 + 2.8*x[i]**3 + 0.9*x[i]**2 + 0.3*x[i] + 0.05)
        conditioning = 1.0 + 0.15 * np.tanh(grad_magnitude / self.dim)
        result *= conditioning
        
        # Fractal-like structure with improved scaling and amplitude
        fractal_sum = 0.0
        for i in range(self.dim):
            for freq in [1, 3, 6, 12]:
                fractal_sum += np.sin(freq * x[i]) * np.exp(-0.05 * (freq - 6)**2)
        result += 0.3 * fractal_sum**2
        
        # Additional non-separable components for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    result += 0.05 * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2)
        
        # Final normalization and bias term
        result /= self.dim
        result += 0.015 * np.sum(np.abs(x)**1.5)
        
        return result