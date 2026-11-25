import numpy as np

class AsymmetricMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with asymmetric conditioning
        result = 0.1 * np.sum(x**2)
        
        # Polynomial terms with varying degrees and signs
        for i in range(self.dim):
            if i % 3 == 0:
                result += 0.5 * x[i]**4
            elif i % 3 == 1:
                result -= 0.3 * x[i]**5
            else:
                result += 0.7 * x[i]**6
        
        # Trigonometric components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 1.2 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.8 * np.sin(5 * x[i])
        
        # Exponential decay with sinusoidal modulation
        for i in range(self.dim):
            result += 1.5 * np.exp(-0.5 * x[i]**2) * np.sin(4 * x[i])**2
        
        # Cross-dimensional coupling with asymmetric interaction weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = (x[i] + x[j])**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                if i % 2 == 0:
                    result += 0.8 * interaction
                else:
                    result += 0.4 * interaction
        
        # Asymmetric gradient field with modified polynomial terms
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.6 * x[i]**3.5 * np.exp(-0.1 * x[i])
            else:
                result += 0.2 * x[i]**4.5 * np.exp(-0.2 * np.abs(x[i]))
        
        # High-frequency oscillatory component with spatially varying amplitude
        for i in range(self.dim):
            result += 1.8 * np.sin(15 * x[i]) * np.cos(7 * x[i]) * (1 + 0.3 * np.sin(0.5 * x[i]))
        
        # Fractional power and logarithmic interaction terms with altered exponents
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.5 * np.abs(x[i])**1.8 * np.log(np.abs(x[i]) + 1)
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result