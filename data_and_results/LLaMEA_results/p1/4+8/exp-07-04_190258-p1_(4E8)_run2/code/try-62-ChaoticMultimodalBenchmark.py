import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies, exponential damping, and hyperbolic components
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.tan(0.5 * x[i]) * 
                       np.exp(-0.05 * x[i]**2) * np.sin(0.1 * x[i]**3) * 
                       np.cosh(0.2 * x[i]) * np.log(1 + np.abs(x[i])))
        
        # Higher-order saddle point structure with quartic, quintic, and logarithmic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**5 - 3 * x[i]**3 + 2 * x[i]) * np.cos(0.5 * x[i]) * np.log(1 + np.abs(x[i]))
        
        # Complex cross-term interactions with higher-degree polynomials, trigonometric coupling, and fractal-like scaling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * (1 + 0.1 * np.sin(10 * (x[i] + x[j])))
        
        # Additional chaotic interference term with mixed trigonometric, polynomial, and logarithmic components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity control
                interference += 0.1 * np.sin(2 * x[i] + 3 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2) * np.log(1 + np.abs(x[i] - x[j]))
        
        # Fractal-like self-similar structure with recursive scaling and additional chaotic modulation
        fractal = 0
        for i in range(self.dim):
            fractal += 0.05 * np.sin(10 * np.sin(5 * x[i])) * np.cos(3 * x[i]) * (1 + 0.2 * np.sin(20 * x[i]))
        
        return quadratic + chaotic + saddle + cross + interference + fractal