import numpy as np

class PolynomialRadialGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial potential with varying degrees
        result = 0.0
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.3 * x[i]**2
        
        # Radial basis function components with multiple centers
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            rb_value = 0.0
            for j, center in enumerate(centers):
                if j < self.dim:
                    rb_value += 2.0 * np.exp(-0.5 * (x[i] - center)**2) * np.sin(2 * np.pi * (x[i] - center))
            result += rb_value
        
        # Directional gradient fields with cosine modulation
        for i in range(self.dim):
            grad_field = 0.0
            for j in range(max(1, i-2), min(i+3, self.dim)):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    grad_field += 1.5 * np.cos(3 * dist) * np.exp(-0.1 * dist**2)
            result += 0.5 * grad_field
        
        # Multi-scale harmonic potentials with phase shifts
        for i in range(self.dim):
            result += 1.2 * np.sin(4 * x[i]) + 0.8 * np.cos(7 * x[i]) + 0.6 * np.sin(11 * x[i])
        
        # Cross-dimensional coupling with elliptical contours
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * (x[i]**2 + 0.5 * x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Asymmetric polynomial terms with different exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.4 * x[i]**3.5 + 0.1 * x[i]**6
            else:
                result += 0.3 * x[i]**2.7 + 0.2 * x[i]**5
        
        # Noise component to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result