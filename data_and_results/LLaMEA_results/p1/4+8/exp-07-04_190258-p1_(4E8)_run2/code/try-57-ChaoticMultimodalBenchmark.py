import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies and exponential damping
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.tan(0.5 * x[i]) * 
                       np.exp(-0.05 * x[i]**2) * np.sin(0.1 * x[i]**3))
        
        # Higher-order saddle point structure with quartic and quintic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**5 - 3 * x[i]**3 + 2 * x[i]) * np.cos(0.5 * x[i])
        
        # Complex cross-term interactions with higher-degree polynomials and trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic interference term with mixed trigonometric and polynomial components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity control
                interference += 0.1 * np.sin(2 * x[i] + 3 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Novel fractal-like self-similar component with logarithmic scaling and hyperbolic tangents
        fractal = 0
        for i in range(self.dim):
            fractal += (np.tanh(2 * x[i]) * np.log(np.abs(x[i]) + 1) * 
                       np.sin(0.3 * x[i]**4) * np.cos(0.7 * x[i]**2))
        
        # Hyperbolic perturbation component to increase landscape irregularity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += (np.sinh(0.5 * x[i]) * np.cosh(0.3 * x[i]) * 
                          np.exp(-0.02 * x[i]**2) * np.sin(0.2 * x[i]**5))
        
        return quadratic + chaotic + saddle + cross + interference + fractal + hyperbolic