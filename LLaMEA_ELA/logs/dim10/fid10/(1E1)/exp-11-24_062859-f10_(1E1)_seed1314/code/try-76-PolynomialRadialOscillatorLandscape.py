import numpy as np

class PolynomialRadialOscillatorLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial potential with varying exponents
        result = 0.0
        for i in range(self.dim):
            if i % 3 == 0:
                result += 0.1 * x[i]**4
            elif i % 3 == 1:
                result += 0.2 * x[i]**6
            else:
                result += 0.15 * x[i]**8
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                result += 2.0 * np.exp(-0.5 * (x[i] - centers[i])**2 / 0.5)
        
        # Harmonic oscillator terms with frequency modulation
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.3 * i)
            result += 0.8 * (x[i]**2) * freq
        
        # Cross-dimensional coupling with Gaussian interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist_sq = (x[i] - x[j])**2
                result += 0.5 * np.exp(-dist_sq / 2.0) * np.sin(2 * (x[i] + x[j]))
        
        # Asymmetric polynomial terms with different powers
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.3 * x[i]**3.5
            else:
                result += 0.4 * np.abs(x[i])**2.7
        
        # Multi-frequency trigonometric components
        for i in range(self.dim):
            result += 1.2 * np.sin(4 * x[i]) + 0.8 * np.cos(6 * x[i]) + 0.5 * np.sin(10 * x[i])
        
        # Fractional dimension coupling with logarithmic scaling
        if self.dim > 1:
            result += 0.3 * np.log(np.sum(x**2) + 1)
        
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result