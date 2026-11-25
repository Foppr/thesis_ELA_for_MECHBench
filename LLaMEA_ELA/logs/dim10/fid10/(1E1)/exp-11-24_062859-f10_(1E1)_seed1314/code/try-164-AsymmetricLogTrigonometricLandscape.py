import numpy as np

class AsymmetricLogTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with asymmetric scaling
        result = 0.01 * np.sum(np.abs(x)**3)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 3.0 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i]) * (1 + 0.3 * np.sin(0.7 * x[i]))
        
        # Logarithmic barrier terms to encourage exploration near boundaries
        for i in range(self.dim):
            result += 2.0 * (np.log(np.abs(x[i]) + 1) + 1) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with asymmetric interaction weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(3 * x[i]) * np.cos(2 * x[j]) + 0.5 * np.cos(4 * x[i]) * np.sin(x[j])
                weight = 0.8 if i % 2 == 0 else 1.2
                result += weight * interaction * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Asymmetric polynomial terms with different exponents
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.5 * x[i]**4 * np.exp(-0.3 * x[i])
            else:
                result += 0.8 * np.abs(x[i])**2.5 * np.exp(-0.4 * np.abs(x[i]))
        
        # High-frequency noise component with controlled amplitude
        for i in range(self.dim):
            result += 1.2 * np.sin(13 * x[i]) * np.cos(9 * x[i])
        
        # Add small random perturbation to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result